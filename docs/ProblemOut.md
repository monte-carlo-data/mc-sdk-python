# ProblemOut

The error body returned by every failed request.  Every response with a status of 400 or higher has this shape, so a client only has one error contract to handle no matter which endpoint or which failure produced it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Machine-readable code identifying the category of error. Branch on this rather than on &#x60;status&#x60;, because several codes can share one status. | 
**detail** | **str** | Human-readable explanation of this particular occurrence of the error. | 
**errors** | [**List[FieldErrorOut]**](FieldErrorOut.md) | The fields that failed validation. Empty unless this is a validation error. | [optional] 
**extra** | **Dict[str, str]** | Values that parameterize &#x60;message&#x60;, for a client that renders its own text instead of showing &#x60;message&#x60; directly. Absent when there is nothing to report. | [optional] 
**request_id** | **str** | Identifier for this request, also returned in the &#x60;X-Request-Id&#x60; header. Quote it when reporting the error to support. | 
**status** | **int** | HTTP status code, repeated here for clients that only see the body. | 
**title** | **str** | Short, human-readable summary of the category of error. | 
**type** | **str** | URI identifying the category of error. The same category always uses the same URI. | 

## Example

```python
from montecarlo.models.problem_out import ProblemOut

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemOut from a JSON string
problem_out_instance = ProblemOut.from_json(json)
# print the JSON string representation of the object
print(ProblemOut.to_json())

# convert the object into a dict
problem_out_dict = problem_out_instance.to_dict()
# create an instance of ProblemOut from a dict
problem_out_from_dict = ProblemOut.from_dict(problem_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


