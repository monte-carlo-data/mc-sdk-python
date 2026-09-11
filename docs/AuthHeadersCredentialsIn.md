# AuthHeadersCredentialsIn

The HTTP headers Monte Carlo presents when it calls the agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **Dict[str, str]** | Header names, each mapped to the value to send for it. Names have to be valid HTTP header names. At most 20 headers, each value up to 8192 characters. | 

## Example

```python
from montecarlo.models.auth_headers_credentials_in import AuthHeadersCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of AuthHeadersCredentialsIn from a JSON string
auth_headers_credentials_in_instance = AuthHeadersCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(AuthHeadersCredentialsIn.to_json())

# convert the object into a dict
auth_headers_credentials_in_dict = auth_headers_credentials_in_instance.to_dict()
# create an instance of AuthHeadersCredentialsIn from a dict
auth_headers_credentials_in_from_dict = AuthHeadersCredentialsIn.from_dict(auth_headers_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


