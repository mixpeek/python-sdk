# LintResult

A single lint result with actionable suggestion.  Example:     {         \"code\": \"UNUSED_EXTRACTOR\",         \"severity\": \"warning\",         \"message\": \"Feature extractor 'text_extractor' in namespace 'my_ns' is not used by any collection\",         \"location\": \"namespaces[0].feature_extractors[1]\",         \"suggestion\": \"Remove the unused extractor or add a collection that uses it\",         \"fix_example\": \"collections:\\n  - name: text_docs\\n    feature_extractor:\\n      name: text_extractor\"     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Lint rule code (e.g., &#39;UNUSED_EXTRACTOR&#39;, &#39;MISSING_CACHE_CONFIG&#39;) | 
**severity** | [**LintSeverity**](LintSeverity.md) | Severity level: error, warning, or info | 
**message** | **str** | Human-readable description of the issue | 
**location** | **str** | Path to the problematic element (e.g., &#39;retrievers[0].stages[2]&#39;) | 
**suggestion** | **str** | Actionable suggestion for fixing the issue | 
**fix_example** | **str** | Optional YAML example showing the correct configuration | [optional] 

## Example

```python
from mixpeek.models.lint_result import LintResult

# TODO update the JSON string below
json = "{}"
# create an instance of LintResult from a JSON string
lint_result_instance = LintResult.from_json(json)
# print the JSON string representation of the object
print(LintResult.to_json())

# convert the object into a dict
lint_result_dict = lint_result_instance.to_dict()
# create an instance of LintResult from a dict
lint_result_from_dict = LintResult.from_dict(lint_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


