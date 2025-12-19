# BatchStatistics

Statistics about batches in a bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of batches in this bucket | [optional] [default to 0]
**active** | **int** | Number of batches that are not completed (DRAFT, PENDING, IN_PROGRESS, PROCESSING) | [optional] [default to 0]
**completed** | **int** | Number of completed batches | [optional] [default to 0]
**failed** | **int** | Number of failed batches | [optional] [default to 0]

## Example

```python
from mixpeek.models.batch_statistics import BatchStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of BatchStatistics from a JSON string
batch_statistics_instance = BatchStatistics.from_json(json)
# print the JSON string representation of the object
print(BatchStatistics.to_json())

# convert the object into a dict
batch_statistics_dict = batch_statistics_instance.to_dict()
# create an instance of BatchStatistics from a dict
batch_statistics_from_dict = BatchStatistics.from_dict(batch_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


