# EnrichmentField

Field-level enrichment behaviour specification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_path** | **str** | Dot-notation path of the field to copy from the taxonomy node. | 
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


