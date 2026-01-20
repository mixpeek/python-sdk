# SharedTriggersModelsCreateTriggerRequest

Request to create a new trigger.  Examples:     Cluster trigger (cron):         {             \"action_type\": \"cluster\",             \"action_config\": {\"cluster_id\": \"clust_abc123\"},             \"trigger_type\": \"cron\",             \"schedule_config\": {\"cron_expression\": \"0 2 * * *\", \"timezone\": \"UTC\"},             \"description\": \"Daily clustering at 2am\"         }      Taxonomy trigger (interval):         {             \"action_type\": \"taxonomy_enrichment\",             \"action_config\": {\"taxonomy_id\": \"tax_products\", \"collection_id\": \"col_inv\"},             \"trigger_type\": \"interval\",             \"schedule_config\": {\"interval_seconds\": 21600},             \"description\": \"Re-enrich every 6 hours\"         }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**TriggerActionType**](TriggerActionType.md) | Type of action to execute | 
**action_config** | **object** | Action-specific configuration | 
**trigger_type** | [**SharedTriggersModelsTriggerType**](SharedTriggersModelsTriggerType.md) | Type of schedule | 
**schedule_config** | **object** | Schedule-specific configuration | 
**description** | **str** | Human-readable description | [optional] 
**status** | [**SharedTriggersModelsTriggerStatus**](SharedTriggersModelsTriggerStatus.md) | Initial status (active or paused) | [optional] 

## Example

```python
from mixpeek.models.shared_triggers_models_create_trigger_request import SharedTriggersModelsCreateTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SharedTriggersModelsCreateTriggerRequest from a JSON string
shared_triggers_models_create_trigger_request_instance = SharedTriggersModelsCreateTriggerRequest.from_json(json)
# print the JSON string representation of the object
print(SharedTriggersModelsCreateTriggerRequest.to_json())

# convert the object into a dict
shared_triggers_models_create_trigger_request_dict = shared_triggers_models_create_trigger_request_instance.to_dict()
# create an instance of SharedTriggersModelsCreateTriggerRequest from a dict
shared_triggers_models_create_trigger_request_from_dict = SharedTriggersModelsCreateTriggerRequest.from_dict(shared_triggers_models_create_trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


