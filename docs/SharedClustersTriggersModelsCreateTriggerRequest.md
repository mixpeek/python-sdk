# SharedClustersTriggersModelsCreateTriggerRequest

Request to create a new cluster trigger.  Creates an automated trigger that executes clustering based on schedules, events, or conditions.  Requirements:     - trigger_type: REQUIRED - Determines which schedule_config fields are needed     - schedule_config: REQUIRED - Configuration specific to trigger_type     - execution_config OR cluster_id: REQUIRED - Either provide config directly or reference existing cluster  Trigger Types and schedule_config:     - **cron**: Requires {\"cron_expression\": str, \"timezone\": str}     - **interval**: Requires {\"interval_seconds\": int, \"start_immediately\": bool}     - **event**: Requires {\"event_type\": str, \"event_threshold\": int, \"collection_id\": str, \"cooldown_seconds\": int}     - **conditional**: Requires {\"condition_type\": str, \"threshold\": float, \"metric\": str, \"check_interval_seconds\": int}  Use Cases:     - Scheduled maintenance: Use cron or interval triggers     - Reactive clustering: Use event triggers to cluster when data changes     - Intelligent clustering: Use conditional triggers based on metrics  Examples:     Cron trigger (daily at 2am UTC):         {             \"trigger_type\": \"cron\",             \"schedule_config\": {                 \"cron_expression\": \"0 2 * * *\",                 \"timezone\": \"UTC\"             },             \"execution_config\": {                 \"collection_ids\": [\"col_abc123\"],                 \"config\": {                     \"algorithm\": \"kmeans\",                     \"n_clusters\": 5                 }             },             \"description\": \"Daily clustering at 2am\"         }      Interval trigger (every 6 hours):         {             \"trigger_type\": \"interval\",             \"schedule_config\": {                 \"interval_seconds\": 21600,                 \"start_immediately\": false             },             \"execution_config\": {                 \"collection_ids\": [\"col_products\"],                 \"config\": {                     \"algorithm\": \"hdbscan\",                     \"min_cluster_size\": 10                 }             },             \"description\": \"Cluster every 6 hours\"         }      Event trigger (after 100 documents added):         {             \"trigger_type\": \"event\",             \"schedule_config\": {                 \"event_type\": \"documents_added\",                 \"event_threshold\": 100,                 \"collection_id\": \"col_abc123\",                 \"cooldown_seconds\": 300             },             \"execution_config\": {                 \"collection_ids\": [\"col_abc123\"],                 \"config\": {                     \"algorithm\": \"kmeans\",                     \"n_clusters\": 3                 }             },             \"description\": \"Cluster after 100 new documents\"         }      Conditional trigger (when drift exceeds 30%):         {             \"trigger_type\": \"conditional\",             \"schedule_config\": {                 \"condition_type\": \"drift\",                 \"threshold\": 0.3,                 \"metric\": \"cosine_drift\",                 \"check_interval_seconds\": 3600             },             \"execution_config\": {                 \"collection_ids\": [\"col_abc123\"],                 \"config\": {                     \"algorithm\": \"hdbscan\",                     \"min_cluster_size\": 5                 }             },             \"description\": \"Re-cluster when drift > 30%\"         }      Using existing cluster definition:         {             \"trigger_type\": \"interval\",             \"schedule_config\": {                 \"interval_seconds\": 3600,                 \"start_immediately\": true             },             \"cluster_id\": \"cluster_xyz789\",             \"description\": \"Hourly clustering using cluster_xyz789\"         }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | OPTIONAL. Reference to existing cluster definition. If provided, execution_config is inherited from the cluster. Either cluster_id OR execution_config must be provided. | [optional] 
**execution_config** | [**TriggerExecutionConfig**](TriggerExecutionConfig.md) | OPTIONAL. Clustering configuration for this trigger. Specifies collections and algorithm to use when trigger fires. Required if cluster_id is not provided. | [optional] 
**trigger_type** | [**SharedClustersTriggersModelsTriggerType**](SharedClustersTriggersModelsTriggerType.md) | REQUIRED. Type of trigger to create. Determines which schedule_config fields are required. Options: &#39;cron&#39;, &#39;interval&#39;, &#39;event&#39;, &#39;conditional&#39;. | 
**schedule_config** | **Dict[str, object]** | REQUIRED. Type-specific schedule configuration. Contents depend on trigger_type. See trigger type examples above for required fields. | 
**description** | **str** | OPTIONAL. Human-readable description of what this trigger does. Helpful for identifying triggers in dashboards. | [optional] 
**status** | [**SharedClustersTriggersModelsTriggerStatus**](SharedClustersTriggersModelsTriggerStatus.md) | OPTIONAL. Initial status of trigger. Defaults to &#39;active&#39; (enabled). Can be set to &#39;paused&#39; to create disabled trigger. | [optional] 

## Example

```python
from mixpeek.models.shared_clusters_triggers_models_create_trigger_request import SharedClustersTriggersModelsCreateTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SharedClustersTriggersModelsCreateTriggerRequest from a JSON string
shared_clusters_triggers_models_create_trigger_request_instance = SharedClustersTriggersModelsCreateTriggerRequest.from_json(json)
# print the JSON string representation of the object
print(SharedClustersTriggersModelsCreateTriggerRequest.to_json())

# convert the object into a dict
shared_clusters_triggers_models_create_trigger_request_dict = shared_clusters_triggers_models_create_trigger_request_instance.to_dict()
# create an instance of SharedClustersTriggersModelsCreateTriggerRequest from a dict
shared_clusters_triggers_models_create_trigger_request_from_dict = SharedClustersTriggersModelsCreateTriggerRequest.from_dict(shared_clusters_triggers_models_create_trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


