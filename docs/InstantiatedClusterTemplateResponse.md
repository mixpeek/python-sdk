# InstantiatedClusterTemplateResponse

Response after instantiating a cluster template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | ID of the created cluster | 
**cluster_name** | **str** | Name of the created cluster | 
**template_id** | **str** | ID of the template used | 
**status** | **str** | Status of the instantiation | [optional] [default to 'created']
**created_at** | **datetime** | Timestamp when cluster was created | [optional] 

## Example

```python
from mixpeek.models.instantiated_cluster_template_response import InstantiatedClusterTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstantiatedClusterTemplateResponse from a JSON string
instantiated_cluster_template_response_instance = InstantiatedClusterTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(InstantiatedClusterTemplateResponse.to_json())

# convert the object into a dict
instantiated_cluster_template_response_dict = instantiated_cluster_template_response_instance.to_dict()
# create an instance of InstantiatedClusterTemplateResponse from a dict
instantiated_cluster_template_response_from_dict = InstantiatedClusterTemplateResponse.from_dict(instantiated_cluster_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


