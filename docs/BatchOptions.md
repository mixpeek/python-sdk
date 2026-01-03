# BatchOptions

Options for batch processing in migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_size** | **int** | Documents per batch | [optional] [default to 100]
**max_workers** | **int** | Maximum parallel workers | [optional] [default to 10]
**retry_failed** | **bool** | Retry failed batches | [optional] [default to True]

## Example

```python
from mixpeek.models.batch_options import BatchOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BatchOptions from a JSON string
batch_options_instance = BatchOptions.from_json(json)
# print the JSON string representation of the object
print(BatchOptions.to_json())

# convert the object into a dict
batch_options_dict = batch_options_instance.to_dict()
# create an instance of BatchOptions from a dict
batch_options_from_dict = BatchOptions.from_dict(batch_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


