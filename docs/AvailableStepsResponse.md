# AvailableStepsResponse

Response containing all available steps for a taxonomy/collection.  This endpoint helps users discover what steps exist in their analytics data before querying transitions or paths.  Example Response:     ```json     {         \"taxonomy_id\": \"tax_sales_stages\",         \"collection_id\": \"col_emails\",         \"total_events\": 5432,         \"total_sequences\": 1000,         \"steps\": [             {                 \"step_key\": \"inquiry\",                 \"event_count\": 1000,                 \"sequence_count\": 1000,                 \"first_seen\": \"2025-11-01T00:00:00Z\",                 \"last_seen\": \"2025-12-07T00:00:00Z\"             },             {                 \"step_key\": \"followup\",                 \"event_count\": 450,                 \"sequence_count\": 450,                 \"first_seen\": \"2025-11-02T00:00:00Z\",                 \"last_seen\": \"2025-12-06T00:00:00Z\"             },             {                 \"step_key\": \"closed_won\",                 \"event_count\": 350,                 \"sequence_count\": 350,                 \"first_seen\": \"2025-11-05T00:00:00Z\",                 \"last_seen\": \"2025-12-07T00:00:00Z\"             }         ]     }     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_id** | **str** | Taxonomy ID | 
**collection_id** | **str** | Collection ID | 
**total_events** | **int** | Total events in dataset | 
**total_sequences** | **int** | Total unique sequences | 
**steps** | [**List[StepInfo]**](StepInfo.md) | Available steps sorted by count | 

## Example

```python
from mixpeek.models.available_steps_response import AvailableStepsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableStepsResponse from a JSON string
available_steps_response_instance = AvailableStepsResponse.from_json(json)
# print the JSON string representation of the object
print(AvailableStepsResponse.to_json())

# convert the object into a dict
available_steps_response_dict = available_steps_response_instance.to_dict()
# create an instance of AvailableStepsResponse from a dict
available_steps_response_from_dict = AvailableStepsResponse.from_dict(available_steps_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


