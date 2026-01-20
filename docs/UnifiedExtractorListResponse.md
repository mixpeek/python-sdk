# UnifiedExtractorListResponse

Response for listing all extractors available to a namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the request succeeded | [optional] [default to True]
**extractors** | [**List[UnifiedExtractorResponse]**](UnifiedExtractorResponse.md) | List of all available extractors | 
**total** | **int** | Total number of extractors | 
**namespace_id** | **str** | Namespace ID | 
**builtin_count** | **int** | Number of builtin extractors | 
**custom_count** | **int** | Number of custom extractors (org + namespace level) | 

## Example

```python
from mixpeek.models.unified_extractor_list_response import UnifiedExtractorListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedExtractorListResponse from a JSON string
unified_extractor_list_response_instance = UnifiedExtractorListResponse.from_json(json)
# print the JSON string representation of the object
print(UnifiedExtractorListResponse.to_json())

# convert the object into a dict
unified_extractor_list_response_dict = unified_extractor_list_response_instance.to_dict()
# create an instance of UnifiedExtractorListResponse from a dict
unified_extractor_list_response_from_dict = UnifiedExtractorListResponse.from_dict(unified_extractor_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


