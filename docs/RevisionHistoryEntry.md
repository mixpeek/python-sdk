# RevisionHistoryEntry

A single entry in the revision history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | Version number | 
**updated_at** | **datetime** | When this version was created | 
**updated_by** | **str** | User who made the change | [optional] 
**changes** | **str** | Description of changes made | [optional] 

## Example

```python
from mixpeek.models.revision_history_entry import RevisionHistoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RevisionHistoryEntry from a JSON string
revision_history_entry_instance = RevisionHistoryEntry.from_json(json)
# print the JSON string representation of the object
print(RevisionHistoryEntry.to_json())

# convert the object into a dict
revision_history_entry_dict = revision_history_entry_instance.to_dict()
# create an instance of RevisionHistoryEntry from a dict
revision_history_entry_from_dict = RevisionHistoryEntry.from_dict(revision_history_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


