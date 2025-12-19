# TextIndexParams

Configuration for text index.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'text']
**tokenizer** | [**TokenizerType**](TokenizerType.md) |  | [optional] 
**min_token_len** | **int** |  | [optional] [default to 2]
**max_token_len** | **int** |  | [optional] [default to 15]
**lowercase** | **bool** |  | [optional] [default to True]

## Example

```python
from mixpeek.models.text_index_params import TextIndexParams

# TODO update the JSON string below
json = "{}"
# create an instance of TextIndexParams from a JSON string
text_index_params_instance = TextIndexParams.from_json(json)
# print the JSON string representation of the object
print(TextIndexParams.to_json())

# convert the object into a dict
text_index_params_dict = text_index_params_instance.to_dict()
# create an instance of TextIndexParams from a dict
text_index_params_from_dict = TextIndexParams.from_dict(text_index_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


