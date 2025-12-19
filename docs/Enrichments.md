# Enrichments

Container for document enrichments from various sources.  Uses existing models where appropriate to ensure consistency and reuse (e.g., `ClusterMember` for cluster assignments).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[ClusterMember]**](ClusterMember.md) | Cluster member assignments (reuses ClusterMember model) | [optional] 
**taxonomies** | [**List[TaxonomyAssignment]**](TaxonomyAssignment.md) | Taxonomy assignments referencing taxonomy/node IDs | [optional] 

## Example

```python
from mixpeek.models.enrichments import Enrichments

# TODO update the JSON string below
json = "{}"
# create an instance of Enrichments from a JSON string
enrichments_instance = Enrichments.from_json(json)
# print the JSON string representation of the object
print(Enrichments.to_json())

# convert the object into a dict
enrichments_dict = enrichments_instance.to_dict()
# create an instance of Enrichments from a dict
enrichments_from_dict = Enrichments.from_dict(enrichments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


