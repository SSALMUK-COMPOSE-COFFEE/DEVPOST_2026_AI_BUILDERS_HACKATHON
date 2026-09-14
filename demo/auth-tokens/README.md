# demo/auth-tokens

Token issuance, expiry, refresh window, scope matching, and slot allocation.
Line coverage is around 60%: `has_scope`, `token_fingerprint`, and
`revoke_all_before` have no tests at all. The tests that do exist check
boundaries, so the mutation score is higher than the coverage number suggests.

One mutant loops forever on purpose. It is reported as a timeout, not a kill.
