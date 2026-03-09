# LifecycleStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | 
**lifecycle_state** | [**LifecycleState**](LifecycleState.md) |  | 
**s3_vector_index** | **str** |  | [optional] 
**qdrant_document_count** | **int** |  | [optional] 
**s3_vector_count** | **int** |  | [optional] 
**last_transitioned_at** | **datetime** |  | [optional] 
**task_id** | **str** |  | [optional] 
**warning** | **str** |  | [optional] 

## Example

```python
from mixpeek.models.lifecycle_status_response import LifecycleStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleStatusResponse from a JSON string
lifecycle_status_response_instance = LifecycleStatusResponse.from_json(json)
# print the JSON string representation of the object
print(LifecycleStatusResponse.to_json())

# convert the object into a dict
lifecycle_status_response_dict = lifecycle_status_response_instance.to_dict()
# create an instance of LifecycleStatusResponse from a dict
lifecycle_status_response_from_dict = LifecycleStatusResponse.from_dict(lifecycle_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


