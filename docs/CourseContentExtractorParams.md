# CourseContentExtractorParams

Parameters for the course content extractor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractor_type** | **str** | Discriminator field. Must be &#39;course_content_extractor&#39;. | [optional] [default to 'course_content_extractor']
**target_segment_duration_ms** | **int** | Target duration for video segments in milliseconds. | [optional] [default to 120000]
**min_segment_duration_ms** | **int** | Minimum duration for video segments in milliseconds. | [optional] [default to 30000]
**segmentation_method** | **str** | Video segmentation method: &#39;scene&#39;, &#39;srt&#39;, or &#39;time&#39;. | [optional] [default to 'scene']
**scene_detection_threshold** | **float** | Scene detection sensitivity (0.0-1.0). | [optional] [default to 0.3]
**use_whisper_asr** | **bool** | Use Whisper ASR for transcription instead of SRT subtitles. | [optional] [default to True]
**expand_to_granular_docs** | **bool** | Expand each segment into multiple granular documents. | [optional] [default to True]
**ocr_frames_per_segment** | **int** | Number of frames to OCR per video segment. | [optional] [default to 3]
**pdf_extraction_mode** | **str** | How to extract PDF content: &#39;per_page&#39; or &#39;per_element&#39;. | [optional] [default to 'per_element']
**pdf_render_dpi** | **int** | DPI for rendering PDF pages/elements as images. | [optional] [default to 150]
**detect_code_in_pdf** | **bool** | Whether to detect code blocks in PDF text. | [optional] [default to True]
**segment_functions** | **bool** | Whether to segment code files into individual functions. | [optional] [default to True]
**supported_languages** | **List[str]** | Programming languages to extract from code archives. | [optional] 
**run_text_embedding** | **bool** | Generate E5 text embeddings (1024D) for transcripts and text. | [optional] [default to True]
**run_code_embedding** | **bool** | Generate Jina Code embeddings (768D) for code snippets. | [optional] [default to True]
**run_visual_embedding** | **bool** | Generate SigLIP visual embeddings (768D) for video frames. | [optional] [default to False]
**visual_embedding_use_case** | **str** | Content type preset for visual embedding strategy. | [optional] [default to 'lecture']
**extract_screen_text** | **bool** | Run OCR on video frames to extract on-screen text. | [optional] [default to True]
**generate_thumbnails** | **bool** | Generate thumbnail images for each learning unit. | [optional] [default to True]
**use_cdn** | **bool** | Use CDN for thumbnail delivery. | [optional] [default to False]
**enrich_with_llm** | **bool** | Use Gemini to generate summaries and enhance descriptions. | [optional] [default to False]
**llm_prompt** | **str** | Prompt for LLM enrichment when enrich_with_llm&#x3D;True. | [optional] [default to 'Summarize this educational content segment, highlighting key concepts.']

## Example

```python
from mixpeek.models.course_content_extractor_params import CourseContentExtractorParams

# TODO update the JSON string below
json = "{}"
# create an instance of CourseContentExtractorParams from a JSON string
course_content_extractor_params_instance = CourseContentExtractorParams.from_json(json)
# print the JSON string representation of the object
print(CourseContentExtractorParams.to_json())

# convert the object into a dict
course_content_extractor_params_dict = course_content_extractor_params_instance.to_dict()
# create an instance of CourseContentExtractorParams from a dict
course_content_extractor_params_from_dict = CourseContentExtractorParams.from_dict(course_content_extractor_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


