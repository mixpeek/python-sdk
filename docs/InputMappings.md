# InputMappings

Mapping from extractor input names to source field paths. Tells the extractor which source fields to process. Example: {'image': 'thumbnail_url', 'text': 'description'}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from mixpeek.models.input_mappings import InputMappings

# TODO update the JSON string below
json = "{}"
# create an instance of InputMappings from a JSON string
input_mappings_instance = InputMappings.from_json(json)
# print the JSON string representation of the object
print(InputMappings.to_json())

# convert the object into a dict
input_mappings_dict = input_mappings_instance.to_dict()
# create an instance of InputMappings from a dict
input_mappings_from_dict = InputMappings.from_dict(input_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


