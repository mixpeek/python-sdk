# ResourceScopeInput

Fine-grained restriction applied to an API key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | [**ResourceTypeInput**](ResourceTypeInput.md) | Resource type this scope governs. Use ResourceType enum values to scope a key to namespaces, collections, clusters, etc. | 
**resource_id** | **str** | Identifier or pattern for the resource. Accepts a literal ID (e.g. &#39;ns_production&#39;) or wildcard forms such as &#39;*&#39; or &#39;ns_customer_*&#39;. | 
**operations** | [**List[NamespaceOperation]**](NamespaceOperation.md) | Subset of operations allowed within the scope. When omitted the key may perform any operation permitted by its Permission list. | [optional] 

## Example

```python
from mixpeek.models.resource_scope_input import ResourceScopeInput

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceScopeInput from a JSON string
resource_scope_input_instance = ResourceScopeInput.from_json(json)
# print the JSON string representation of the object
print(ResourceScopeInput.to_json())

# convert the object into a dict
resource_scope_input_dict = resource_scope_input_instance.to_dict()
# create an instance of ResourceScopeInput from a dict
resource_scope_input_from_dict = ResourceScopeInput.from_dict(resource_scope_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


