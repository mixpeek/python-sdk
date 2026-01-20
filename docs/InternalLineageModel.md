# InternalLineageModel

Lineage tracking information for document provenance.  Tracks the complete processing history from the original bucket object through all transformation stages in the decomposition tree.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_object_id** | **str** | Original object ID from bucket (root of decomposition tree). All documents derived from the same object share this ID. | [optional] 
**root_bucket_id** | **str** | Bucket ID containing the root object. | [optional] 
**source_type** | **str** | Type of immediate parent source. &#39;bucket&#39;: Document created directly from bucket object (tier 1). &#39;collection&#39;: Document created from another collection (tier 2+). | [optional] 
**source_object_id** | **str** | Object ID of immediate parent when source_type&#x3D;&#39;bucket&#39;. | [optional] 
**source_document_id** | **str** | Document ID of immediate parent when source_type&#x3D;&#39;collection&#39;. | [optional] 
**source_collection_id** | **str** | Collection ID of immediate parent when source_type&#x3D;&#39;collection&#39;. | [optional] 
**path** | **str** | Materialized lineage path string (e.g., &#39;bkt_123/col_456/col_789&#39;). | [optional] 
**chain** | **List[object]** | Ordered list of processing steps from root object to this document. Each step contains: collection_id, feature_extractor_id, document_id, timestamp. | [optional] 

## Example

```python
from mixpeek.models.internal_lineage_model import InternalLineageModel

# TODO update the JSON string below
json = "{}"
# create an instance of InternalLineageModel from a JSON string
internal_lineage_model_instance = InternalLineageModel.from_json(json)
# print the JSON string representation of the object
print(InternalLineageModel.to_json())

# convert the object into a dict
internal_lineage_model_dict = internal_lineage_model_instance.to_dict()
# create an instance of InternalLineageModel from a dict
internal_lineage_model_from_dict = InternalLineageModel.from_dict(internal_lineage_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


