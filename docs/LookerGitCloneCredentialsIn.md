# LookerGitCloneCredentialsIn

What to create LookML repository credentials with.  Send `username` and `token` for an HTTPS clone, or `ssh_key` for an SSH clone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Git user for an HTTPS clone. Send it with &#x60;token&#x60;. | [optional] 
**ssl_ca_data** | **str** | PEM certificate of the CA that signed the git server&#39;s certificate. | [optional] 
**ssl_skip_cert_verification** | **bool** | Skip verifying the git server&#39;s TLS certificate. | [optional] 
**token** | **str** | Access token of &#x60;username&#x60;, for an HTTPS clone. Send this or &#x60;ssh_key&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**ssh_key** | **str** | Private key for an SSH clone, as PEM text including its BEGIN and END lines. Send this or &#x60;username&#x60; and &#x60;token&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**repo_url** | **str** | Clone URL of the LookML repository, over HTTPS or SSH. | 

## Example

```python
from montecarlo.models.looker_git_clone_credentials_in import LookerGitCloneCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of LookerGitCloneCredentialsIn from a JSON string
looker_git_clone_credentials_in_instance = LookerGitCloneCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(LookerGitCloneCredentialsIn.to_json())

# convert the object into a dict
looker_git_clone_credentials_in_dict = looker_git_clone_credentials_in_instance.to_dict()
# create an instance of LookerGitCloneCredentialsIn from a dict
looker_git_clone_credentials_in_from_dict = LookerGitCloneCredentialsIn.from_dict(looker_git_clone_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


