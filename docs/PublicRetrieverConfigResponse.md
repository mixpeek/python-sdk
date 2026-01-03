# PublicRetrieverConfigResponse

Response for fetching public retriever configuration (for UI rendering).  This is what the public frontend (apps.mixpeek.com) fetches to render the search interface. It includes everything needed for UI rendering.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_name** | **str** | Public name of the retriever | 
**public_api_key** | **str** | Public API key for making authenticated requests. Frontend needs this to call the execute endpoint. | 
**display_config** | [**DisplayConfigOutput**](DisplayConfigOutput.md) | Display configuration for rendering the UI. Includes inputs, theme, layout, and exposed fields. | 
**password_protected** | **bool** | Whether this retriever requires password authentication | 
**retriever_metadata** | [**RetrieverMetadata**](RetrieverMetadata.md) | OPTIONAL. Technical metadata about how the retriever works. Only present if include_metadata&#x3D;True was set during publishing. | [optional] 

## Example

```python
from mixpeek.models.public_retriever_config_response import PublicRetrieverConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicRetrieverConfigResponse from a JSON string
public_retriever_config_response_instance = PublicRetrieverConfigResponse.from_json(json)
# print the JSON string representation of the object
print(PublicRetrieverConfigResponse.to_json())

# convert the object into a dict
public_retriever_config_response_dict = public_retriever_config_response_instance.to_dict()
# create an instance of PublicRetrieverConfigResponse from a dict
public_retriever_config_response_from_dict = PublicRetrieverConfigResponse.from_dict(public_retriever_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


