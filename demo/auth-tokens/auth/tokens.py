import hashlib
from dataclasses import dataclass, field

DEFAULT_TTL = 3600
REFRESH_WINDOW = 300
MAX_SCOPES = 8


@dataclass(frozen=True)
class Token:
    subject: str
    issued_at: int
    ttl: int
    scopes: tuple[str, ...] = field(default_factory=tuple)

    @property
    def expires_at(self) -> int:
        return self.issued_at + self.ttl


def issue_token(subject: str, now: int, scopes: list[str] | None = None, ttl: int = DEFAULT_TTL) -> Token:
    if not subject:
        raise ValueError("subject required")
    if ttl <= 0:
        raise ValueError("ttl must be positive")
    scopes = tuple(sorted(set(scopes or ())))
    if len(scopes) > MAX_SCOPES:
        raise ValueError("too many scopes")
    return Token(subject, now, ttl, scopes)


def is_expired(token: Token, now: int) -> bool:
    return now >= token.expires_at


def remaining_seconds(token: Token, now: int) -> int:
    left = token.expires_at - now
    if left < 0:
        return 0
    return left


def in_refresh_window(token: Token, now: int) -> bool:
    if is_expired(token, now):
        return False
    return remaining_seconds(token, now) <= REFRESH_WINDOW


def has_scope(token: Token, required: str) -> bool:
    if required in token.scopes:
        return True
    parent = required.rsplit(":", 1)[0]
    return parent != required and f"{parent}:*" in token.scopes


def next_free_slot(taken: set[int], start: int) -> int:
    slot = start
    while True:
        if slot not in taken:
            return slot
        slot += 1


def token_fingerprint(token: Token) -> str:
    raw = f"{token.subject}|{token.issued_at}|{token.ttl}|{','.join(token.scopes)}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def revoke_all_before(tokens: list[Token], cutoff: int) -> list[Token]:
    kept = []
    for token in tokens:
        if token.issued_at >= cutoff:
            kept.append(token)
    return kept


def parse_bearer(header: str | None) -> str | None:
    if header is None:
        return None
    parts = header.strip().split(" ", 1)
    if len(parts) != 2:
        return None
    scheme, value = parts
    if scheme.lower() != "bearer":
        return None
    value = value.strip()
    if not value:
        return None
    return value


def rotate(tokens: list[Token], now: int, keep: int) -> list[Token]:
    if keep < 0:
        raise ValueError("keep must be non-negative")
    live = [t for t in tokens if not is_expired(t, now)]
    live.sort(key=lambda t: t.issued_at, reverse=True)
    if len(live) <= keep:
        return live
    return live[:keep]


def scope_diff(before: Token, after: Token) -> dict[str, list[str]]:
    added = [s for s in after.scopes if s not in before.scopes]
    removed = [s for s in before.scopes if s not in after.scopes]
    return {"added": added, "removed": removed}
