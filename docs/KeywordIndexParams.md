# KeywordIndexParams

Configuration for keyword index.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'keyword']
**is_tenant** | **bool** |  | [optional] [default to False]

## Example

```python
from mixpeek.models.keyword_index_params import KeywordIndexParams

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordIndexParams from a JSON string
keyword_index_params_instance = KeywordIndexParams.from_json(json)
# print the JSON string representation of the object
print(KeywordIndexParams.to_json())

# convert the object into a dict
keyword_index_params_dict = keyword_index_params_instance.to_dict()
# create an instance of KeywordIndexParams from a dict
keyword_index_params_from_dict = KeywordIndexParams.from_dict(keyword_index_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


