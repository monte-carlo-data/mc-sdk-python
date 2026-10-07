# LookerGitCloneCredentialsValidateIn

Candidate LookML repository credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**username** | **str** | Git user for an HTTPS clone. Send it with &#x60;token&#x60;. | [optional] 
**ssl_ca_data** | **str** | PEM certificate of the CA that signed the git server&#39;s certificate. | [optional] 
**ssl_skip_cert_verification** | **bool** | Skip verifying the git server&#39;s TLS certificate. | [optional] 
**token** | **str** | Access token of &#x60;username&#x60;, for an HTTPS clone. Send this or &#x60;ssh_key&#x60;. Used for this check and not kept. | [optional] 
**ssh_key** | **str** | Private key for an SSH clone, as PEM text including its BEGIN and END lines. Send this or &#x60;username&#x60; and &#x60;token&#x60;. Used for this check and not kept. | [optional] 
**repo_url** | **str** | Clone URL of the LookML repository, over HTTPS or SSH. | 

## Example

```python
from pycarlo2.models.looker_git_clone_credentials_validate_in import LookerGitCloneCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of LookerGitCloneCredentialsValidateIn from a JSON string
looker_git_clone_credentials_validate_in_instance = LookerGitCloneCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(LookerGitCloneCredentialsValidateIn.to_json())

# convert the object into a dict
looker_git_clone_credentials_validate_in_dict = looker_git_clone_credentials_validate_in_instance.to_dict()
# create an instance of LookerGitCloneCredentialsValidateIn from a dict
looker_git_clone_credentials_validate_in_from_dict = LookerGitCloneCredentialsValidateIn.from_dict(looker_git_clone_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


