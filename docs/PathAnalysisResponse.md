# PathAnalysisResponse

API response model for multi-step path analysis.  Contains discovered transition paths with frequency and duration statistics.  Example Response:     ```json     {         \"from_step\": \"inquiry\",         \"to_step\": \"closed_won\",         \"total_sequences\": 1000,         \"completed_sequences\": 350,         \"completion_rate\": 0.35,         \"paths\": [             {                 \"path\": [\"inquiry\", \"followup\", \"proposal\", \"closed_won\"],                 \"count\": 120,                 \"percentage\": 34.3,                 \"avg_duration_sec\": 604800.0             },             {                 \"path\": [\"inquiry\", \"proposal\", \"closed_won\"],                 \"count\": 90,                 \"percentage\": 25.7,                 \"avg_duration_sec\": 432000.0             },             {                 \"path\": [\"inquiry\", \"closed_won\"],                 \"count\": 70,                 \"percentage\": 20.0,                 \"avg_duration_sec\": 172800.0             }         ]     }     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_step** | **str** |  | 
**to_step** | **str** |  | 
**total_sequences** | **int** | Total sequences that started at from_step | 
**completed_sequences** | **int** | Number of sequences that reached to_step | 
**completion_rate** | **float** | Percentage that completed the path | 
**paths** | [**List[TransitionPath]**](TransitionPath.md) | List of paths sorted by frequency (most common first) | 

## Example

```python
from mixpeek.models.path_analysis_response import PathAnalysisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PathAnalysisResponse from a JSON string
path_analysis_response_instance = PathAnalysisResponse.from_json(json)
# print the JSON string representation of the object
print(PathAnalysisResponse.to_json())

# convert the object into a dict
path_analysis_response_dict = path_analysis_response_instance.to_dict()
# create an instance of PathAnalysisResponse from a dict
path_analysis_response_from_dict = PathAnalysisResponse.from_dict(path_analysis_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


