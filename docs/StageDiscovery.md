# StageDiscovery

Extended stage discovery information with examples.  Includes everything from RetrieverStageDefinition plus usage examples and common patterns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage_id** | **str** | Unique identifier for the stage | 
**description** | **str** | Human-readable description of stage behavior | 
**category** | **str** | Transformation category: filter, sort, reduce, apply, enrich | 
**icon** | **str** | Lucide React icon identifier | 
**parameter_schema** | **Dict[str, object]** | JSON Schema for stage parameters | [optional] 
**example_config** | **Dict[str, object]** | Example stage configuration | [optional] 
**common_use_cases** | **List[str]** | Common scenarios where this stage is useful | [optional] 
**cost_tier** | **str** | Relative cost tier: cheap, moderate, expensive | [optional] [default to 'moderate']
**requires_collections** | **bool** | Whether this stage requires collection access | [optional] [default to True]

## Example

```python
from mixpeek.models.stage_discovery import StageDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of StageDiscovery from a JSON string
stage_discovery_instance = StageDiscovery.from_json(json)
# print the JSON string representation of the object
print(StageDiscovery.to_json())

# convert the object into a dict
stage_discovery_dict = stage_discovery_instance.to_dict()
# create an instance of StageDiscovery from a dict
stage_discovery_from_dict = StageDiscovery.from_dict(stage_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


