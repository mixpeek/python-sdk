# SourceFiltersInput

Filters applied to source data when processing collections.  Source filters determine which objects (from buckets) or documents (from collections) are processed by this collection. Filters use the same LogicalOperator model as list APIs throughout the system, supporting complex AND/OR/NOT logic.  Use Cases:     - Process only specific content types from mixed-content buckets     - Filter by metadata fields (status, category, tags, dates)     - Create specialized collections from broader sources     - Exclude certain objects or documents from processing  Examples:     Process only video content:         {             \"AND\": [                 {\"field\": \"blobs.type\", \"operator\": \"eq\", \"value\": \"video\"}             ]         }      Process only active, published content:         {             \"AND\": [                 {\"field\": \"metadata.status\", \"operator\": \"eq\", \"value\": \"active\"},                 {\"field\": \"metadata.published\", \"operator\": \"eq\", \"value\": true}             ]         }      Process content from last 30 days:         {             \"AND\": [                 {\"field\": \"created_at\", \"operator\": \"gte\", \"value\": \"2025-10-08T00:00:00Z\"}             ]         }      Process specific brands OR categories:         {             \"OR\": [                 {\"field\": \"brand_name\", \"operator\": \"in\", \"value\": [\"Acme\", \"TechCo\"]},                 {\"field\": \"category\", \"operator\": \"eq\", \"value\": \"premium\"}             ]         }  Filter Operators:     - eq (equals)     - ne (not equals)     - gt (greater than)     - gte (greater than or equal)     - lt (less than)     - lte (less than or equal)     - in (value in list)     - nin (value not in list)     - contains (string contains)     - starts_with (string starts with)     - ends_with (string ends with)  Performance Considerations:     - Filters are evaluated at batch creation time     - Only matching objects/documents are included in processing     - More selective filters = smaller batches = faster processing     - Use indexed fields (metadata, timestamps) for better performance  Relationship to Batch Filters:     - Source filters: Applied at collection definition (consistent across all batches)     - Batch filters: Applied at batch creation (ad-hoc, per-batch basis)     - Both can be used together: source filters + batch filters = intersection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Optional logical filters to apply to source data. Uses LogicalOperator model with AND/OR/NOT support. When specified, only objects/documents matching these filters will be processed by this collection. When null, all source data is processed (no filtering). Filters are consistent across all batch runs for this collection. | [optional] 

## Example

```python
from mixpeek.models.source_filters_input import SourceFiltersInput

# TODO update the JSON string below
json = "{}"
# create an instance of SourceFiltersInput from a JSON string
source_filters_input_instance = SourceFiltersInput.from_json(json)
# print the JSON string representation of the object
print(SourceFiltersInput.to_json())

# convert the object into a dict
source_filters_input_dict = source_filters_input_instance.to_dict()
# create an instance of SourceFiltersInput from a dict
source_filters_input_from_dict = SourceFiltersInput.from_dict(source_filters_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


