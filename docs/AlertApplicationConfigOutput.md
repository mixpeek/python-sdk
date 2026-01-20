# AlertApplicationConfigOutput

Configuration for attaching an alert to a collection.  The key responsibility here is INPUT MAPPING: connecting document fields (or constants) to the retriever's expected inputs.  Note: Filtering logic (scroll_filters, min_score, etc.) belongs in the retriever, not here. The retriever owns all query semantics.  Use Cases:     - Attach safety alert to video upload collection     - Configure different field mappings for different collections     - Set execution priority for multiple alerts  Attributes:     alert_id: ID of the alert to execute     execution_mode: When this alert should execute     input_mappings: Map document fields or constants to retriever inputs     execution_phase: Which phase this alert runs in (default: ALERT)     priority: Priority within the execution phase (higher = runs first)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **str** | ID of the alert to execute | 
**execution_mode** | [**AlertExecutionMode**](AlertExecutionMode.md) | When this alert should execute | [optional] 
**input_mappings** | [**List[AlertInputMapping]**](AlertInputMapping.md) | Map document fields or constants to retriever input parameters | 
**execution_phase** | [**PostProcessingPhase**](PostProcessingPhase.md) | Which phase this alert runs in. Default: ALERT (phase 3, after taxonomies and clusters) | [optional] 
**priority** | **int** | Priority within the execution phase (higher &#x3D; runs first) | [optional] [default to 0]

## Example

```python
from mixpeek.models.alert_application_config_output import AlertApplicationConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AlertApplicationConfigOutput from a JSON string
alert_application_config_output_instance = AlertApplicationConfigOutput.from_json(json)
# print the JSON string representation of the object
print(AlertApplicationConfigOutput.to_json())

# convert the object into a dict
alert_application_config_output_dict = alert_application_config_output_instance.to_dict()
# create an instance of AlertApplicationConfigOutput from a dict
alert_application_config_output_from_dict = AlertApplicationConfigOutput.from_dict(alert_application_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


