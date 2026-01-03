# GroupByField

Configuration for grouping by a field.  Defines how to group data by a specific field, with optional transformations.  Requirements:     - field: REQUIRED, the field to group by     - alias: OPTIONAL, name for the grouped field in results     - date_trunc: OPTIONAL, truncate date fields to time periods     - date_part: OPTIONAL, extract part of date field  Examples:     - Simple grouping: GroupByField(field=\"metadata.category\")     - Daily grouping: GroupByField(field=\"created_at\", date_trunc=DateTruncUnit.DAY)     - Hour of day: GroupByField(field=\"created_at\", date_part=DatePartUnit.HOUR)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The field path to group by. Supports dot notation for nested fields (e.g., &#39;metadata.category&#39;). For date fields, can be combined with date_trunc or date_part. | 
**alias** | **str** | Optional alias for the grouped field in results. If not provided, uses the field name. Useful for nested fields to create simpler result names. | [optional] 
**date_trunc** | [**DateTruncUnit**](DateTruncUnit.md) | Truncate date field to specified unit. REQUIRED when grouping by date/time periods. Only valid for date/datetime fields. Cannot be used with date_part. | [optional] 
**date_part** | [**DatePartUnit**](DatePartUnit.md) | Extract specific part from date field. OPTIONAL for analyzing date patterns. Only valid for date/datetime fields. Cannot be used with date_trunc. | [optional] 

## Example

```python
from mixpeek.models.group_by_field import GroupByField

# TODO update the JSON string below
json = "{}"
# create an instance of GroupByField from a JSON string
group_by_field_instance = GroupByField.from_json(json)
# print the JSON string representation of the object
print(GroupByField.to_json())

# convert the object into a dict
group_by_field_dict = group_by_field_instance.to_dict()
# create an instance of GroupByField from a dict
group_by_field_from_dict = GroupByField.from_dict(group_by_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


