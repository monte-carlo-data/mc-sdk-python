# CurrentUserOut

The identity the request was authenticated as, and the account it resolved to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Unique identifier of the user. | 
**email** | **str** | Email address of the user. An identity with no mailbox of its own, such as an AI agent, carries a display label here instead. | 
**first_name** | **str** | Given name of the user. Null when it is not set. | [optional] 
**last_name** | **str** | Family name of the user. Null when it is not set. | [optional] 
**identity_type** | [**IdentityType**](IdentityType.md) | What kind of identity this is. It does not decide what the identity may do — that comes from the authorization groups it belongs to. | 
**account_id** | **UUID** | Unique identifier of the caller&#39;s account. | 
**account_name** | **str** | Display name of the account. Null when the account has no name. | [optional] 
**account_frozen** | **bool** | Whether the account is paused. While it is, this endpoint still answers but every other one returns 403 with the code &#x60;account_frozen&#x60;. | 
**auth_groups** | **List[str]** | Names of the authorization groups this user belongs to. They determine what the user is permitted to do. | [optional] 

## Example

```python
from pycarlo2.models.current_user_out import CurrentUserOut

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentUserOut from a JSON string
current_user_out_instance = CurrentUserOut.from_json(json)
# print the JSON string representation of the object
print(CurrentUserOut.to_json())

# convert the object into a dict
current_user_out_dict = current_user_out_instance.to_dict()
# create an instance of CurrentUserOut from a dict
current_user_out_from_dict = CurrentUserOut.from_dict(current_user_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


