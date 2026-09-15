from dataclasses import dataclass
from datetime import date, timedelta
from decimal import ROUND_HALF_UP, Decimal


@dataclass(frozen=True)
class Tier:
    name: str
    unit_price: Decimal
    max_units: int | None


TIERS = [
    Tier("free", Decimal("0.00"), 100),
    Tier("team", Decimal("0.40"), 5000),
    Tier("business", Decimal("0.25"), None),
]

TRIAL_DAYS = 14
MAX_RETRIES = 3
GRACE_DAYS = 3
TAX_RATE = Decimal("0.10")


class GatewayError(Exception):
    pass


def tier_for_usage(units: int) -> Tier:
    if units < 0:
        raise ValueError("units must be non-negative")
    if units <= TIERS[0].max_units:
        return TIERS[0]
    if units <= TIERS[1].max_units:
        return TIERS[1]
    return TIERS[2]


def round_cents(amount: Decimal) -> Decimal:
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def apply_discount(subtotal: Decimal, percent: int, coupon_active: bool) -> Decimal:
    if not coupon_active or percent <= 0:
        return subtotal
    if percent > 100:
        raise ValueError("percent out of range")
    discounted = subtotal * (Decimal(100 - percent) / Decimal(100))
    return round_cents(discounted)


def apply_tax(amount: Decimal, exempt: bool = False) -> Decimal:
    if exempt:
        return amount
    return round_cents(amount * (Decimal(1) + TAX_RATE))


def calculate_invoice(units: int, percent_off: int = 0, coupon_active: bool = False, tax_exempt: bool = False) -> dict:
    tier = tier_for_usage(units)
    billable = max(units - TIERS[0].max_units, 0) if tier.name != "free" else 0
    subtotal = round_cents(tier.unit_price * billable)
    discounted = apply_discount(subtotal, percent_off, coupon_active)
    total = apply_tax(discounted, tax_exempt)
    return {
        "tier": tier.name,
        "billable_units": billable,
        "subtotal": subtotal,
        "discounted": discounted,
        "total": total,
    }


def prorate(amount: Decimal, days_used: int, days_in_period: int) -> Decimal:
    if days_in_period <= 0:
        raise ValueError("period must be positive")
    if days_used >= days_in_period:
        return amount
    if days_used <= 0:
        return Decimal("0.00")
    return round_cents(amount * Decimal(days_used) / Decimal(days_in_period))


def is_in_trial_window(signup: date, today: date) -> bool:
    if today < signup:
        return False
    return today - signup < timedelta(days=TRIAL_DAYS)


def is_overdue(due: date, today: date, grace_days: int = GRACE_DAYS) -> bool:
    return today > due + timedelta(days=grace_days)


def retry_allowed(attempts: int, last_error: str | None) -> bool:
    if last_error is None:
        return False
    if last_error.startswith("fatal"):
        return False
    return attempts < MAX_RETRIES


def parse_coupon(code: str | None) -> tuple[str, int] | None:
    if code is None or not code.strip():
        return None
    name, sep, pct = code.strip().upper().partition("-")
    if not sep or not pct.isdigit():
        return None
    return name, int(pct)


def normalize_email(value: str | None) -> str | None:
    if value is None:
        return None
    cleaned = value.strip().lower()
    if "@" not in cleaned or cleaned.startswith("@") or cleaned.endswith("@"):
        return None
    return cleaned


def can_upgrade(current: str, target: str, balance_due: Decimal) -> bool:
    order = [t.name for t in TIERS]
    if current not in order or target not in order:
        return False
    return order.index(target) > order.index(current) and balance_due <= 0


def charge(gateway, amount: Decimal) -> dict:
    try:
        ref = gateway.charge(amount)
    except GatewayError:
        raise
    return {"ok": True, "ref": ref, "amount": amount}


def refund(gateway, ref: str, amount: Decimal) -> dict:
    if amount <= 0:
        raise ValueError("refund must be positive")
    try:
        gateway.refund(ref, amount)
    except GatewayError as exc:
        return {"ok": False, "error": str(exc)}
    return {"ok": True, "ref": ref, "amount": amount}


def billing_anchor(signup: date, today: date) -> date:
    day = min(signup.day, 28)
    anchor = today.replace(day=day)
    if anchor > today:
        month = anchor.month - 1 or 12
        year = anchor.year if anchor.month != 1 else anchor.year - 1
        anchor = anchor.replace(year=year, month=month)
    return anchor
