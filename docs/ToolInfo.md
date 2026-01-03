# ToolInfo

Information about an available agent tool.  Attributes:     name: Tool name (use this in available_tools)     description: What the tool does     category: Tool category (search, read, create, etc.)     parameters: Parameter definitions     required_params: List of required parameter names

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Tool name | 
**description** | **str** | Tool description | 
**category** | **str** | Tool category | 
**parameters** | **Dict[str, object]** | Parameter definitions | [optional] 
**required_params** | **List[str]** | Required parameters | [optional] 

## Example

```python
from mixpeek.models.tool_info import ToolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ToolInfo from a JSON string
tool_info_instance = ToolInfo.from_json(json)
# print the JSON string representation of the object
print(ToolInfo.to_json())

# convert the object into a dict
tool_info_dict = tool_info_instance.to_dict()
# create an instance of ToolInfo from a dict
tool_info_from_dict = ToolInfo.from_dict(tool_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


