# StageDefsGroupByFieldConfig

Configuration for grouping documents before aggregation.  When specified, aggregations are computed per-group rather than across all documents.  Example:     Group by category and count:         ```json         {\"field\": \"metadata.category\", \"alias\": \"category\"}         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | REQUIRED. Field path to group by (dot notation supported). Documents with the same value for this field are grouped together. Examples: &#39;metadata.category&#39;, &#39;collection_id&#39;, &#39;metadata.file_type&#39;. | 
**alias** | **str** | OPTIONAL. Alias for this group-by field in the output. Defaults to the field name (last segment after dot). Example: &#39;category&#39; for field &#39;metadata.category&#39;. | [optional] 

## Example

```python
from mixpeek.models.stage_defs_group_by_field_config import StageDefsGroupByFieldConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StageDefsGroupByFieldConfig from a JSON string
stage_defs_group_by_field_config_instance = StageDefsGroupByFieldConfig.from_json(json)
# print the JSON string representation of the object
print(StageDefsGroupByFieldConfig.to_json())

# convert the object into a dict
stage_defs_group_by_field_config_dict = stage_defs_group_by_field_config_instance.to_dict()
# create an instance of StageDefsGroupByFieldConfig from a dict
stage_defs_group_by_field_config_from_dict = StageDefsGroupByFieldConfig.from_dict(stage_defs_group_by_field_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


