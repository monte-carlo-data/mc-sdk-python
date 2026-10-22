# ConnectionMatch

How Monte Carlo decides that a dbt Cloud run belongs to the connection's warehouse.  `off` drops no run for its dbt connection. `auto` drops a run whose dbt environment connects to none of the warehouse's own connections. It keeps a run whose dbt connection it cannot identify. `allow_list` drops a run unless one of `allowed_connection_fields` on its dbt environment connection equals one of `allowed_connection_values`.

## Enum

* `OFF` (value: `'off'`)

* `AUTO` (value: `'auto'`)

* `ALLOW_LIST` (value: `'allow_list'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


