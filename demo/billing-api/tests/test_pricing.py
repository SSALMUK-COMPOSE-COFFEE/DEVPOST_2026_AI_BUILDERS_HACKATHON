from datetime import date
from decimal import Decimal

import pytest

from billing import (
    apply_discount,
    calculate_invoice,
    is_in_trial_window,
    retry_allowed,
    round_cents,
    tier_for_usage,
)


def test_tier_for_usage_free():
    assert tier_for_usage(0).name == "free"
    assert tier_for_usage(50).name == "free"


def test_tier_for_usage_team():
    assert tier_for_usage(500).name == "team"
    assert tier_for_usage(3000).name == "team"


def test_tier_for_usage_business():
    assert tier_for_usage(10000).name == "business"
    assert tier_for_usage(999999).name == "business"


def test_tier_for_usage_negative_raises():
    with pytest.raises(ValueError):
        tier_for_usage(-1)


def test_round_cents_basic():
    assert round_cents(Decimal("1.234")) == Decimal("1.23")
    assert round_cents(Decimal("1.2")) == Decimal("1.20")


def test_round_cents_zero():
    assert round_cents(Decimal("0")) == Decimal("0.00")


def test_apply_discount_inactive_coupon():
    assert apply_discount(Decimal("10.00"), 20, False) == Decimal("10.00")


def test_apply_discount_zero_percent():
    assert apply_discount(Decimal("10.00"), 0, True) == Decimal("10.00")


def test_apply_discount_applies():
    assert apply_discount(Decimal("10.00"), 20, True) == Decimal("8.00")
    assert apply_discount(Decimal("99.99"), 50, True) == Decimal("50.00")


def test_apply_discount_over_100_raises():
    with pytest.raises(ValueError):
        apply_discount(Decimal("10.00"), 150, True)


def test_calculate_invoice_free():
    inv = calculate_invoice(50)
    assert inv["tier"] == "free"
    assert inv["billable_units"] == 0
    assert inv["total"] == Decimal("0.00")


def test_calculate_invoice_team():
    inv = calculate_invoice(600)
    assert inv["tier"] == "team"
    assert inv["billable_units"] == 500
    assert inv["subtotal"] == Decimal("200.00")
    assert inv["total"] == Decimal("200.00")


def test_calculate_invoice_team_with_coupon():
    inv = calculate_invoice(600, percent_off=10, coupon_active=True)
    assert inv["total"] == Decimal("180.00")


def test_calculate_invoice_business():
    inv = calculate_invoice(20000)
    assert inv["tier"] == "business"
    assert inv["billable_units"] == 19900
    assert inv["subtotal"] == Decimal("4975.00")


def test_trial_window_inside():
    assert is_in_trial_window(date(2026, 1, 1), date(2026, 1, 5))


def test_trial_window_outside():
    assert not is_in_trial_window(date(2026, 1, 1), date(2026, 3, 1))


def test_trial_window_before_signup():
    assert not is_in_trial_window(date(2026, 1, 10), date(2026, 1, 1))


def test_retry_allowed_no_error():
    assert not retry_allowed(0, None)


def test_retry_allowed_fatal():
    assert not retry_allowed(0, "fatal: disk")


def test_retry_allowed_under_limit():
    assert retry_allowed(1, "timeout")


def test_retry_allowed_way_over_limit():
    assert not retry_allowed(10, "timeout")
