# AttributeBasedConfig

Configuration for attribute-based clustering.  Attribute-based clustering groups documents by metadata attributes (e.g., category, brand, status) instead of vector similarity. This is useful for organizing content by business logic rather than semantic similarity.  Examples:     - Group products by category and brand     - Organize orders by status and priority     - Cluster content by author and topic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **List[str]** | List of attribute field names to use for clustering. Documents will be grouped by unique combinations of these attribute values. Supports dot-notation for nested fields (e.g., &#39;metadata.category&#39;). Order matters for hierarchical grouping: first attribute is top-level, subsequent are nested. | 
**hierarchical_grouping** | **bool** | Whether to create hierarchical clusters based on attribute order. When True: Creates parent clusters for each unique value of the first attribute, then child clusters for subsequent attributes within each parent. When False: Creates flat clusters for each unique combination of all attributes. Example with [&#39;category&#39;, &#39;brand&#39;]:   hierarchical&#x3D;True → &#39;Electronics&#39; (parent) → &#39;Apple&#39;, &#39;Samsung&#39; (children).   hierarchical&#x3D;False → &#39;Electronics_Apple&#39;, &#39;Electronics_Samsung&#39; (flat). | [optional] [default to False]
**aggregation_method** | **str** | Method for aggregating attribute values when creating cluster centroids. Options: &#39;most_frequent&#39; (default), &#39;first&#39;, &#39;last&#39;. Most use cases should use the default. | [optional] 

## Example

```python
from mixpeek.models.attribute_based_config import AttributeBasedConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeBasedConfig from a JSON string
attribute_based_config_instance = AttributeBasedConfig.from_json(json)
# print the JSON string representation of the object
print(AttributeBasedConfig.to_json())

# convert the object into a dict
attribute_based_config_dict = attribute_based_config_instance.to_dict()
# create an instance of AttributeBasedConfig from a dict
attribute_based_config_from_dict = AttributeBasedConfig.from_dict(attribute_based_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


