# ValidationRunOut

A validation run and every validation in it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Identifier of the run. Poll &#x60;GET /validations/{run_id}&#x60; with it. | 
**status** | [**RunStatus**](RunStatus.md) | Whether the run is still going. Every validation is final once it is not. | 
**revision** | **int** | Moves forward every time a validation changes. Pass it as &#x60;since&#x60; on the next poll to get only the validations that changed after this response. | 
**target_type** | [**TargetType**](TargetType.md) | What the run validates. | 
**target_id** | **UUID** | Identifier of what is being validated: the connection, or the credentials a change applies to. Null for candidate values, which are not stored anywhere. | 
**validations_passed** | **int** | How many validations reached a passing verdict. One that was skipped or never reached a verdict is not counted here, but is still in &#x60;validations_total&#x60;. | 
**validations_total** | **int** | How many validations the run covers. | 
**started_at** | **datetime** | When the run started. | 
**finished_at** | **datetime** | When the run finished. Null while it is still going. | 
**expires_at** | **datetime** | When the run stops being readable. Measured from the start, not the finish, and never extended, so a slow run is readable for less time after it ends. | 
**validations** | [**List[ValidationOut]**](ValidationOut.md) | The run&#39;s validations, in the order they are declared. A validation stays &#x60;pending&#x60; until it starts. It can wait on a prerequisite, or for earlier validations to finish. A read with &#x60;since&#x60; lists only the validations that changed after that revision, and may list none. | 

## Example

```python
from pycarlo2.models.validation_run_out import ValidationRunOut

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationRunOut from a JSON string
validation_run_out_instance = ValidationRunOut.from_json(json)
# print the JSON string representation of the object
print(ValidationRunOut.to_json())

# convert the object into a dict
validation_run_out_dict = validation_run_out_instance.to_dict()
# create an instance of ValidationRunOut from a dict
validation_run_out_from_dict = ValidationRunOut.from_dict(validation_run_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


