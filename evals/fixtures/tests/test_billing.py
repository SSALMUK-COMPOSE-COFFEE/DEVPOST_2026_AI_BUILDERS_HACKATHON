from datetime import date
from decimal import Decimal

import pytest

from billing import (
    GatewayError,
    apply_discount,
    apply_tax,
    billing_anchor,
    calculate_invoice,
    can_upgrade,
    charge,
    is_in_trial_window,
    is_overdue,
    normalize_email,
    parse_coupon,
    prorate,
    refund,
    retry_allowed,
    round_cents,
    tier_for_usage,
)


class FakeGateway:
    def __init__(self, fail=False):
        self.fail = fail
        self.calls = []

    def charge(self, amount):
        if self.fail:
            raise GatewayError("declined")
        self.calls.append(("charge", amount))
        return "ch_1"

    def refund(self, ref, amount):
        if self.fail:
            raise GatewayError("declined")
        self.calls.append(("refund", ref, amount))


def test_tier_for_usage_free():
    assert tier_for_usage(50).name == "free"


def test_tier_for_usage_team():
    assert tier_for_usage(2500).name == "team"


def test_tier_for_usage_business():
    assert tier_for_usage(20000).name == "business"


def test_tier_for_usage_negative_raises():
    with pytest.raises(ValueError):
        tier_for_usage(-5)


def test_round_cents():
    assert round_cents(Decimal("1.234")) == Decimal("1.23")


def test_apply_discount_inactive():
    assert apply_discount(Decimal("10.00"), 20, False) == Decimal("10.00")


def test_apply_discount_applies():
    assert apply_discount(Decimal("10.00"), 20, True) == Decimal("8.00")


def test_apply_discount_over_100_raises():
    with pytest.raises(ValueError):
        apply_discount(Decimal("10.00"), 150, True)


def test_apply_tax():
    assert apply_tax(Decimal("10.00")) == Decimal("11.00")


def test_apply_tax_exempt():
    assert apply_tax(Decimal("10.00"), exempt=True) == Decimal("10.00")


def test_calculate_invoice_free():
    inv = calculate_invoice(50)
    assert inv["tier"] == "free"
    assert inv["total"] == Decimal("0.00")


def test_calculate_invoice_team_with_coupon():
    inv = calculate_invoice(600, percent_off=10, coupon_active=True)
    assert inv["billable_units"] == 500
    assert inv["subtotal"] == Decimal("200.00")
    assert inv["discounted"] == Decimal("180.00")
    assert inv["total"] == Decimal("198.00")


def test_prorate_partial():
    assert prorate(Decimal("30.00"), 10, 30) == Decimal("10.00")


def test_prorate_full_period():
    assert prorate(Decimal("30.00"), 45, 30) == Decimal("30.00")


def test_prorate_unused():
    assert prorate(Decimal("30.00"), -2, 30) == Decimal("0.00")


def test_prorate_bad_period():
    with pytest.raises(ValueError):
        prorate(Decimal("30.00"), 1, 0)


def test_trial_window_inside():
    assert is_in_trial_window(date(2026, 1, 1), date(2026, 1, 5))


def test_trial_window_outside():
    assert not is_in_trial_window(date(2026, 1, 1), date(2026, 3, 1))


def test_trial_window_before_signup():
    assert not is_in_trial_window(date(2026, 1, 10), date(2026, 1, 1))


def test_overdue():
    assert is_overdue(date(2026, 1, 1), date(2026, 1, 20))


def test_not_overdue():
    assert not is_overdue(date(2026, 1, 1), date(2026, 1, 2))


def test_retry_allowed_no_error():
    assert not retry_allowed(0, None)


def test_retry_allowed_fatal():
    assert not retry_allowed(0, "fatal: disk")


def test_retry_allowed_under_limit():
    assert retry_allowed(1, "timeout")


def test_retry_allowed_over_limit():
    assert not retry_allowed(10, "timeout")


def test_parse_coupon_valid():
    assert parse_coupon(" save-20 ") == ("SAVE", 20)


def test_parse_coupon_empty():
    assert parse_coupon(None) is None
    assert parse_coupon("   ") is None


def test_parse_coupon_malformed():
    assert parse_coupon("SAVE20") is None


def test_normalize_email():
    assert normalize_email("  Foo@Example.com ") == "foo@example.com"


def test_normalize_email_none():
    assert normalize_email(None) is None


def test_normalize_email_invalid():
    assert normalize_email("nope") is None


def test_can_upgrade():
    assert can_upgrade("free", "team", Decimal("0"))


def test_can_upgrade_downgrade():
    assert not can_upgrade("team", "free", Decimal("0"))


def test_can_upgrade_unknown():
    assert not can_upgrade("gold", "team", Decimal("0"))


def test_charge_ok():
    gw = FakeGateway()
    assert charge(gw, Decimal("5.00")) == {"ok": True, "ref": "ch_1", "amount": Decimal("5.00")}


def test_charge_declined():
    with pytest.raises(GatewayError):
        charge(FakeGateway(fail=True), Decimal("5.00"))


def test_refund_ok():
    gw = FakeGateway()
    assert refund(gw, "ch_1", Decimal("2.00"))["ok"] is True


def test_refund_declined():
    assert refund(FakeGateway(fail=True), "ch_1", Decimal("2.00"))["ok"] is False


def test_refund_nonpositive():
    with pytest.raises(ValueError):
        refund(FakeGateway(), "ch_1", Decimal("0"))


def test_billing_anchor_same_month():
    assert billing_anchor(date(2026, 1, 10), date(2026, 3, 15)) == date(2026, 3, 10)


def test_billing_anchor_previous_month():
    assert billing_anchor(date(2026, 1, 20), date(2026, 3, 15)) == date(2026, 2, 20)


def test_billing_anchor_january_rollover():
    assert billing_anchor(date(2025, 12, 31), date(2026, 1, 15)) == date(2025, 12, 28)
