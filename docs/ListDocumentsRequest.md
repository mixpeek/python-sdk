# ListDocumentsRequest

Request model for listing documents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Filters to apply. | [optional] 
**sort** | [**SortOption**](SortOption.md) | Sort options. | [optional] 
**search** | **str** | Search term. | [optional] 
**return_url** | **bool** | Whether to return presigned URLs for object keys. | [optional] [default to False]
**return_vectors** | **bool** | Whether to return vector embeddings in the document results. | [optional] [default to False]

## Example

```python
from mixpeek.models.list_documents_request import ListDocumentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListDocumentsRequest from a JSON string
list_documents_request_instance = ListDocumentsRequest.from_json(json)
# print the JSON string representation of the object
print(ListDocumentsRequest.to_json())

# convert the object into a dict
list_documents_request_dict = list_documents_request_instance.to_dict()
# create an instance of ListDocumentsRequest from a dict
list_documents_request_from_dict = ListDocumentsRequest.from_dict(list_documents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


