# ConnectionTypeOut

A connection type your account can add a connection of, and what that connection takes.  A type your plan does not include is not listed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** | The connection type. Credentials for it name this type, and the connection takes its type from them. | 
**name** | **str** | Display name of the connection type. | 
**parent** | [**ConnectionParent**](ConnectionParent.md) | What a connection of this type is added to. Create or reuse one first. | 
**warehouse_type** | [**WarehouseType**](WarehouseType.md) | The type of warehouse the connection goes on. Null unless &#x60;parent&#x60; is &#x60;warehouse&#x60;. Null too for a type any existing warehouse takes, such as &#x60;dbt-cloud-webhook&#x60;. | 
**bi_container_type** | [**NewBiContainerType**](NewBiContainerType.md) | The type of BI container the connection goes on. Null unless &#x60;parent&#x60; is &#x60;bi_container&#x60;. | 
**etl_container_type** | [**NewEtlContainerType**](NewEtlContainerType.md) | The type of ETL container the connection goes on. Null unless &#x60;parent&#x60; is &#x60;etl_container&#x60;. | 
**credentials_required** | **bool** | Whether the connection needs credentials. False for a push-only type: its data is sent to Monte Carlo, and Monte Carlo reaches no system for it. | 
**mc_managed_credentials_operation** | **str** | The operation that stores this type&#39;s credentials with Monte Carlo. Null when Monte Carlo cannot store them. | 
**mc_managed_credentials_secret** | **bool** | Whether storing the credentials with Monte Carlo sends a secret, such as a password or a private key. Null when Monte Carlo cannot store them. | 
**self_hosted_credentials_storages** | [**List[CredentialsStorageType]**](CredentialsStorageType.md) | The stores you run that the credentials can be kept in, with Monte Carlo keeping only where they are. Empty when they cannot be. | 
**requires_deployment** | **bool** | Whether the connection runs through its parent&#39;s deployment. False for a type that reports to Monte Carlo itself, such as Airflow, or whose data is pushed. | 
**requires_one_of_connection_types** | **List[str]** | The warehouse needs a connection of one of these types before one of this type is added. Empty when it needs none. | 
**job_types** | **List[str]** | The collection jobs a connection of this type can run. | 
**is_custom** | **bool** | Whether a collection agent registered the type for your account. A custom type&#39;s connection runs through the deployment of that agent. | 

## Example

```python
from pycarlo2.models.connection_type_out import ConnectionTypeOut

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionTypeOut from a JSON string
connection_type_out_instance = ConnectionTypeOut.from_json(json)
# print the JSON string representation of the object
print(ConnectionTypeOut.to_json())

# convert the object into a dict
connection_type_out_dict = connection_type_out_instance.to_dict()
# create an instance of ConnectionTypeOut from a dict
connection_type_out_from_dict = ConnectionTypeOut.from_dict(connection_type_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


