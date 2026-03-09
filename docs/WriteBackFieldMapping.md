# WriteBackFieldMapping

Maps a field from retriever results back to the document.  Controls how retriever result fields are written to the source document.  Attributes:     source_field: Field path in retriever result (dot notation for nested fields)     target_field: Field name to write on the document     mode: How to aggregate values across multiple results:         - \"first\": Write value from first result only (default)         - \"all_as_array\": Collect values from all results into a list         - \"concat\": Concatenate string values with \", \" separator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_field** | **str** | Field path in retriever result (dot notation supported) | 
**target_field** | **str** | Field name to write on the document | 
**mode** | **str** | How to aggregate values from multiple results. &#39;first&#39;: top result only. &#39;all_as_array&#39;: collect into list. &#39;concat&#39;: join strings with &#39;, &#39;. | [optional] [default to 'first']

## Example

```python
from mixpeek.models.write_back_field_mapping import WriteBackFieldMapping

# TODO update the JSON string below
json = "{}"
# create an instance of WriteBackFieldMapping from a JSON string
write_back_field_mapping_instance = WriteBackFieldMapping.from_json(json)
# print the JSON string representation of the object
print(WriteBackFieldMapping.to_json())

# convert the object into a dict
write_back_field_mapping_dict = write_back_field_mapping_instance.to_dict()
# create an instance of WriteBackFieldMapping from a dict
write_back_field_mapping_from_dict = WriteBackFieldMapping.from_dict(write_back_field_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


