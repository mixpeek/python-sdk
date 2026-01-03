# CollectionOverviewResponse

Collection overview metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | 
**collection_name** | **str** |  | 
**total_documents** | **int** |  | 
**documents_last_24h** | **int** |  | 
**documents_last_7d** | **int** |  | 
**avg_processing_time_ms** | **float** |  | 
**success_rate** | **float** |  | 
**active_taxonomies** | **int** |  | 
**active_clusters** | **int** |  | 
**last_indexed** | **datetime** |  | [optional] 

## Example

```python
from mixpeek.models.collection_overview_response import CollectionOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionOverviewResponse from a JSON string
collection_overview_response_instance = CollectionOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(CollectionOverviewResponse.to_json())

# convert the object into a dict
collection_overview_response_dict = collection_overview_response_instance.to_dict()
# create an instance of CollectionOverviewResponse from a dict
collection_overview_response_from_dict = CollectionOverviewResponse.from_dict(collection_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


