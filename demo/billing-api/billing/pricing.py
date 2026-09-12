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


def tier_for_usage(units: int) -> Tier:
    if units < 0:
        raise ValueError("units must be non-negative")
    for tier in TIERS[:-1]:
        if units <= tier.max_units:
            return tier
    return TIERS[-1]


def round_cents(amount: Decimal) -> Decimal:
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def apply_discount(subtotal: Decimal, percent: int, coupon_active: bool) -> Decimal:
    if not coupon_active or percent <= 0:
        return subtotal
    if percent > 100:
        raise ValueError("percent out of range")
    discounted = subtotal * (Decimal(100 - percent) / Decimal(100))
    return round_cents(discounted)


def calculate_invoice(units: int, percent_off: int = 0, coupon_active: bool = False) -> dict:
    tier = tier_for_usage(units)
    billable = max(units - TIERS[0].max_units, 0) if tier.name != "free" else 0
    subtotal = round_cents(tier.unit_price * billable)
    total = apply_discount(subtotal, percent_off, coupon_active)
    return {
        "tier": tier.name,
        "billable_units": billable,
        "subtotal": subtotal,
        "total": total,
    }


def is_in_trial_window(signup: date, today: date) -> bool:
    if today < signup:
        return False
    return today - signup < timedelta(days=TRIAL_DAYS)


def retry_allowed(attempts: int, last_error: str | None) -> bool:
    if last_error is None:
        return False
    if last_error.startswith("fatal"):
        return False
    return attempts < MAX_RETRIES
