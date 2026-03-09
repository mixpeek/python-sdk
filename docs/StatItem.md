# StatItem

A single stat item for the stats bar.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Stat label (e.g. &#39;Total Ads&#39;) | 
**value** | **str** | Stat value (e.g. &#39;12,400+&#39;) | 

## Example

```python
from mixpeek.models.stat_item import StatItem

# TODO update the JSON string below
json = "{}"
# create an instance of StatItem from a JSON string
stat_item_instance = StatItem.from_json(json)
# print the JSON string representation of the object
print(StatItem.to_json())

# convert the object into a dict
stat_item_dict = stat_item_instance.to_dict()
# create an instance of StatItem from a dict
stat_item_from_dict = StatItem.from_dict(stat_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


