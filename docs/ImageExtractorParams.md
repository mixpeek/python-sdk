# ImageExtractorParams

Parameters for the Image Extractor.  The Image Extractor processes images to generate dense vector embeddings using Google's SigLIP (Sigmoid Language-Image Pre-training) model.  **When to Use**:     - Image search and similarity matching     - Visual content discovery and recommendations     - Image clustering and organization     - Cross-modal search (find images from text queries via SigLIP text encoder)     - E-commerce product image search     - Stock photo/media library search  **When NOT to Use**:     - Face recognition (use face_identity_extractor instead)     - Video content (use multimodal_extractor instead)     - Text-heavy images requiring OCR (use multimodal_extractor with OCR enabled)  **Model Details**:     - Model: google/siglip-base-patch16-224     - Embedding dimensions: 768     - Input resolution: 224x224     - Training: Sigmoid loss (improved over CLIP's contrastive loss)  **Performance**:     - Processing time: ~50-100ms per image     - Batch processing: Up to 24 images per batch     - GPU accelerated inference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractor_type** | **str** | Discriminator field for parameter type identification. Must be &#39;image_extractor&#39;. | [optional] [default to 'image_extractor']
**enable_thumbnails** | **bool** | Whether to generate thumbnail images. Thumbnails are resized/optimized versions uploaded to S3. Useful for UI previews and reducing bandwidth. | [optional] [default to True]
**use_cdn** | **bool** | Whether to use CloudFront CDN for thumbnail delivery. When True: Uploads to public bucket with CloudFront URLs. When False: Uses private bucket with presigned URLs. | [optional] [default to False]

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


