# InstantiateBucketTemplateRequest

Request to instantiate a bucket from a template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Name for the new bucket | 
**description** | **str** | Optional description override for the bucket | [optional] 

## Example

```python
from mixpeek.models.instantiate_bucket_template_request import InstantiateBucketTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstantiateBucketTemplateRequest from a JSON string
instantiate_bucket_template_request_instance = InstantiateBucketTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(InstantiateBucketTemplateRequest.to_json())

# convert the object into a dict
instantiate_bucket_template_request_dict = instantiate_bucket_template_request_instance.to_dict()
# create an instance of InstantiateBucketTemplateRequest from a dict
instantiate_bucket_template_request_from_dict = InstantiateBucketTemplateRequest.from_dict(instantiate_bucket_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


