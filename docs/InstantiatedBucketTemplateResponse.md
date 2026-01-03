# InstantiatedBucketTemplateResponse

Response after instantiating a bucket template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** | ID of the created bucket | 
**bucket_name** | **str** | Name of the created bucket | 
**template_id** | **str** | ID of the template used | 
**status** | **str** | Status of the instantiation | [optional] [default to 'created']
**created_at** | **datetime** | Timestamp when bucket was created | [optional] 

## Example

```python
from mixpeek.models.instantiated_bucket_template_response import InstantiatedBucketTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstantiatedBucketTemplateResponse from a JSON string
instantiated_bucket_template_response_instance = InstantiatedBucketTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(InstantiatedBucketTemplateResponse.to_json())

# convert the object into a dict
instantiated_bucket_template_response_dict = instantiated_bucket_template_response_instance.to_dict()
# create an instance of InstantiatedBucketTemplateResponse from a dict
instantiated_bucket_template_response_from_dict = InstantiatedBucketTemplateResponse.from_dict(instantiated_bucket_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


