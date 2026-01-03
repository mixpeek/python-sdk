# OffsetPaginationParams

Offset-based pagination using page number sizing.  Best for: Traditional page UIs with page number navigation  How it works: - Uses page numbers (1, 2, 3...) and page size - Calculates offset as: (page_number - 1) * page_size - Simple and familiar for users - Can jump to any page directly  Tradeoffs: - Can have \"page drift\" if data changes between requests - Example: Items added/deleted causes duplicates or gaps - Less efficient for large offsets (database must skip N rows)  Use when: - Building traditional page-numbered UIs - Users need to jump to specific pages - Result set is relatively stable - Working with smaller datasets  Example: Page 1: {\"method\": \"offset\", \"page_size\": 25, \"page_number\": 1} Page 2: {\"method\": \"offset\", \"page_size\": 25, \"page_number\": 2}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**PaginationMethod**](PaginationMethod.md) | Constant identifying offset pagination (REQUIRED). | [optional] 
**page_size** | **int** | Number of documents per page (REQUIRED). Default: 10. | [optional] [default to 10]
**page_number** | **int** | 1-based page index to retrieve (REQUIRED). Default: 1. | [optional] [default to 1]

## Example

```python
from mixpeek.models.offset_pagination_params import OffsetPaginationParams

# TODO update the JSON string below
json = "{}"
# create an instance of OffsetPaginationParams from a JSON string
offset_pagination_params_instance = OffsetPaginationParams.from_json(json)
# print the JSON string representation of the object
print(OffsetPaginationParams.to_json())

# convert the object into a dict
offset_pagination_params_dict = offset_pagination_params_instance.to_dict()
# create an instance of OffsetPaginationParams from a dict
offset_pagination_params_from_dict = OffsetPaginationParams.from_dict(offset_pagination_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


