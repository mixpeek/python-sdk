# PatchRetrieverRequest

Request to update a retriever's metadata.  **IMPORTANT: Partial Updates with Controlled Mutability**  This endpoint allows updating ONLY metadata fields. Core retriever logic is immutable to ensure consistency for dependent resources (taxonomies, cached results, etc.).  **✅ Fields You CAN Update (Metadata Only):** - `retriever_name`: Rename the retriever - `description`: Update documentation - `tags`: Update organization tags - `display_config`: Update display configuration for publishing  **❌ Fields You CANNOT Update (Immutable Core Logic):** - `input_schema`: Input field definitions (breaks dependent taxonomies) - `stages`: Retriever stages and configurations (changes matching behavior) - `collection_ids`: Target collections (changes data sources) - `budget_limits`: Budget constraints (affects execution behavior)  **Need to Modify Core Logic?** Use POST /retrievers/{retriever_id}/clone instead. Cloning creates a new retriever with a new ID, allowing you to: - Fix typos in stage names - Add or remove stages - Change target collections - Modify input schema or budget limits  **Behavior:** - All fields are OPTIONAL - provide only what you want to update - Version number automatically increments on each update - Empty updates (no fields provided) will be rejected with 400 error - Original retriever remains unchanged (no destructive operations)  **Why This Design?** - Taxonomies reference retrievers by ID and expect consistent behavior - Cached results remain valid after metadata-only changes - Version tracking enables auditing and rollback - Published retrievers maintain stable behavior for consumers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_name** | **str** | Updated retriever name. OPTIONAL - only provide if you want to rename the retriever. | [optional] 
**description** | **str** | Updated human-readable description. OPTIONAL - only provide if you want to update the description. | [optional] 
**tags** | **List[str]** | Updated tags for organization and filtering. OPTIONAL - replaces existing tags if provided. | [optional] 
**display_config** | [**DisplayConfigInput**](DisplayConfigInput.md) | Updated display configuration for public retriever UI rendering. OPTIONAL - only provide if you want to update the display settings. Defines how the search interface should appear when published. | [optional] 

## Example

```python
from mixpeek.models.patch_retriever_request import PatchRetrieverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchRetrieverRequest from a JSON string
patch_retriever_request_instance = PatchRetrieverRequest.from_json(json)
# print the JSON string representation of the object
print(PatchRetrieverRequest.to_json())

# convert the object into a dict
patch_retriever_request_dict = patch_retriever_request_instance.to_dict()
# create an instance of PatchRetrieverRequest from a dict
patch_retriever_request_from_dict = PatchRetrieverRequest.from_dict(patch_retriever_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


