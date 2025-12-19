# SDK Method Names - Clean & Intuitive

The Mixpeek Python SDK uses simplified, developer-friendly method names with all `v1` prefixes and redundant path information removed.

## Method Name Transformation

### Before & After Examples

| Original (Auto-generated) | Simplified | API |
|--------------------------|------------|-----|
| `create_collection_v1_collections_post` | `create_collection` | Collections |
| `get_collection_v1_collections__collection_identifier__get` | `get_collection` | Collections |
| `list_collections_v1_collections_list_post` | `list_collections` | Collections |
| `delete_collection_v1_collections__collection_identifier__delete` | `delete_collection` | Collections |
| `describe_collection_features_route_v1_collections__collection_identifier__features_get` | `describe_collection_features` | Collections |
| `create_retriever_v1_retrievers_post` | `create_retriever` | Retrievers |
| `execute_retriever_v1_retrievers__retriever_identifier__execute_post` | `execute_retriever` | Retrievers |
| `list_retrievers_v1_retrievers_list_post` | `list_retrievers` | Retrievers |
| `create_document_v1_collections__collection_identifier__documents_post` | `create_document` | Documents |
| `get_document_v1_collections__collection_identifier__documents__document_id__get` | `get_document` | Documents |
| `create_organization_private_v1_private_organizations_post` | `create_organization` | Organizations |
| `create_namespace_v1_namespaces_post` | `create_namespace` | Namespaces |
| `create_bucket_v1_buckets_post` | `create_bucket` | Buckets |
| `execute_cluster_v1_clusters__cluster_identifier__execute_post` | `execute_cluster` | Clusters |
| `create_taxonomy_v1_taxonomies_post` | `create_taxonomy` | Taxonomies |

## Method Naming Convention

All methods follow a consistent, intuitive pattern:

```python
{action}_{resource}
```

### Common Actions

- **create** - Create a new resource
- **get** - Retrieve a specific resource
- **list** - List multiple resources
- **update** - Update an existing resource
- **delete** - Delete a resource
- **execute** - Execute an operation (search, cluster, etc.)
- **describe** - Get detailed information

### Example Usage

#### Collections

```python
from mixpeek.api import collections_api

# Clean, intuitive method names
collections.create_collection(...)      # Create
collections.get_collection(...)         # Read
collections.update_collection(...)      # Update
collections.delete_collection(...)      # Delete
collections.list_collections()          # List
```

#### Retrievers

```python
from mixpeek.api import retrievers_api

# Clear, simple methods
retrievers.create_retriever(...)
retrievers.get_retriever(...)
retrievers.execute_retriever(...)       # Execute search
retrievers.list_retrievers()
retrievers.delete_retriever(...)
```

#### Documents

```python
from mixpeek.api import collection_documents_api

# Straightforward document operations
documents.create_document(...)
documents.get_document(...)
documents.update_document(...)
documents.delete_document(...)
documents.list_documents()
```

#### Clusters

```python
from mixpeek.api import clusters_api

# Simple cluster management
clusters.create_cluster(...)
clusters.get_cluster(...)
clusters.execute_cluster(...)           # Run clustering
clusters.list_clusters()
clusters.delete_cluster(...)
```

## Benefits

### ✅ Developer-Friendly

- **No version prefixes**: No more `v1_` in method names
- **No HTTP methods**: No `_post`, `_get`, `_delete` suffixes
- **No path duplication**: No redundant `collections_collections` or `list_list`
- **Clean identifiers**: Parameters like `collection_identifier` instead of path components

### ✅ Intuitive & Predictable

Every API follows CRUD patterns:

```python
# Pattern is always the same
api.create_{resource}(...)
api.get_{resource}(...)
api.update_{resource}(...)
api.delete_{resource}(...)
api.list_{resources}()
```

### ✅ IDE-Friendly

With simplified names, IDE autocomplete is much more useful:

```python
from mixpeek.api import collections_api

collections.cr[TAB]
# Shows:
#   - create_collection
#   - (not create_collection_v1_collections_post)
```

## Full API Reference

### Available APIs (18 total)

1. **BucketBatchesApi** - Batch operations on buckets
2. **BucketObjectsApi** - Object management in buckets
3. **BucketsApi** - Bucket storage management
4. **ClusterTriggersApi** - Automated cluster triggers
5. **ClustersApi** - Clustering and analysis
6. **CollectionDocumentsApi** - Document CRUD operations
7. **CollectionsApi** - Collection management
8. **FeatureExtractorsApi** - Feature extraction
9. **HealthApi** - Service health checks
10. **NamespacesApi** - Namespace management
11. **OrganizationsApi** - Organization management
12. **OrganizationsPrivateApi** - Private organization ops
13. **RetrieverStagesApi** - Retriever stage definitions
14. **RetrieversApi** - Search and retrieval
15. **TasksApi** - Async task monitoring
16. **TaxonomiesApi** - Classification and tagging

All APIs use the same clean, consistent method naming.

## Technical Details

### How Method Names are Simplified

The SDK generation process automatically:

1. **Removes version prefixes**: `_v1_`, `_v2_`, etc.
2. **Removes HTTP method suffixes**: `_post`, `_get`, `_put`, `_delete`, `_patch`
3. **Removes path identifiers**: `__identifier__`, `__id__`
4. **Deduplicates words**: `list_collections_list` → `list_collections`
5. **Removes generic terms**: `route`, `endpoint`, `api`, `private`, `public`
6. **Prevents plural/singular duplication**: `collections_collection` → `collection`

### Maintaining Compatibility

These simplified names are generated during SDK creation from the OpenAPI spec. They are:
- ✅ Stable across regenerations
- ✅ Type-safe with full IDE support
- ✅ Documented with docstrings
- ✅ Include parameter hints

---

**Note**: This simplification happens automatically during SDK generation. When the API updates, the method names remain clean and consistent.

