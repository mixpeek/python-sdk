# JoinStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processed_docs** | **int** |  | [optional] [default to 0]
**batches** | **int** |  | [optional] [default to 0]
**errors** | **int** |  | [optional] [default to 0]

## Example

```python
from mixpeek.models.join_stats import JoinStats

# TODO update the JSON string below
json = "{}"
# create an instance of JoinStats from a JSON string
join_stats_instance = JoinStats.from_json(json)
# print the JSON string representation of the object
print(JoinStats.to_json())

# convert the object into a dict
join_stats_dict = join_stats_instance.to_dict()
# create an instance of JoinStats from a dict
join_stats_from_dict = JoinStats.from_dict(join_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


