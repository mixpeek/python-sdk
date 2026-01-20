# PatchTaxonomyRequest

Request to update a taxonomy's metadata.  **IMPORTANT: Partial Updates with Controlled Mutability**  This endpoint allows updating ONLY metadata fields. Core taxonomy logic is immutable to ensure consistency for join history and dependent resources.  **✅ Fields You CAN Update (Metadata Only):** - `taxonomy_name`: Rename the taxonomy - `description`: Update documentation - `metadata`: Update custom metadata fields  **❌ Fields You CANNOT Update (Immutable Core Logic):** - `config`: Taxonomy configuration (retriever_id, input_mappings, collections, hierarchy) - `taxonomy_type`: Type (flat vs hierarchical) - `retriever_id`: Associated retriever - `input_mappings`: Field mappings - `enrichment_fields`: Enrichment configuration  **Need to Modify Core Logic?** Use POST /taxonomies/{taxonomy_id}/clone instead. Cloning creates a new taxonomy with a new ID, allowing you to: - Change retriever or input mappings - Modify enrichment fields - Update collection configuration - Change taxonomy hierarchy  **Behavior:** - All fields are OPTIONAL - provide only what you want to update - Empty updates (no fields provided) will be rejected with 400 error - Original taxonomy remains unchanged (no destructive operations)  **Why This Design?** - Join history is tied to specific taxonomy configuration - Changing retriever would invalidate previous joins - Version tracking enables auditing and rollback

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_name** | **str** | Updated name for the taxonomy | [optional] 
**description** | **str** | Updated description for the taxonomy | [optional] 
**metadata** | **object** | Updated metadata for the taxonomy | [optional] 

## Example

```python
from mixpeek.models.patch_taxonomy_request import PatchTaxonomyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchTaxonomyRequest from a JSON string
patch_taxonomy_request_instance = PatchTaxonomyRequest.from_json(json)
# print the JSON string representation of the object
print(PatchTaxonomyRequest.to_json())

# convert the object into a dict
patch_taxonomy_request_dict = patch_taxonomy_request_instance.to_dict()
# create an instance of PatchTaxonomyRequest from a dict
patch_taxonomy_request_from_dict = PatchTaxonomyRequest.from_dict(patch_taxonomy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


