# CreateTaxonomyRequest

Request model to create a taxonomy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_name** | **str** | A unique name for the taxonomy within the namespace. | 
**description** | **str** | An optional description of the taxonomy. | [optional] 
**config** | [**Config1**](Config1.md) |  | 

## Example

```python
from mixpeek.models.create_taxonomy_request import CreateTaxonomyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaxonomyRequest from a JSON string
create_taxonomy_request_instance = CreateTaxonomyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTaxonomyRequest.to_json())

# convert the object into a dict
create_taxonomy_request_dict = create_taxonomy_request_instance.to_dict()
# create an instance of CreateTaxonomyRequest from a dict
create_taxonomy_request_from_dict = CreateTaxonomyRequest.from_dict(create_taxonomy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


