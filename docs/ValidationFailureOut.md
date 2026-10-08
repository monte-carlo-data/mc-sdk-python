# ValidationFailureOut

One reason a validation reported a problem.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**friendly_message** | **str** | What went wrong, in terms a reader can act on. Null when none was given. | 
**resolution** | **str** | What to change to fix it. Null when there is no specific step to suggest. | 
**cause** | **str** | The underlying error the check ran into, as the system reported it. Values that look like passwords or tokens are masked, and long text is shortened. Null when none was reported. | 
**stack_trace** | **str** | The call stack the system reported with the error, ending at the most recent call. Values that look like passwords or tokens are masked, and a long trace keeps only its end. Null when none was reported. | 

## Example

```python
from pycarlo2.models.validation_failure_out import ValidationFailureOut

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationFailureOut from a JSON string
validation_failure_out_instance = ValidationFailureOut.from_json(json)
# print the JSON string representation of the object
print(ValidationFailureOut.to_json())

# convert the object into a dict
validation_failure_out_dict = validation_failure_out_instance.to_dict()
# create an instance of ValidationFailureOut from a dict
validation_failure_out_from_dict = ValidationFailureOut.from_dict(validation_failure_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


