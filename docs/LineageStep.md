# LineageStep

Single processing step in a document's lineage chain.  Each step represents one transformation in the decomposition tree, tracking which collection and feature extractor produced the document.  Example:     ```python     step = LineageStep(         collection_id=\"col_video_frames\",         feature_extractor_id=\"multimodal_extractor_v1\",         document_id=\"doc_frame123\",         timestamp=datetime.now()     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | Collection ID where this processing step occurred | 
**feature_extractor_id** | **str** | Feature extractor that processed the data in this step | 
**document_id** | **str** | Document ID from this step (for intermediate steps). Allows tracing back through the decomposition tree. | [optional] 
**timestamp** | **datetime** | When this processing step occurred | [optional] 

## Example

```python
from mixpeek.models.lineage_step import LineageStep

# TODO update the JSON string below
json = "{}"
# create an instance of LineageStep from a JSON string
lineage_step_instance = LineageStep.from_json(json)
# print the JSON string representation of the object
print(LineageStep.to_json())

# convert the object into a dict
lineage_step_dict = lineage_step_instance.to_dict()
# create an instance of LineageStep from a dict
lineage_step_from_dict = LineageStep.from_dict(lineage_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


