import pytest

from auth import Token, in_refresh_window, is_expired, issue_token, remaining_seconds


def test_issue_token_basic():
    t = issue_token("alice", 1000, ["read", "write"])
    assert t.subject == "alice"
    assert t.issued_at == 1000
    assert t.ttl == 3600
    assert t.scopes == ("read", "write")


def test_issue_token_dedups_and_sorts_scopes():
    t = issue_token("bob", 0, ["write", "read", "read"])
    assert t.scopes == ("read", "write")


def test_issue_token_requires_subject():
    with pytest.raises(ValueError):
        issue_token("", 0)


def test_issue_token_rejects_zero_ttl():
    with pytest.raises(ValueError):
        issue_token("x", 0, ttl=0)
    issue_token("x", 0, ttl=1)


def test_issue_token_scope_limit():
    issue_token("x", 0, [f"s{i}" for i in range(8)])
    with pytest.raises(ValueError):
        issue_token("x", 0, [f"s{i}" for i in range(9)])


def test_is_expired_boundary():
    t = Token("a", 100, 50)
    assert not is_expired(t, 149)
    assert is_expired(t, 150)
    assert is_expired(t, 151)


def test_remaining_seconds():
    t = Token("a", 100, 50)
    assert remaining_seconds(t, 100) == 50
    assert remaining_seconds(t, 149) == 1
    assert remaining_seconds(t, 150) == 0
    assert remaining_seconds(t, 999) == 0


def test_refresh_window_boundaries():
    t = Token("a", 0, 1000)
    assert not in_refresh_window(t, 699)
    assert in_refresh_window(t, 700)
    assert in_refresh_window(t, 999)
    assert not in_refresh_window(t, 1000)
