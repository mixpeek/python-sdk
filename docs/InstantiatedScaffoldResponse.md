# InstantiatedScaffoldResponse

Response after successful scaffold instantiation.  Contains IDs and names of all four created resources. Use these IDs for subsequent operations: - Upload data: POST /v1/buckets/{bucket_id}/objects - Process: POST /v1/collections/{collection_id}/batches - Search: POST /v1/retrievers/{retriever_id}/retrieve

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_id** | **str** | Created namespace ID (ns_xxx) | 
**namespace_name** | **str** | Created namespace name | 
**bucket_id** | **str** | Created bucket ID (bkt_xxx) | 
**bucket_name** | **str** | Created bucket name | 
**collection_id** | **str** | Created collection ID (col_xxx) | 
**collection_name** | **str** | Created collection name | 
**retriever_id** | **str** | Created retriever ID (ret_xxx) | 
**retriever_name** | **str** | Created retriever name | 
**template_id** | **str** | Scaffold template ID used | 
**status** | **str** | Status: &#39;created&#39; on success | [optional] [default to 'created']
**created_at** | **datetime** | UTC timestamp of creation | [optional] 

## Example

```python
from mixpeek.models.instantiated_scaffold_response import InstantiatedScaffoldResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstantiatedScaffoldResponse from a JSON string
instantiated_scaffold_response_instance = InstantiatedScaffoldResponse.from_json(json)
# print the JSON string representation of the object
print(InstantiatedScaffoldResponse.to_json())

# convert the object into a dict
instantiated_scaffold_response_dict = instantiated_scaffold_response_instance.to_dict()
# create an instance of InstantiatedScaffoldResponse from a dict
instantiated_scaffold_response_from_dict = InstantiatedScaffoldResponse.from_dict(instantiated_scaffold_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


