# AlertInputMapping

Maps a retriever input to a document field or constant.  Input mappings define how to construct retriever inputs from the ingested document. This allows the same alert to be used with different collections that have different field structures.  Examples:     # Map document embedding to retriever query     {         \"input_key\": \"query_embedding\",         \"source\": {\"source_type\": \"document_field\", \"path\": \"features.video_embedding\"}     }      # Use constant collection for search target     {         \"input_key\": \"collection_id\",         \"source\": {\"source_type\": \"constant\", \"value\": \"col_known_incidents\"}     }  Attributes:     input_key: The retriever input parameter name     source: Where to get the value from

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_key** | **str** | The retriever input parameter name | 
**source** | [**InputMappingSource**](InputMappingSource.md) | Where to get the value from | 

## Example

```python
from mixpeek.models.alert_input_mapping import AlertInputMapping

# TODO update the JSON string below
json = "{}"
# create an instance of AlertInputMapping from a JSON string
alert_input_mapping_instance = AlertInputMapping.from_json(json)
# print the JSON string representation of the object
print(AlertInputMapping.to_json())

# convert the object into a dict
alert_input_mapping_dict = alert_input_mapping_instance.to_dict()
# create an instance of AlertInputMapping from a dict
alert_input_mapping_from_dict = AlertInputMapping.from_dict(alert_input_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


