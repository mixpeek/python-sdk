# FaceIdentityExtractorParams

Parameters for the Face Identity Extractor.  The Face Identity Extractor processes images or video frames to detect, align, and embed faces using production-grade SOTA models (SCRFD + ArcFace).  Core Pipeline: 1. SCRFD Detection → Bounding boxes + 5 landmarks 2. 5-Point Affine Alignment → 112×112 canonical face 3. ArcFace Embedding → 512-d L2-normalized vector 4. Optional Quality Scoring → Filter low-quality faces  Use Cases:     - Face verification (1:1 matching)     - Face identification (1:N search)     - Face clustering (group photos by person)     - Duplicate face detection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractor_type** | **str** | Discriminator field for parameter type identification. Must be &#39;face_identity_extractor&#39;. | [optional] [default to 'face_identity_extractor']
**detection_model** | **str** | SCRFD model for face detection. &#39;scrfd_500m&#39;: Fastest (2-3ms). &#39;scrfd_2.5g&#39;: Balanced (5-7ms), recommended. &#39;scrfd_10g&#39;: Highest accuracy (10-15ms). | [optional] [default to 'scrfd_2.5g']
**min_face_size** | **int** | Minimum face size in pixels to detect. 20px: Balanced. 40px: Higher quality. 10px: Maximum recall. | [optional] [default to 20]
**detection_threshold** | **float** | Confidence threshold for face detection (0.0-1.0). | [optional] [default to 0.5]
**max_faces_per_image** | **int** | Maximum number of faces to process per image. None: Process all. | [optional] 
**normalize_embeddings** | **bool** | L2-normalize embeddings to unit vectors (recommended). | [optional] [default to True]
**enable_quality_scoring** | **bool** | Compute quality scores (blur, size, landmarks). Adds ~5ms per face. | [optional] [default to True]
**quality_threshold** | **float** | Minimum quality score to index faces. None: Index all faces. 0.5: Moderate filtering. 0.7: High quality only. | [optional] 
**max_video_length** | **int** | Maximum video length in seconds. 60: Default. 10: Recommended for retrieval. 300: Maximum (extraction only). | [optional] [default to 60]
**video_sampling_fps** | **float** | Frames per second to sample from video. 1.0: One frame per second (recommended). | [optional] [default to 1.0]
**video_deduplication** | **bool** | Remove duplicate faces across video frames (extraction only). Reduces 90-95% redundancy. NOT used in retrieval. | [optional] [default to True]
**video_deduplication_threshold** | **float** | Cosine similarity threshold for deduplication. 0.8: Conservative (default). | [optional] [default to 0.8]
**output_mode** | **str** | &#39;per_face&#39;: One document per face (recommended). &#39;per_image&#39;: One doc per image with faces array. | [optional] [default to 'per_face']
**include_face_crops** | **bool** | Include aligned 112×112 face crops as base64. Adds ~5KB per face. | [optional] [default to False]
**store_detection_metadata** | **bool** | Store bbox, landmarks, detection scores. Recommended for debugging. | [optional] [default to True]

## Example

```python
from mixpeek.models.face_identity_extractor_params import FaceIdentityExtractorParams

# TODO update the JSON string below
json = "{}"
# create an instance of FaceIdentityExtractorParams from a JSON string
face_identity_extractor_params_instance = FaceIdentityExtractorParams.from_json(json)
# print the JSON string representation of the object
print(FaceIdentityExtractorParams.to_json())

# convert the object into a dict
face_identity_extractor_params_dict = face_identity_extractor_params_instance.to_dict()
# create an instance of FaceIdentityExtractorParams from a dict
face_identity_extractor_params_from_dict = FaceIdentityExtractorParams.from_dict(face_identity_extractor_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


