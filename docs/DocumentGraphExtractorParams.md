# DocumentGraphExtractorParams

Parameters for the document graph extractor.  This extractor decomposes PDFs into spatial blocks with layout classification, confidence scoring, and optional VLM correction for degraded documents.  **When to Use**:     - Historical/archival document processing (FBI files, old records)     - Scanned documents with mixed quality     - Documents requiring spatial understanding (forms, tables, multi-column)     - When you need block-level granularity with bounding boxes     - When confidence scoring is needed for downstream filtering  **When NOT to Use**:     - Simple text-only documents -> Use text_extractor instead     - When page-level granularity is sufficient -> Use pdf_extractor instead     - Real-time processing requirements -> VLM correction adds latency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractor_type** | **str** | Discriminator field for parameter type identification. Must be &#39;document_graph_extractor&#39;. | [optional] [default to 'document_graph_extractor']
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
from mixpeek.models.document_graph_extractor_params import DocumentGraphExtractorParams

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentGraphExtractorParams from a JSON string
document_graph_extractor_params_instance = DocumentGraphExtractorParams.from_json(json)
# print the JSON string representation of the object
print(DocumentGraphExtractorParams.to_json())

# convert the object into a dict
document_graph_extractor_params_dict = document_graph_extractor_params_instance.to_dict()
# create an instance of DocumentGraphExtractorParams from a dict
document_graph_extractor_params_from_dict = DocumentGraphExtractorParams.from_dict(document_graph_extractor_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


