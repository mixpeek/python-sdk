# ClarificationOption

A single option presented to the user for clarifying intent.  Attributes:     label: Short label for the option (e.g., \"Search existing data\")     description: Detailed explanation of what this option means     action: Recommended tool/action to use if user selects this option

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Option label | 
**description** | **str** | Option description | 
**action** | **str** | Recommended action/tool | 

## Example

```python
from mixpeek.models.clarification_option import ClarificationOption

# TODO update the JSON string below
json = "{}"
# create an instance of ClarificationOption from a JSON string
clarification_option_instance = ClarificationOption.from_json(json)
# print the JSON string representation of the object
print(ClarificationOption.to_json())

# convert the object into a dict
clarification_option_dict = clarification_option_instance.to_dict()
# create an instance of ClarificationOption from a dict
clarification_option_from_dict = ClarificationOption.from_dict(clarification_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


