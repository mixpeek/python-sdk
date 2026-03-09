# DiscoveryResponse

Combined discovery response with all available resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractors** | [**List[ExtractorDiscovery]**](ExtractorDiscovery.md) | Available feature extractors | [optional] 
**stages** | [**List[StageDiscovery]**](StageDiscovery.md) | Available retriever stages | [optional] 
**manifest_schema** | [**ManifestSchemaDiscovery**](ManifestSchemaDiscovery.md) | Manifest schema information | [optional] 

## Example

```python
from mixpeek.models.discovery_response import DiscoveryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryResponse from a JSON string
discovery_response_instance = DiscoveryResponse.from_json(json)
# print the JSON string representation of the object
print(DiscoveryResponse.to_json())

# convert the object into a dict
discovery_response_dict = discovery_response_instance.to_dict()
# create an instance of DiscoveryResponse from a dict
discovery_response_from_dict = DiscoveryResponse.from_dict(discovery_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


