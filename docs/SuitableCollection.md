# SuitableCollection

Information about a collection that might fulfill the user's request.  Attributes:     collection_id: Collection identifier     collection_name: Human-readable collection name     feature_extractor: Extractor used in this collection     capabilities: What this collection can do (e.g., \"video search\", \"face detection\")     match_score: How well this collection matches the request (0.0-1.0)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | Collection ID | 
**collection_name** | **str** | Collection name | 
**feature_extractor** | **str** | Feature extractor name | 
**capabilities** | **List[str]** | Collection capabilities | [optional] 
**match_score** | **float** | Match confidence | 

## Example

```python
from mixpeek.models.suitable_collection import SuitableCollection

# TODO update the JSON string below
json = "{}"
# create an instance of SuitableCollection from a JSON string
suitable_collection_instance = SuitableCollection.from_json(json)
# print the JSON string representation of the object
print(SuitableCollection.to_json())

# convert the object into a dict
suitable_collection_dict = suitable_collection_instance.to_dict()
# create an instance of SuitableCollection from a dict
suitable_collection_from_dict = SuitableCollection.from_dict(suitable_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


