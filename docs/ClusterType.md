# ClusterType

Type of clustering to perform.  Determines the clustering approach: - vector: Cluster documents by embedding similarity (semantic clustering) - attribute: Cluster documents by metadata attributes (business logic clustering)  Use Cases:     vector:         - Group semantically similar content         - Find content with similar meaning         - Organize by topic/theme         - Requires vector embeddings      attribute:         - Group by business attributes (category, brand, status, etc.)         - Organize by explicit metadata         - Create hierarchical groupings         - No embeddings required

## Enum

* `VECTOR` (value: `'vector'`)

* `ATTRIBUTE` (value: `'attribute'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


