# InstantiateCollectionTemplateRequest

Request to instantiate a collection from a template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_name** | **str** | Name for the new collection | 
**bucket_ids** | **List[str]** | Bucket IDs to use for the collection (for bucket sources) | [optional] 
**collection_id** | **str** | Collection ID to use for the collection (for collection sources) | [optional] 
**description** | **str** | Optional description override for the collection | [optional] 
**tags** | **List[str]** | Optional tags for the collection | [optional] 

## Example

```python
from mixpeek.models.instantiate_collection_template_request import InstantiateCollectionTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstantiateCollectionTemplateRequest from a JSON string
instantiate_collection_template_request_instance = InstantiateCollectionTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(InstantiateCollectionTemplateRequest.to_json())

# convert the object into a dict
instantiate_collection_template_request_dict = instantiate_collection_template_request_instance.to_dict()
# create an instance of InstantiateCollectionTemplateRequest from a dict
instantiate_collection_template_request_from_dict = InstantiateCollectionTemplateRequest.from_dict(instantiate_collection_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


