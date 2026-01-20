# PathAnalysisRequest

API request model for multi-step path analysis.  Discovers the most common sequences of intermediate steps documents take when progressing from from_step to to_step.  Unlike the transitions endpoint which only analyzes direct A→B progressions, this endpoint reveals the actual paths taken (e.g., A → X → Y → B).  Example:     ```json     {         \"collection_id\": \"col_emails\",         \"taxonomy_id\": \"tax_sales_stages\",         \"from_step\": \"inquiry\",         \"to_step\": \"closed_won\",         \"max_path_length\": 10,         \"min_support\": 5     }     ```  Response includes:     - Most common paths sorted by frequency     - Count and percentage for each path     - Average duration per path

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | Collection to analyze | 
**taxonomy_id** | **str** | Taxonomy ID | 
**from_step** | **str** | Starting step | 
**to_step** | **str** | Ending step | 
**max_path_length** | **int** | Maximum number of steps in a path | [optional] [default to 10]
**min_support** | **int** | Minimum sequences required to include a path | [optional] [default to 5]
**max_window_days** | **int** | Maximum duration for path completion (in days) | [optional] 
**filters** | **object** | Optional event filters | [optional] 

## Example

```python
from mixpeek.models.path_analysis_request import PathAnalysisRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PathAnalysisRequest from a JSON string
path_analysis_request_instance = PathAnalysisRequest.from_json(json)
# print the JSON string representation of the object
print(PathAnalysisRequest.to_json())

# convert the object into a dict
path_analysis_request_dict = path_analysis_request_instance.to_dict()
# create an instance of PathAnalysisRequest from a dict
path_analysis_request_from_dict = PathAnalysisRequest.from_dict(path_analysis_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


