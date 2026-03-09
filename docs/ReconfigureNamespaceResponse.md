# ReconfigureNamespaceResponse

Response from reconfiguring a namespace's Qdrant collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_id** | **str** | The reconfigured namespace | 
**status** | **str** | Operation status: &#39;reconfigured&#39; or &#39;no_changes_needed&#39; | 
**previous_points_count** | **int** | Number of Qdrant points that were in the collection before reconfigure | 
**vectors_added** | **List[str]** | Names of new vector indexes added to the schema | 
**vectors_total** | **List[str]** | All vector index names in the reconfigured collection | 
**collections_to_reprocess** | **List[str]** | Collection IDs that need to be re-triggered to populate new vectors | 
**message** | **str** | Human-readable status message | 

## Example

```python
from mixpeek.models.reconfigure_namespace_response import ReconfigureNamespaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigureNamespaceResponse from a JSON string
reconfigure_namespace_response_instance = ReconfigureNamespaceResponse.from_json(json)
# print the JSON string representation of the object
print(ReconfigureNamespaceResponse.to_json())

# convert the object into a dict
reconfigure_namespace_response_dict = reconfigure_namespace_response_instance.to_dict()
# create an instance of ReconfigureNamespaceResponse from a dict
reconfigure_namespace_response_from_dict = ReconfigureNamespaceResponse.from_dict(reconfigure_namespace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


