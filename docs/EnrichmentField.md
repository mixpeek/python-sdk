# EnrichmentField

Field-level enrichment behaviour specification.  Defines how to copy fields from taxonomy source nodes to enriched documents. Supports field renaming via target_field parameter.  Examples:     - Copy field as-is: {\"field_path\": \"category\", \"merge_mode\": \"replace\"}     - Rename field: {\"field_path\": \"label\", \"target_field\": \"visual_style\", \"merge_mode\": \"replace\"}     - Append to array: {\"field_path\": \"tags\", \"merge_mode\": \"append\"}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_path** | **str** | Dot-notation path of the field to copy from the taxonomy node. | 
**target_field** | **str** | Optional target field name in the enriched document. If specified, the source field will be renamed to this name. If not specified, the field_path is used as the target name. Use this to rename fields during enrichment (e.g., label → visual_style). | [optional] 
**merge_mode** | [**EnrichmentMergeMode**](EnrichmentMergeMode.md) | Whether to overwrite the target&#39;s value or append (for arrays). | [optional] 

## Example

```python
from mixpeek.models.enrichment_field import EnrichmentField

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichmentField from a JSON string
enrichment_field_instance = EnrichmentField.from_json(json)
# print the JSON string representation of the object
print(EnrichmentField.to_json())

# convert the object into a dict
enrichment_field_dict = enrichment_field_instance.to_dict()
# create an instance of EnrichmentField from a dict
enrichment_field_from_dict = EnrichmentField.from_dict(enrichment_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


