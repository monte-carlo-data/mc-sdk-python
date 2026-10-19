# LookerGitCloneCredentialsPatch

A change to existing LookML repository credentials.  A field left out is unchanged. The `ssl_*` fields set to null are cleared. A secret set to null is unchanged. `repo_url` cannot be cleared, and neither can `username` for an HTTPS clone, which needs one. Sending `ssh_key` drops a stored username and token, and sending `username` or `token` drops a stored key. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Git user for an HTTPS clone. Send it with &#x60;token&#x60;. | [optional] 
**ssl_ca_data** | **str** | PEM certificate of the CA that signed the git server&#39;s certificate. | [optional] 
**ssl_skip_cert_verification** | **bool** | Skip verifying the git server&#39;s TLS certificate. | [optional] 
**token** | **str** | Access token of &#x60;username&#x60;, for an HTTPS clone. Send this or &#x60;ssh_key&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**ssh_key** | **str** | Private key for an SSH clone, as PEM text including its BEGIN and END lines. Send this or &#x60;username&#x60; and &#x60;token&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**repo_url** | **str** | Clone URL of the LookML repository, over HTTPS or SSH. Changing it requires sending the credentials&#39; secrets again. | [optional] 

## Example

```python
from pycarlo2.models.looker_git_clone_credentials_patch import LookerGitCloneCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of LookerGitCloneCredentialsPatch from a JSON string
looker_git_clone_credentials_patch_instance = LookerGitCloneCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(LookerGitCloneCredentialsPatch.to_json())

# convert the object into a dict
looker_git_clone_credentials_patch_dict = looker_git_clone_credentials_patch_instance.to_dict()
# create an instance of LookerGitCloneCredentialsPatch from a dict
looker_git_clone_credentials_patch_from_dict = LookerGitCloneCredentialsPatch.from_dict(looker_git_clone_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


