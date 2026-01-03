# ListToolsResponse

Response for listing available agent tools.  Use this endpoint to discover available tools before creating a session. Pass tool names to available_tools in AgentConfig when creating a session.  Attributes:     results: List of available tools with descriptions     total: Total number of tools available     categories: Unique tool categories  Example:     ```python     response = ListToolsResponse(         results=[             ToolInfo(name=\"smart_search\", description=\"...\", category=\"search\"),             ToolInfo(name=\"list_collections\", description=\"...\", category=\"read\"),         ],         total=25,         categories=[\"search\", \"read\", \"create\"]     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ToolInfo]**](ToolInfo.md) | Available tools | 
**total** | **int** | Total number of tools | 
**categories** | **List[str]** | Unique tool categories | 

## Example

```python
from mixpeek.models.list_tools_response import ListToolsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListToolsResponse from a JSON string
list_tools_response_instance = ListToolsResponse.from_json(json)
# print the JSON string representation of the object
print(ListToolsResponse.to_json())

# convert the object into a dict
list_tools_response_dict = list_tools_response_instance.to_dict()
# create an instance of ListToolsResponse from a dict
list_tools_response_from_dict = ListToolsResponse.from_dict(list_tools_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


