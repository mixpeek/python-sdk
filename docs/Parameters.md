# Parameters

Parameters for the feature extractor. Each extractor type has specific parameters. See the schema for your chosen extractor (e.g., MultimodalExtractorParams for multimodal_extractor).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractor_type** | **str** | Discriminator field for parameter type identification. Must be &#39;document_graph_extractor&#39;. | [optional] [default to 'document_graph_extractor']
**split_by** | [**TextSplitStrategy**](TextSplitStrategy.md) | OPTIONAL. Strategy for splitting text into multiple documents. Default is &#39;none&#39; (no splitting, entire text becomes one document). Options: &#39;characters&#39; - Split by character count (fastest, may break words). &#39;words&#39; - Split by word boundaries (preserves words). &#39;sentences&#39; - Split by sentence boundaries (preserves semantic units). &#39;paragraphs&#39; - Split by paragraph boundaries (best for articles). &#39;pages&#39; - Split by page breaks (best for paginated documents). &#39;none&#39; - No splitting (default). Choose based on your content structure and retrieval granularity needs. | [optional] 
**chunk_size** | **int** | OPTIONAL. Target size for each chunk. Interpretation depends on split_by strategy: - characters: Number of characters per chunk (e.g., 1000 chars). - words: Number of words per chunk (e.g., 200 words). - sentences: Number of sentences per chunk (e.g., 5 sentences). - paragraphs: Number of paragraphs per chunk (e.g., 2 paragraphs). - pages: Number of pages per chunk (e.g., 1 page). - none: Ignored (entire text processed as one document). Default: 1000. Recommended ranges: characters (500-2000), words (100-400), sentences (3-10). | [optional] [default to 1000]
**chunk_overlap** | **int** | OPTIONAL. Number of units to overlap between consecutive chunks. Helps preserve context across chunk boundaries. Units match split_by strategy (characters, words, sentences, etc.). Example: With chunk_size&#x3D;1000 and chunk_overlap&#x3D;100, chunks will be: [0-1000], [900-1900], [1800-2800], etc. Default: 0 (no overlap). Recommended: 10-20% of chunk_size (e.g., 100-200 for chunk_size&#x3D;1000). Higher overlap improves context but increases storage and processing time. | [optional] [default to 0]
**response_shape** | [**ResponseShape1**](ResponseShape1.md) |  | [optional] 
**llm_provider** | **str** | OPTIONAL. LLM provider to use for structured extraction. Only required if response_shape is provided. Supported providers: &#39;openai&#39;, &#39;google&#39;, &#39;anthropic&#39;. Default: &#39;openai&#39; if not specified. | [optional] 
**llm_model** | **str** | OPTIONAL. Specific LLM model for structured extraction. Only required if response_shape is provided. Examples: - OpenAI: &#39;gpt-4o-mini-2024-07-18&#39; (efficient), &#39;gpt-4o-2024-08-06&#39; (best quality) - Google: &#39;gemini-2.0-flash&#39; (fastest, recommended) - Anthropic: &#39;claude-3-5-haiku-20241022&#39; (fast), &#39;claude-3-5-sonnet-20241022&#39; (best reasoning) Default: Uses provider&#39;s recommended model if not specified. | [optional] 
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
**enable_thumbnails** | **bool** | Whether to generate thumbnail images. Thumbnails are resized/optimized versions uploaded to S3. Useful for UI previews and reducing bandwidth. | [optional] [default to True]
**use_cdn** | **bool** | Whether to use CloudFront CDN for thumbnail delivery. When True: Uploads to public bucket with CloudFront URLs. When False: Uses private bucket with presigned URLs. | [optional] [default to False]
**generation_config** | [**GenerationConfig**](GenerationConfig.md) |  | [optional] 
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
**use_layout_detection** | **bool** | Enable ML-based layout detection to find ALL document elements (text, images, tables, figures). When enabled, uses PaddleOCR to detect and extract both text regions AND non-text elements (scanned images, figures, charts) as separate documents. **Recommended for**: Scanned documents, image-heavy PDFs, mixed content documents. **When disabled**: Falls back to text-only extraction (faster but misses images). Default: True (detects all elements including images). | [optional] [default to True]
**vertical_threshold** | **float** | Maximum vertical gap (in points) between lines to be grouped in same block. Increase for looser grouping, decrease for tighter blocks. Default 15pt works well for standard documents. | [optional] [default to 15.0]
**horizontal_threshold** | **float** | Maximum horizontal distance (in points) for overlap detection. Affects column detection and block merging. Increase for wider columns, decrease for narrow layouts. | [optional] [default to 50.0]
**min_text_length** | **int** | Minimum text length (characters) to keep a block. Blocks with less text are filtered out. Helps remove noise and tiny fragments. | [optional] [default to 20]
**base_confidence** | **float** | Base confidence score for embedded (native) text. Penalties are subtracted for OCR artifacts, encoding issues, etc. | [optional] [default to 0.85]
**min_confidence_for_vlm** | **float** | Confidence threshold below which VLM correction is triggered. Blocks with confidence &lt; this value get sent to VLM for correction. Only applies when use_vlm_correction&#x3D;True. | [optional] [default to 0.6]
**use_vlm_correction** | **bool** | Enable VLM (Vision Language Model) correction for low-confidence blocks. Uses Gemini/GPT-4V to correct OCR errors by analyzing the page image. Significantly slower (~1 page/sec) but improves accuracy for degraded docs. | [optional] [default to True]
**fast_mode** | **bool** | Skip VLM correction entirely for maximum throughput (~15 pages/sec). Overrides use_vlm_correction. Use when speed is more important than accuracy. | [optional] [default to False]
**vlm_provider** | **str** | LLM provider for VLM correction. Options: &#39;google&#39; (Gemini), &#39;openai&#39; (GPT-4V), &#39;anthropic&#39; (Claude). Google recommended for best vision quality. | [optional] [default to 'google']
**vlm_model** | **str** | Specific model for VLM correction. Examples: &#39;gemini-2.0-flash&#39;, &#39;gpt-4o&#39;, &#39;claude-3-5-sonnet&#39;. | [optional] [default to 'gemini-2.0-flash']
**run_text_embedding** | **bool** | Generate text embeddings for semantic search over block content. Uses E5-Large (1024-dim) for multilingual support. | [optional] [default to True]
**render_dpi** | **int** | DPI for page rendering (used for VLM correction). 72: Fast, lower quality. 150: Balanced (recommended). 300: High quality, slower. | [optional] [default to 150]
**generate_thumbnails** | **bool** | Generate thumbnail images for blocks. Useful for visual previews and UI display. | [optional] [default to True]
**thumbnail_mode** | **str** | Thumbnail generation mode. &#39;full_page&#39;: Low-res thumbnail of entire page. &#39;segment&#39;: Cropped thumbnail of just the block&#39;s bounding box. &#39;both&#39;: Generate both types (recommended for flexibility). | [optional] [default to 'both']
**thumbnail_dpi** | **int** | DPI for thumbnail generation. Lower DPI &#x3D; smaller files. 72: Standard web quality. 36: Very small thumbnails. | [optional] [default to 72]

## Example

```python
from mixpeek.models.parameters import Parameters

# TODO update the JSON string below
json = "{}"
# create an instance of Parameters from a JSON string
parameters_instance = Parameters.from_json(json)
# print the JSON string representation of the object
print(Parameters.to_json())

# convert the object into a dict
parameters_dict = parameters_instance.to_dict()
# create an instance of Parameters from a dict
parameters_from_dict = Parameters.from_dict(parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


