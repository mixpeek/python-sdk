# CollectionScheduleConfig

Schedule configuration for automatic collection re-processing.  Attaches a cron or interval schedule to a collection, which creates a COLLECTION_TRIGGER trigger behind the scenes. This is a DX convenience so users don't need to create triggers manually.  Examples:     Daily re-crawl at 2am UTC:         {\"trigger_type\": \"cron\", \"schedule_config\": {\"cron_expression\": \"0 2 * * *\"}}      Every 6 hours:         {\"trigger_type\": \"interval\", \"schedule_config\": {\"interval_seconds\": 21600}}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_type** | **str** | Schedule type: &#39;cron&#39; or &#39;interval&#39; | 
**schedule_config** | **Dict[str, object]** | Schedule configuration. For cron: {cron_expression, timezone}. For interval: {interval_seconds, start_immediately}. | 
**description** | **str** | Human-readable description of the schedule. | [optional] 

## Example

```python
from mixpeek.models.collection_schedule_config import CollectionScheduleConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionScheduleConfig from a JSON string
collection_schedule_config_instance = CollectionScheduleConfig.from_json(json)
# print the JSON string representation of the object
print(CollectionScheduleConfig.to_json())

# convert the object into a dict
collection_schedule_config_dict = collection_schedule_config_instance.to_dict()
# create an instance of CollectionScheduleConfig from a dict
collection_schedule_config_from_dict = CollectionScheduleConfig.from_dict(collection_schedule_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


