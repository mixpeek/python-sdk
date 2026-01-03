# InstantiateScaffoldRequest

Request to instantiate a scaffold template.  Only namespace_name is required. Other names use scaffold defaults.  Options:     include_sample_data: If true, clone from demo namespace with sample data.                         If false (default), create empty resources.  Example:     # Empty scaffold     {\"namespace_name\": \"my_app\"}      # With sample data     {\"namespace_name\": \"my_app\", \"include_sample_data\": true}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_name** | **str** | Name for the new namespace (required, must be unique) | 
**namespace_description** | **str** | Optional description for the namespace | [optional] 
**bucket_name** | **str** | Override default bucket name from scaffold | [optional] 
**collection_name** | **str** | Override default collection name from scaffold | [optional] 
**retriever_name** | **str** | Override default retriever name from scaffold | [optional] 
**include_sample_data** | **bool** | If true, include sample data from demo namespace. If false, create empty resources. | [optional] [default to False]

## Example

```python
from mixpeek.models.instantiate_scaffold_request import InstantiateScaffoldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstantiateScaffoldRequest from a JSON string
instantiate_scaffold_request_instance = InstantiateScaffoldRequest.from_json(json)
# print the JSON string representation of the object
print(InstantiateScaffoldRequest.to_json())

# convert the object into a dict
instantiate_scaffold_request_dict = instantiate_scaffold_request_instance.to_dict()
# create an instance of InstantiateScaffoldRequest from a dict
instantiate_scaffold_request_from_dict = InstantiateScaffoldRequest.from_dict(instantiate_scaffold_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


