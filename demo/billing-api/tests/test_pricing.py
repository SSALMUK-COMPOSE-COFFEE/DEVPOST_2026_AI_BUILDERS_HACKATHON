from datetime import date
from decimal import Decimal

import pytest

from billing import (
    Tier,
    apply_discount,
    calculate_invoice,
    is_in_trial_window,
    retry_allowed,
    round_cents,
    tier_for_usage,
)
from billing.pricing import MAX_RETRIES, TIERS, TRIAL_DAYS


def test_tiers_defined():
    assert len(TIERS) == 3


def test_tier_names():
    assert [t.name for t in TIERS] == ["free", "team", "business"]


def test_tier_is_frozen_dataclass():
    with pytest.raises(Exception):
        TIERS[0].name = "x"


def test_tier_for_usage_returns_tier():
    assert isinstance(tier_for_usage(10), Tier)


def test_tier_for_usage_free():
    assert tier_for_usage(10).name == "free"


def test_tier_for_usage_team():
    assert tier_for_usage(1000).name == "team"


def test_tier_for_usage_business():
    assert tier_for_usage(100000).name == "business"


def test_tier_for_usage_rejects_negative():
    with pytest.raises(ValueError):
        tier_for_usage(-5)


def test_round_cents_returns_decimal():
    assert isinstance(round_cents(Decimal("1.5")), Decimal)


def test_round_cents_two_places():
    assert round_cents(Decimal("1.234")) == Decimal("1.23")


def test_round_cents_pads():
    assert round_cents(Decimal("2")) == Decimal("2.00")


def test_apply_discount_returns_decimal():
    assert isinstance(apply_discount(Decimal("10.00"), 20, True), Decimal)


def test_apply_discount_inactive_coupon_unchanged():
    assert apply_discount(Decimal("10.00"), 20, False) == Decimal("10.00")


def test_apply_discount_half():
    assert apply_discount(Decimal("10.00"), 50, True) == Decimal("5.00")


def test_apply_discount_reduces_total():
    assert apply_discount(Decimal("80.00"), 25, True) < Decimal("80.00")


def test_apply_discount_rejects_over_100():
    with pytest.raises(ValueError):
        apply_discount(Decimal("10.00"), 150, True)


def test_invoice_is_dict():
    assert isinstance(calculate_invoice(600), dict)


def test_invoice_keys():
    assert set(calculate_invoice(600)) == {"tier", "billable_units", "subtotal", "total"}


def test_invoice_tier_team():
    assert calculate_invoice(600)["tier"] == "team"


def test_invoice_tier_business():
    assert calculate_invoice(20000)["tier"] == "business"


def test_invoice_free_total_zero():
    assert calculate_invoice(10)["total"] == Decimal("0.00")


def test_invoice_free_no_billable_units():
    assert calculate_invoice(10)["billable_units"] == 0


def test_invoice_team_positive():
    assert calculate_invoice(600)["total"] > 0


def test_invoice_business_positive():
    assert calculate_invoice(20000)["total"] > 0


def test_invoice_subtotal_is_decimal():
    assert isinstance(calculate_invoice(600)["subtotal"], Decimal)


def test_invoice_total_without_coupon_matches_subtotal():
    inv = calculate_invoice(600)
    assert inv["total"] == inv["subtotal"]


def test_invoice_coupon_lowers_total():
    inv = calculate_invoice(600, percent_off=10, coupon_active=True)
    assert inv["total"] < inv["subtotal"]


def test_invoice_inactive_coupon_ignored():
    inv = calculate_invoice(600, percent_off=10, coupon_active=False)
    assert inv["total"] == inv["subtotal"]


def test_invoice_defaults():
    assert calculate_invoice(600) == calculate_invoice(600, 0, False)


def test_trial_days_constant():
    assert TRIAL_DAYS == 14


def test_trial_window_inside():
    assert is_in_trial_window(date(2026, 1, 1), date(2026, 1, 5))


def test_trial_window_outside():
    assert not is_in_trial_window(date(2026, 1, 1), date(2026, 3, 1))


def test_trial_window_before_signup():
    assert not is_in_trial_window(date(2026, 1, 10), date(2026, 1, 1))


def test_trial_window_returns_bool():
    assert isinstance(is_in_trial_window(date(2026, 1, 1), date(2026, 1, 2)), bool)


def test_max_retries_constant():
    assert MAX_RETRIES == 3


def test_retry_allowed_no_error():
    assert not retry_allowed(0, None)


def test_retry_allowed_fatal():
    assert not retry_allowed(0, "fatal: disk")


def test_retry_allowed_first_attempt():
    assert retry_allowed(0, "timeout")


def test_retry_allowed_many_attempts():
    assert not retry_allowed(10, "timeout")


def test_retry_allowed_returns_bool():
    assert isinstance(retry_allowed(1, "timeout"), bool)
