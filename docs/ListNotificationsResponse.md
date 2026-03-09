# ListNotificationsResponse

Response model for listing notifications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Notification]**](Notification.md) | List of notifications | 
**pagination** | **Dict[str, object]** | Pagination information | 
**total** | **int** | Total number of notifications | 

## Example

```python
from mixpeek.models.list_notifications_response import ListNotificationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotificationsResponse from a JSON string
list_notifications_response_instance = ListNotificationsResponse.from_json(json)
# print the JSON string representation of the object
print(ListNotificationsResponse.to_json())

# convert the object into a dict
list_notifications_response_dict = list_notifications_response_instance.to_dict()
# create an instance of ListNotificationsResponse from a dict
list_notifications_response_from_dict = ListNotificationsResponse.from_dict(list_notifications_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


