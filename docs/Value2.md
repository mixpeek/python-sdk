# Value2

Pre-computed embedding vector. Accepts: (1) list[float] for single dense vectors, (2) list[list[float]] for multi-dense vectors (ColBERT token embeddings), (3) a template string (e.g., '{{INPUT.query}}') that resolves to either format. No inference is performed; the vector is used directly for similarity search.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from mixpeek.models.value2 import Value2

# TODO update the JSON string below
json = "{}"
# create an instance of Value2 from a JSON string
value2_instance = Value2.from_json(json)
# print the JSON string representation of the object
print(Value2.to_json())

# convert the object into a dict
value2_dict = value2_instance.to_dict()
# create an instance of Value2 from a dict
value2_from_dict = Value2.from_dict(value2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


