# CloneNamespaceResponse

Response after initiating namespace clone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | [**NamespaceModel**](NamespaceModel.md) | Cloned namespace with new namespace_id | 
**source_namespace_id** | **str** | Source namespace that was cloned | 
**status** | **str** | Clone status: &#39;cloning&#39;, &#39;ready&#39;, or &#39;failed&#39; | [optional] [default to 'cloning']
**task_id** | **str** | Celery task ID for tracking clone progress | [optional] 
**cloned_resources** | [**ClonedResourceSummary**](ClonedResourceSummary.md) | Summary of cloned resources (present when ready) | [optional] 

## Example

```python
from mixpeek.models.clone_namespace_response import CloneNamespaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloneNamespaceResponse from a JSON string
clone_namespace_response_instance = CloneNamespaceResponse.from_json(json)
# print the JSON string representation of the object
print(CloneNamespaceResponse.to_json())

# convert the object into a dict
clone_namespace_response_dict = clone_namespace_response_instance.to_dict()
# create an instance of CloneNamespaceResponse from a dict
clone_namespace_response_from_dict = CloneNamespaceResponse.from_dict(clone_namespace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


