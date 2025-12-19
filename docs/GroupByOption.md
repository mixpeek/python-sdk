# GroupByOption

Options for grouping results by a specific field.  Attributes:     field: The field to group by.     max_features: The maximum number of features (documents) to return per group.     sort: Optional sorting options to apply within each group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The field to group by. | 
**max_features** | **int** | The maximum number of features (documents) to return per group. | [optional] [default to 10]
**sort** | [**SortOption**](SortOption.md) | Optional sorting options to apply within each group. | [optional] 

## Example

```python
from mixpeek.models.group_by_option import GroupByOption

# TODO update the JSON string below
json = "{}"
# create an instance of GroupByOption from a JSON string
group_by_option_instance = GroupByOption.from_json(json)
# print the JSON string representation of the object
print(GroupByOption.to_json())

# convert the object into a dict
group_by_option_dict = group_by_option_instance.to_dict()
# create an instance of GroupByOption from a dict
group_by_option_from_dict = GroupByOption.from_dict(group_by_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


