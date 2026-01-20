# InteractionWeights

Custom weights for different interaction types when computing metrics.  Higher weights indicate more importance. Purchases typically have higher weight than clicks because they're a stronger signal of user intent.  Example: {\"click\": 1.0, \"purchase\": 5.0, \"add_to_cart\": 2.0, \"bookmark\": 1.5}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weights** | **Dict[str, float]** | Mapping of interaction_type -&gt; weight (higher &#x3D; more important). | [optional] 

## Example

```python
from mixpeek.models.interaction_weights import InteractionWeights

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionWeights from a JSON string
interaction_weights_instance = InteractionWeights.from_json(json)
# print the JSON string representation of the object
print(InteractionWeights.to_json())

# convert the object into a dict
interaction_weights_dict = interaction_weights_instance.to_dict()
# create an instance of InteractionWeights from a dict
interaction_weights_from_dict = InteractionWeights.from_dict(interaction_weights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


