# ValidationOut

One validation within a run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Identifier of the validation, unique within the run. | 
**description** | **str** | What the validation checks. | 
**status** | [**ValidationStatus**](ValidationStatus.md) | Whether the validation ran, not whether what it checked is healthy. | 
**is_prerequisite** | **bool** | Whether the rest of the run depends on this one. A prerequisite that does not pass skips every validation waiting on it. | 
**passed** | **bool** | Whether the validation found no blocking problem. Null until it reaches a verdict, and for one that never did. | 
**errors** | [**List[ValidationFailureOut]**](ValidationFailureOut.md) | Blocking problems. Empty when the validation passed. | 
**warnings** | [**List[ValidationFailureOut]**](ValidationFailureOut.md) | Problems that did not stop the validation from passing. | 
**additional_data** | **Dict[str, object]** | Extra detail the validation reported, if it reported any. | 
**truncated** | **bool** | Whether some detail was too large to return and was clipped. The problems that are here are still accurate; there may have been more of them. | 

## Example

```python
from montecarlo.models.validation_out import ValidationOut

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationOut from a JSON string
validation_out_instance = ValidationOut.from_json(json)
# print the JSON string representation of the object
print(ValidationOut.to_json())

# convert the object into a dict
validation_out_dict = validation_out_instance.to_dict()
# create an instance of ValidationOut from a dict
validation_out_from_dict = ValidationOut.from_dict(validation_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


