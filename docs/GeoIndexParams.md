# GeoIndexParams

Configuration for geo index.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'geo']

## Example

```python
from mixpeek.models.geo_index_params import GeoIndexParams

# TODO update the JSON string below
json = "{}"
# create an instance of GeoIndexParams from a JSON string
geo_index_params_instance = GeoIndexParams.from_json(json)
# print the JSON string representation of the object
print(GeoIndexParams.to_json())

# convert the object into a dict
geo_index_params_dict = geo_index_params_instance.to_dict()
# create an instance of GeoIndexParams from a dict
geo_index_params_from_dict = GeoIndexParams.from_dict(geo_index_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


