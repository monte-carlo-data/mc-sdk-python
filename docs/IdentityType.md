# IdentityType

What kind of identity a user record represents.  `user` is a person who signs in. `service` is an API key or OAuth client acting for the account. `agent` is a Monte Carlo AI agent acting within one of your domains. `system` is Monte Carlo itself acting on the account's behalf, for example while handling a support request.  This is not an authorization role. What an identity may do comes from the authorization groups it belongs to.

## Enum

* `USER` (value: `'user'`)

* `SERVICE` (value: `'service'`)

* `SYSTEM` (value: `'system'`)

* `AGENT` (value: `'agent'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


