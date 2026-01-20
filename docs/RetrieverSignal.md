# RetrieverSignal

Single retriever signal event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Event timestamp | 
**execution_id** | **str** | Execution identifier | 
**signal_type** | **str** | Type of signal | 
**signal_data** | **object** | Signal-specific data | 
**metadata** | **object** | Additional metadata | [optional] 

## Example

```python
from mixpeek.models.retriever_signal import RetrieverSignal

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverSignal from a JSON string
retriever_signal_instance = RetrieverSignal.from_json(json)
# print the JSON string representation of the object
print(RetrieverSignal.to_json())

# convert the object into a dict
retriever_signal_dict = retriever_signal_instance.to_dict()
# create an instance of RetrieverSignal from a dict
retriever_signal_from_dict = RetrieverSignal.from_dict(retriever_signal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


