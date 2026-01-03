# CustomCTA

Optional custom button in header that opens a markdown modal.  Allows users to add a custom call-to-action button in the header bar that opens a modal with markdown content when clicked.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Button label text displayed in the header | 
**markdown_content** | **str** | Markdown content displayed in the modal when button is clicked. Supports standard markdown syntax. | 

## Example

```python
from mixpeek.models.custom_cta import CustomCTA

# TODO update the JSON string below
json = "{}"
# create an instance of CustomCTA from a JSON string
custom_cta_instance = CustomCTA.from_json(json)
# print the JSON string representation of the object
print(CustomCTA.to_json())

# convert the object into a dict
custom_cta_dict = custom_cta_instance.to_dict()
# create an instance of CustomCTA from a dict
custom_cta_from_dict = CustomCTA.from_dict(custom_cta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


