# CustomConnectorTypeOut

A custom connector type: an integration a collection agent registered for your account.  Use its `id` as the connection type of self-hosted credentials, and create the warehouse, ETL container or BI container for it on its `deployment_id`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the custom connector type, used as a connection type. | 
**name** | **str** | Display name of the connector. Supplied by the collection agent that registered it, and not validated. | 
**asset_class** | [**CustomConnectorAssetClass**](CustomConnectorAssetClass.md) | What the connector connects to: a warehouse, an ETL tool or a BI tool. | 
**collection_agent_id** | **UUID** | The collection agent that registered the connector. It may name an agent the collection agents endpoints no longer list. | 
**deployment_id** | **UUID** | The deployment of the collection agent that registered the connector. Its connections run there. The id may name a deployment the deployments endpoints do not list. | 
**job_types** | **List[str]** | The collection jobs the connector runs. | 
**icon_url** | **str** | Icon for the connector. Supplied by the collection agent, not validated, and never fetched by Monte Carlo. Null for a warehouse connector, or when none was supplied. | 
**terminology** | [**CustomConnectorTerminology**](CustomConnectorTerminology.md) | The connector&#39;s nouns for its tiers. Set only for an ETL connector. | 
**capabilities** | [**CustomConnectorCapabilities**](CustomConnectorCapabilities.md) | What the connector supports. Set only for a warehouse connector. | 
**created_time** | **datetime** | When the connector type was first registered. | 
**updated_time** | **datetime** | When the connector type was last registered. | 

## Example

```python
from pycarlo2.models.custom_connector_type_out import CustomConnectorTypeOut

# TODO update the JSON string below
json = "{}"
# create an instance of CustomConnectorTypeOut from a JSON string
custom_connector_type_out_instance = CustomConnectorTypeOut.from_json(json)
# print the JSON string representation of the object
print(CustomConnectorTypeOut.to_json())

# convert the object into a dict
custom_connector_type_out_dict = custom_connector_type_out_instance.to_dict()
# create an instance of CustomConnectorTypeOut from a dict
custom_connector_type_out_from_dict = CustomConnectorTypeOut.from_dict(custom_connector_type_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


