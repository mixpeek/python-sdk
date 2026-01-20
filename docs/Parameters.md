# Parameters

Parameters for the feature extractor. Each extractor type has specific parameters. See the schema for your chosen extractor (e.g., MultimodalExtractorParams for multimodal_extractor).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractor_type** | **str** | Custom plugin extractor type (plugin name) | 
**split_by** | [**TextSplitStrategy**](TextSplitStrategy.md) | Strategy for splitting text into multiple documents. | [optional] 
**chunk_size** | **int** | Target size for each chunk (in units of chunk_strategy). | [optional] [default to 500]
**chunk_overlap** | **int** | Overlap between chunks to preserve context. | [optional] [default to 50]
**response_shape** | [**ResponseShape3**](ResponseShape3.md) |  | [optional] 
**llm_provider** | **str** | LLM provider for structured extraction: openai, google, anthropic | [optional] 
**llm_model** | **str** | LLM model for structured extraction. | [optional] 
**llm_api_key** | **str** | API key for LLM operations (BYOK - Bring Your Own Key). Supports: - Direct key: &#39;sk-proj-abc123...&#39; - Secret reference: &#39;{{SECRET.openai_api_key}}&#39;  When using secret reference, the key is loaded from your organization&#39;s secrets vault at runtime. Store secrets via POST /v1/organizations/secrets.  If not provided, uses Mixpeek&#39;s default API keys. | [optional] 
**split_method** | [**SplitMethod**](SplitMethod.md) | The PRIMARY control for video splitting strategy. This determines which splitting method is used. | [optional] 
**description_prompt** | **str** | The prompt to use for description generation. | [optional] [default to 'Describe the video segment in detail.']
**time_split_interval** | **int** | Interval in seconds for &#39;time&#39; splitting. Used when split_method&#x3D;&#39;time&#39;. | [optional] [default to 10]
**silence_db_threshold** | **int** | The decibel level below which audio is considered silent. Used when split_method&#x3D;&#39;silence&#39;. Recommended value: -40 (auto-applied if not specified). Lower values (e.g., -50) detect more silence, higher values (e.g., -30) detect less. | [optional] 
**scene_detection_threshold** | **float** | Scene detection sensitivity (0.0-1.0). | [optional] [default to 0.3]
**run_transcription** | **bool** | Whether to run transcription on video segments. | [optional] [default to False]
**transcription_language** | **str** | The language of the transcription. Used when run_transcription is True. | [optional] [default to 'en']
**run_video_description** | **bool** | Whether to generate descriptions for video segments. OPTIMIZED: Defaults to False as descriptions add 1-2 minutes. Enable only when needed. | [optional] [default to False]
**run_transcription_embedding** | **bool** | Whether to generate embeddings for transcriptions. Useful for semantic search over spoken content. | [optional] [default to False]
**run_multimodal_embedding** | **bool** | Whether to generate multimodal embeddings for all content types (video/image/gif/text). Uses Google Vertex AI to create unified 1408D embeddings in a shared semantic space. Useful for cross-modal semantic search across all media types. | [optional] [default to True]
**run_ocr** | **bool** | Whether to run OCR to extract text from video frames. OPTIMIZED: Defaults to False as OCR adds significant processing time. Enable only when text extraction from video is required. | [optional] [default to False]
**sensitivity** | **str** | The sensitivity of the scene detection. | [optional] [default to 'low']
**enable_thumbnails** | **bool** | Whether to generate thumbnail images. | [optional] [default to True]
**use_cdn** | **bool** | Use CDN for thumbnail delivery. | [optional] [default to False]
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
**use_layout_detection** | **bool** | Enable ML-based layout detection to find ALL document elements (text, images, tables, figures). When enabled, uses the configured layout_detector to detect and extract both text regions AND non-text elements (scanned images, figures, charts) as separate documents. **Recommended for**: Scanned documents, image-heavy PDFs, mixed content documents. **When disabled**: Falls back to text-only extraction (faster but misses images). Default: True (detects all elements including images). | [optional] [default to True]
**layout_detector** | **str** | Layout detection engine to use when use_layout_detection&#x3D;True. &#39;pymupdf&#39;: Fast, rule-based detection using PyMuPDF heuristics (~15 pages/sec). &#39;docling&#39;: SOTA ML-based detection using IBM Docling with DiT model (~3-8 sec/doc). **Docling advantages**: Better semantic type detection (section_header vs paragraph), true table structure extraction (rows/cols), more accurate figure detection. **PyMuPDF advantages**: Much faster, lower memory usage, simpler dependencies. Default: &#39;pymupdf&#39; for speed. Use &#39;docling&#39; for accuracy-critical applications. | [optional] [default to 'pymupdf']
**vertical_threshold** | **float** | Maximum vertical gap (in points) between lines to be grouped in same block. Increase for looser grouping, decrease for tighter blocks. Default 15pt works well for standard documents. | [optional] [default to 15.0]
**horizontal_threshold** | **float** | Maximum horizontal distance (in points) for overlap detection. Affects column detection and block merging. Increase for wider columns, decrease for narrow layouts. | [optional] [default to 50.0]
**min_text_length** | **int** | Minimum text length (characters) to keep a block. Blocks with less text are filtered out. Helps remove noise and tiny fragments. | [optional] [default to 20]
**base_confidence** | **float** | Base confidence score for embedded (native) text. Penalties are subtracted for OCR artifacts, encoding issues, etc. | [optional] [default to 0.85]
**min_confidence_for_vlm** | **float** | Confidence threshold below which VLM correction is triggered. Blocks with confidence &lt; this value get sent to VLM for correction. Only applies when use_vlm_correction&#x3D;True. | [optional] [default to 0.6]
**use_vlm_correction** | **bool** | Enable VLM (Vision Language Model) correction for low-confidence blocks. Uses Gemini/GPT-4V to correct OCR errors by analyzing the page image. Significantly slower (~1 page/sec) but improves accuracy for degraded docs. | [optional] [default to True]
**fast_mode** | **bool** | Skip VLM correction entirely for maximum throughput (~15 pages/sec). Overrides use_vlm_correction. Use when speed is more important than accuracy. | [optional] [default to False]
**vlm_provider** | **str** | LLM provider for VLM correction. Options: &#39;google&#39; (Gemini), &#39;openai&#39; (GPT-4V), &#39;anthropic&#39; (Claude). Google recommended for best vision quality. | [optional] [default to 'google']
**vlm_model** | **str** | Specific model for VLM correction. Examples: &#39;gemini-2.0-flash&#39;, &#39;gpt-4o&#39;, &#39;claude-3-5-sonnet&#39;. | [optional] [default to 'gemini-2.0-flash']
**run_text_embedding** | **bool** | Generate E5 text embeddings (1024D) for transcripts and text. | [optional] [default to True]
**render_dpi** | **int** | DPI for page rendering (used for VLM correction). 72: Fast, lower quality. 150: Balanced (recommended). 300: High quality, slower. | [optional] [default to 150]
**generate_thumbnails** | **bool** | Generate thumbnail images for each learning unit. | [optional] [default to True]
**thumbnail_mode** | **str** | Thumbnail generation mode. &#39;full_page&#39;: Low-res thumbnail of entire page. &#39;segment&#39;: Cropped thumbnail of just the block&#39;s bounding box. &#39;both&#39;: Generate both types (recommended for flexibility). | [optional] [default to 'both']
**thumbnail_dpi** | **int** | DPI for thumbnail generation. Lower DPI &#x3D; smaller files. 72: Standard web quality. 36: Very small thumbnails. | [optional] [default to 72]
**model_name** | **str** | HuggingFace model name for sentiment classification | [optional] [default to 'distilbert-base-uncased-finetuned-sst-2-english']
**max_length** | **int** | Maximum token length | [optional] [default to 512]
**batch_size** | **int** | Inference batch size | [optional] [default to 32]
**return_all_scores** | **bool** | Return scores for all classes, not just top | [optional] [default to True]
**embed** | **bool** | Generate E5 embeddings for semantic retrieval alongside classification. Uses the internal E5 embedding service for 1024-dimensional vectors. | [optional] [default to False]
**max_depth** | **int** | Maximum link depth to crawl. 0&#x3D;seed page only, 1&#x3D;seed+direct links, etc. Default: 2. Increase for comprehensive crawls, decrease for targeted extraction. | [optional] [default to 2]
**max_pages** | **int** | Maximum pages to crawl. Default: 50. Set higher (1000+) for large documentation sites. Max: 1,000,000. | [optional] [default to 50]
**crawl_timeout** | **int** | Maximum total time for crawling in seconds. Default: 300 (5 minutes). Increase for large sites with many pages. Max: 3600 (1 hour). | [optional] [default to 300]
**crawl_mode** | [**CrawlMode**](CrawlMode.md) | Crawl strategy. DETERMINISTIC: BFS all links (predictable). SEMANTIC: LLM-guided, prioritizes relevant pages (requires crawl_goal). | [optional] 
**crawl_goal** | **str** | Goal for semantic crawling. Only used when crawl_mode&#x3D;SEMANTIC. Example: &#39;Find all S3 API documentation and examples&#39; | [optional] 
**render_strategy** | [**RenderStrategy**](RenderStrategy.md) | How to render pages. AUTO (default): tries static, falls back to JS. STATIC: fast HTTP fetch. JAVASCRIPT: Playwright browser for SPAs. | [optional] 
**include_patterns** | **List[str]** | Regex patterns for URLs to include. Example: [&#39;/docs/&#39;, &#39;/api/&#39;] | [optional] 
**exclude_patterns** | **List[str]** | Regex patterns for URLs to exclude. Example: [&#39;/blog/&#39;, &#39;\\.pdf$&#39;] | [optional] 
**chunk_strategy** | [**ChunkStrategy**](ChunkStrategy.md) | How to split page content. NONE: one chunk per page. SENTENCES/PARAGRAPHS: semantic boundaries. WORDS/CHARACTERS: fixed size chunks. | [optional] 
**document_id_strategy** | [**DocumentIdStrategy**](DocumentIdStrategy.md) | How to generate document IDs. URL (default): stable across re-crawls. POSITION: order-based. CONTENT: deduplicates identical content. | [optional] 
**generate_text_embeddings** | **bool** | Generate E5 embeddings for text content. | [optional] [default to True]
**generate_code_embeddings** | **bool** | Generate Jina code embeddings for code blocks. | [optional] [default to True]
**generate_image_embeddings** | **bool** | Generate SigLIP embeddings for images/figures. | [optional] [default to True]
**max_retries** | **int** | Maximum retry attempts for failed HTTP requests. Uses exponential backoff with jitter. Default: 3. | [optional] [default to 3]
**retry_base_delay** | **float** | Base delay in seconds for retry backoff. Actual delay &#x3D; base * 2^attempt + jitter. Default: 1.0. | [optional] [default to 1.0]
**retry_max_delay** | **float** | Maximum delay in seconds between retries. Default: 30. | [optional] [default to 30.0]
**respect_retry_after** | **bool** | Respect Retry-After header from 429/503 responses. If False, uses exponential backoff instead. Default: True. | [optional] [default to True]
**proxies** | **List[str]** | List of proxy URLs for rotation. Supports formats: &#39;http://host:port&#39;, &#39;http://user:pass@host:port&#39;, &#39;socks5://host:port&#39;. Proxies rotate on errors or every N requests. | [optional] 
**rotate_proxy_on_error** | **bool** | Rotate to next proxy when request fails. Default: True. | [optional] [default to True]
**rotate_proxy_every_n_requests** | **int** | Rotate proxy every N requests (0 &#x3D; disabled). Useful for avoiding IP-based rate limits. Default: 0 (disabled). | [optional] [default to 0]
**captcha_service_provider** | **str** | Captcha solving service provider: &#39;2captcha&#39;, &#39;anti-captcha&#39;, &#39;capsolver&#39;. If not set, captcha pages are skipped gracefully. | [optional] 
**captcha_service_api_key** | **str** | API key for captcha solving service. Supports secret reference: &#39;{{SECRET.captcha_api_key}}&#39;. Required if captcha_service_provider is set. | [optional] 
**detect_captcha** | **bool** | Detect captcha challenges (Cloudflare, reCAPTCHA, hCaptcha). If detected and no solver configured, page is skipped. Default: True. | [optional] [default to True]
**persist_cookies** | **bool** | Persist cookies across requests within a crawl session. Useful for sites requiring authentication. Default: True. | [optional] [default to True]
**custom_headers** | **Dict[str, str]** | Custom HTTP headers to include in all requests. Example: {&#39;Authorization&#39;: &#39;Bearer token&#39;, &#39;X-Custom&#39;: &#39;value&#39;} | [optional] 
**delay_between_requests** | **float** | Delay in seconds between consecutive requests. Useful for polite crawling and avoiding rate limits. Default: 0 (no delay). | [optional] [default to 0.0]
**target_segment_duration_ms** | **int** | Target duration for video segments in milliseconds. | [optional] [default to 120000]
**min_segment_duration_ms** | **int** | Minimum duration for video segments in milliseconds. | [optional] [default to 30000]
**segmentation_method** | **str** | Video segmentation method: &#39;scene&#39;, &#39;srt&#39;, or &#39;time&#39;. | [optional] [default to 'scene']
**use_whisper_asr** | **bool** | Use Whisper ASR for transcription instead of SRT subtitles. | [optional] [default to True]
**expand_to_granular_docs** | **bool** | Expand each segment into multiple granular documents. | [optional] [default to True]
**ocr_frames_per_segment** | **int** | Number of frames to OCR per video segment. | [optional] [default to 3]
**pdf_extraction_mode** | **str** | How to extract PDF content: &#39;per_page&#39; or &#39;per_element&#39;. | [optional] [default to 'per_element']
**pdf_render_dpi** | **int** | DPI for rendering PDF pages/elements as images. | [optional] [default to 150]
**detect_code_in_pdf** | **bool** | Whether to detect code blocks in PDF text. | [optional] [default to True]
**segment_functions** | **bool** | Whether to segment code files into individual functions. | [optional] [default to True]
**supported_languages** | **List[str]** | Programming languages to extract from code archives. | [optional] 
**run_code_embedding** | **bool** | Generate Jina Code embeddings (768D) for code snippets. | [optional] [default to True]
**run_visual_embedding** | **bool** | Generate SigLIP visual embeddings (768D) for video frames. | [optional] [default to False]
**visual_embedding_use_case** | **str** | Content type preset for visual embedding strategy. | [optional] [default to 'lecture']
**extract_screen_text** | **bool** | Run OCR on video frames to extract on-screen text. | [optional] [default to True]
**enrich_with_llm** | **bool** | Use Gemini to generate summaries and enhance descriptions. | [optional] [default to False]
**llm_prompt** | **str** | Prompt for LLM enrichment when enrich_with_llm&#x3D;True. | [optional] [default to 'Summarize this educational content segment, highlighting key concepts.']

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


