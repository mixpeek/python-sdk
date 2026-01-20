# FacetFieldConfig

Configuration for a single facet field.  Faceting counts unique values for a field, enabling faceted search interfaces (e.g., \"Show 45 results in 'Sports', 23 in 'Music'\").  ┌─────────────────────────────────────────────────────────────────────────────┐ │ IMPORTANT: INDEX REQUIREMENT                                                │ │                                                                             │ │ The field MUST have a keyword index in Qdrant for faceting to work.         │ │ Fields are automatically indexed during collection creation for common      │ │ metadata fields. For custom fields, ensure indexing is configured.          │ │                                                                             │ │ Without an index, faceting will fail with an error.                         │ └─────────────────────────────────────────────────────────────────────────────┘  Example:     ```json     {         \"key\": \"metadata.category\",         \"limit\": 10,         \"exact\": false     }     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | REQUIRED. Field path to facet on (e.g., &#39;metadata.category&#39;, &#39;status&#39;). Supports nested fields using dot notation. The field MUST have a keyword index in Qdrant - faceting will fail without it. Common indexed fields: metadata.*, status, collection_id, source_object_id. | 
**limit** | **int** | OPTIONAL. Maximum number of unique values to return (default: 10). Results are sorted by count descending, then by value ascending. Higher limits increase response size but provide more comprehensive facets. Common values: 5 (compact), 10 (standard), 20-50 (detailed). | [optional] [default to 10]
**exact** | **bool** | OPTIONAL. Use exact counts instead of approximate (default: False). - False (default): Fast approximate counts, suitable for most UIs.   Approximate counts are accurate enough for display purposes. - True: Slower but precise counts, useful for debugging or analytics.   Use when exact numbers matter (e.g., reports, dashboards). | [optional] [default to False]

## Example

```python
from mixpeek.models.facet_field_config import FacetFieldConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FacetFieldConfig from a JSON string
facet_field_config_instance = FacetFieldConfig.from_json(json)
# print the JSON string representation of the object
print(FacetFieldConfig.to_json())

# convert the object into a dict
facet_field_config_dict = facet_field_config_instance.to_dict()
# create an instance of FacetFieldConfig from a dict
facet_field_config_from_dict = FacetFieldConfig.from_dict(facet_field_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


