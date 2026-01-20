# ImageExtractorParams

Parameters for the Image Extractor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractor_type** | **str** | Discriminator field for parameter type identification. | [optional] [default to 'image_extractor']
**enable_thumbnails** | **bool** | Whether to generate thumbnail images. | [optional] [default to True]
**use_cdn** | **bool** | Whether to use CloudFront CDN for thumbnail delivery. | [optional] [default to False]

## Example

```python
from mixpeek.models.image_extractor_params import ImageExtractorParams

# TODO update the JSON string below
json = "{}"
# create an instance of ImageExtractorParams from a JSON string
image_extractor_params_instance = ImageExtractorParams.from_json(json)
# print the JSON string representation of the object
print(ImageExtractorParams.to_json())

# convert the object into a dict
image_extractor_params_dict = image_extractor_params_instance.to_dict()
# create an instance of ImageExtractorParams from a dict
image_extractor_params_from_dict = ImageExtractorParams.from_dict(image_extractor_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


