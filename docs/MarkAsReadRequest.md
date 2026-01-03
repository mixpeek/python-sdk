# MarkAsReadRequest

Request model for marking notifications as read.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User ID to mark all as read for | [optional] 

## Example

```python
from mixpeek.models.mark_as_read_request import MarkAsReadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MarkAsReadRequest from a JSON string
mark_as_read_request_instance = MarkAsReadRequest.from_json(json)
# print the JSON string representation of the object
print(MarkAsReadRequest.to_json())

# convert the object into a dict
mark_as_read_request_dict = mark_as_read_request_instance.to_dict()
# create an instance of MarkAsReadRequest from a dict
mark_as_read_request_from_dict = MarkAsReadRequest.from_dict(mark_as_read_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


