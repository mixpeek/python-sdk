# AvailableOrgPluginsResponse

Response listing org-level plugins available to enable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**plugins** | [**List[AvailableOrgPluginItem]**](AvailableOrgPluginItem.md) | List of available org-level plugins | 
**total** | **int** | Total number of plugins | 
**organization_id** | **str** | Organization ID | 
**namespace_id** | **str** | Namespace ID | 

## Example

```python
from mixpeek.models.available_org_plugins_response import AvailableOrgPluginsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableOrgPluginsResponse from a JSON string
available_org_plugins_response_instance = AvailableOrgPluginsResponse.from_json(json)
# print the JSON string representation of the object
print(AvailableOrgPluginsResponse.to_json())

# convert the object into a dict
available_org_plugins_response_dict = available_org_plugins_response_instance.to_dict()
# create an instance of AvailableOrgPluginsResponse from a dict
available_org_plugins_response_from_dict = AvailableOrgPluginsResponse.from_dict(available_org_plugins_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


