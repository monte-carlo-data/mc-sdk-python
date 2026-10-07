# LookerGitCloneCredentialsOut

LookML repository credentials Monte Carlo stores. The token and the SSH key are never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**repo_url** | **str** | Clone URL of the LookML repository, over HTTPS or SSH. | 
**username** | **str** | Git user. Null for an SSH clone. | 
**ssl_ca_data** | **str** | PEM certificate of the CA that signed the git server&#39;s certificate. Null unless set. | 
**ssl_skip_cert_verification** | **bool** | Skip verifying the git server&#39;s TLS certificate. Null unless set. | 

## Example

```python
from pycarlo2.models.looker_git_clone_credentials_out import LookerGitCloneCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of LookerGitCloneCredentialsOut from a JSON string
looker_git_clone_credentials_out_instance = LookerGitCloneCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(LookerGitCloneCredentialsOut.to_json())

# convert the object into a dict
looker_git_clone_credentials_out_dict = looker_git_clone_credentials_out_instance.to_dict()
# create an instance of LookerGitCloneCredentialsOut from a dict
looker_git_clone_credentials_out_from_dict = LookerGitCloneCredentialsOut.from_dict(looker_git_clone_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


