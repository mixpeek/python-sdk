# MultimodalExtractorParams

Parameters for the multimodal extractor.  The multimodal extractor processes video, audio, image, text, and GIF content in a unified embedding space. Videos/GIFs/Audio are decomposed into segments with transcription, visual analysis (video only), OCR, and embeddings. Images and text are embedded directly without decomposition.  **When to Use**:     - Video content libraries requiring searchable segments     - Audio content (podcasts, lectures, music) requiring transcription and search     - Media platforms with search across spoken and visual content     - Educational content with lecture videos and demonstrations     - Surveillance/security footage requiring event detection     - Social media platforms with user-generated video content     - Broadcasting/streaming services with large video catalogs     - Training video repositories with instructional content     - Marketing/advertising analytics for video campaigns  **When NOT to Use**:     - Static image collections → Use image_extractor instead     - Very short videos (<5 seconds) → Overhead not worth it     - Real-time live streams → Use specialized streaming extractors     - Extremely high-resolution videos (8K+) → Consider downsampling first  **Decomposition Methods**:      | Method | Use Case | Accuracy | Segments/Min | Best For |     |--------|----------|----------|--------------|----------|     | **TIME** | Fixed intervals | N/A | 60/interval_sec | General purpose, audio/video chunking |     | **SCENE** | Visual changes | 85-90% | Variable (2-20) | Movies, dynamic content (video only) |     | **SILENCE** | Audio pauses | 80-85% | Variable (5-30) | Lectures, presentations, audio/video |  **Feature Extraction Options**:     - Transcription: Speech-to-text using Whisper (95%+ accuracy)     - Multimodal Embeddings: Unified embeddings from Vertex AI (1408D) for video/image/gif/text     - Transcription Embeddings: Text embeddings from E5-Large (1024D)     - OCR: Text extraction from video frames using Gemini Vision     - Descriptions: AI-generated segment summaries using Gemini     - Thumbnails: Visual preview images for each segment  **Performance Characteristics**:     - Processing Speed: 0.5-2x realtime (depends on features enabled)     - Example: 10min video → 5-20 minutes processing time     - Transcription: ~200ms per second of audio     - Visual Embedding: ~50ms per segment     - OCR: ~300ms per segment     - Description: ~2s per segment (if enabled)  Requirements:     - video URL: REQUIRED (accessible video file)     - All feature parameters: OPTIONAL (defaults provided)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractor_type** | **str** | Discriminator field for parameter type identification. Must be &#39;multimodal_extractor&#39;. | [optional] [default to 'multimodal_extractor']
**split_method** | [**SplitMethod**](SplitMethod.md) | The PRIMARY control for video splitting strategy. This determines which splitting method is used. | [optional] 
**description_prompt** | **str** | The prompt to use for description generation. | [optional] [default to 'Describe the video segment in detail.']
**time_split_interval** | **int** | Interval in seconds for &#39;time&#39; splitting. Used when split_method&#x3D;&#39;time&#39;. | [optional] [default to 10]
**silence_db_threshold** | **int** | The decibel level below which audio is considered silent. Used when split_method&#x3D;&#39;silence&#39;. Recommended value: -40 (auto-applied if not specified). Lower values (e.g., -50) detect more silence, higher values (e.g., -30) detect less. | [optional] 
**scene_detection_threshold** | **float** | The threshold for scene detection (0.0-1.0). Used when split_method&#x3D;&#39;scene&#39;. Recommended value: 0.5 (auto-applied if not specified). Lower values (e.g., 0.3) detect more scenes, higher values (e.g., 0.7) detect fewer scenes. | [optional] 
**run_transcription** | **bool** | Whether to run transcription on video segments. | [optional] [default to False]
**transcription_language** | **str** | The language of the transcription. Used when run_transcription is True. | [optional] [default to 'en']
**run_video_description** | **bool** | Whether to generate descriptions for video segments. OPTIMIZED: Defaults to False as descriptions add 1-2 minutes. Enable only when needed. | [optional] [default to False]
**run_transcription_embedding** | **bool** | Whether to generate embeddings for transcriptions. Useful for semantic search over spoken content. | [optional] [default to False]
**run_multimodal_embedding** | **bool** | Whether to generate multimodal embeddings for all content types (video/image/gif/text). Uses Google Vertex AI to create unified 1408D embeddings in a shared semantic space. Useful for cross-modal semantic search across all media types. | [optional] [default to True]
**run_ocr** | **bool** | Whether to run OCR to extract text from video frames. OPTIMIZED: Defaults to False as OCR adds significant processing time. Enable only when text extraction from video is required. | [optional] [default to False]
**sensitivity** | **str** | The sensitivity of the scene detection. | [optional] [default to 'low']
**enable_thumbnails** | **bool** | Whether to generate thumbnail images for video segments and images. Thumbnails provide visual previews for navigation and UI display. For videos: Extracts a frame from each segment. For images: Creates an optimized thumbnail version.  | [optional] [default to True]
**use_cdn** | **bool** | Whether to use CloudFront CDN for thumbnail delivery. When True: Uploads to public bucket and returns CloudFront URLs. When False (default): Uploads to private bucket with presigned S3 URLs. Benefits of CDN: faster global delivery, permanent URLs, reduced bandwidth costs. Requires CLOUDFRONT_PUBLIC_DOMAIN to be configured in settings. Only applies when enable_thumbnails&#x3D;True. | [optional] [default to False]
**generation_config** | [**GenerationConfig**](GenerationConfig.md) |  | [optional] 
**response_shape** | [**ResponseShape1**](ResponseShape1.md) |  | [optional] 

## Example

```python
from mixpeek.models.multimodal_extractor_params import MultimodalExtractorParams

# TODO update the JSON string below
json = "{}"
# create an instance of MultimodalExtractorParams from a JSON string
multimodal_extractor_params_instance = MultimodalExtractorParams.from_json(json)
# print the JSON string representation of the object
print(MultimodalExtractorParams.to_json())

# convert the object into a dict
multimodal_extractor_params_dict = multimodal_extractor_params_instance.to_dict()
# create an instance of MultimodalExtractorParams from a dict
multimodal_extractor_params_from_dict = MultimodalExtractorParams.from_dict(multimodal_extractor_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


