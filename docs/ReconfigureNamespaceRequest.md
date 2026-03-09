# ReconfigureNamespaceRequest

Request to reconfigure a namespace's Qdrant collection schema.  This is a destructive operation: it deletes and recreates the Qdrant collection with merged vector definitions from all deployed plugins. Existing data is lost and must be re-ingested by triggering batches on each collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirm** | **bool** | Must be True to confirm this destructive operation. Existing Qdrant data will be deleted and must be re-ingested. | 

## Example

```python
from mixpeek.models.reconfigure_namespace_request import ReconfigureNamespaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigureNamespaceRequest from a JSON string
reconfigure_namespace_request_instance = ReconfigureNamespaceRequest.from_json(json)
# print the JSON string representation of the object
print(ReconfigureNamespaceRequest.to_json())

# convert the object into a dict
reconfigure_namespace_request_dict = reconfigure_namespace_request_instance.to_dict()
# create an instance of ReconfigureNamespaceRequest from a dict
reconfigure_namespace_request_from_dict = ReconfigureNamespaceRequest.from_dict(reconfigure_namespace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


