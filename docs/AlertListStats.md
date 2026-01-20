# AlertListStats

Aggregate statistics for a list of alerts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_alerts** | **int** | Total number of alerts | [optional] [default to 0]
**enabled_alerts** | **int** | Number of enabled alerts | [optional] [default to 0]
**disabled_alerts** | **int** | Number of disabled alerts | [optional] [default to 0]
**alerts_by_channel_type** | **Dict[str, int]** | Count of alerts by notification channel type | [optional] 

## Example

```python
from mixpeek.models.alert_list_stats import AlertListStats

# TODO update the JSON string below
json = "{}"
# create an instance of AlertListStats from a JSON string
alert_list_stats_instance = AlertListStats.from_json(json)
# print the JSON string representation of the object
print(AlertListStats.to_json())

# convert the object into a dict
alert_list_stats_dict = alert_list_stats_instance.to_dict()
# create an instance of AlertListStats from a dict
alert_list_stats_from_dict = AlertListStats.from_dict(alert_list_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


