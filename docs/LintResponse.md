# LintResponse

Response from the lint endpoint.  Example:     {         \"valid\": true,         \"results\": [...],         \"summary\": {\"error\": 0, \"warning\": 2, \"info\": 3}     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | Whether the manifest is valid (no errors, warnings OK) | 
**results** | [**List[LintResult]**](LintResult.md) | List of lint results | [optional] 
**summary** | **Dict[str, int]** | Count of results by severity | [optional] 

## Example

```python
from mixpeek.models.lint_response import LintResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LintResponse from a JSON string
lint_response_instance = LintResponse.from_json(json)
# print the JSON string representation of the object
print(LintResponse.to_json())

# convert the object into a dict
lint_response_dict = lint_response_instance.to_dict()
# create an instance of LintResponse from a dict
lint_response_from_dict = LintResponse.from_dict(lint_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


