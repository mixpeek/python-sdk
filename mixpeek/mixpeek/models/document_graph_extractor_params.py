from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentGraphExtractorParams")


@_attrs_define
class DocumentGraphExtractorParams:
    """Parameters for the document graph extractor.

    This extractor decomposes PDFs into spatial blocks with layout classification,
    confidence scoring, and optional VLM correction for degraded documents.

    **When to Use**:
        - Historical/archival document processing (FBI files, old records)
        - Scanned documents with mixed quality
        - Documents requiring spatial understanding (forms, tables, multi-column)
        - When you need block-level granularity with bounding boxes
        - When confidence scoring is needed for downstream filtering

    **When NOT to Use**:
        - Simple text-only documents -> Use text_extractor instead
        - When page-level granularity is sufficient -> Use pdf_extractor instead
        - Real-time processing requirements -> VLM correction adds latency

        Attributes:
            extractor_type (Literal['document_graph_extractor'] | Unset): Discriminator field for parameter type
                identification. Must be 'document_graph_extractor'. Default: 'document_graph_extractor'.
            use_layout_detection (bool | Unset): Enable ML-based layout detection to find ALL document elements (text,
                images, tables, figures). When enabled, uses PaddleOCR to detect and extract both text regions AND non-text
                elements (scanned images, figures, charts) as separate documents. **Recommended for**: Scanned documents, image-
                heavy PDFs, mixed content documents. **When disabled**: Falls back to text-only extraction (faster but misses
                images). Default: True (detects all elements including images). Default: True.
            vertical_threshold (float | Unset): Maximum vertical gap (in points) between lines to be grouped in same block.
                Increase for looser grouping, decrease for tighter blocks. Default 15pt works well for standard documents.
                Default: 15.0.
            horizontal_threshold (float | Unset): Maximum horizontal distance (in points) for overlap detection. Affects
                column detection and block merging. Increase for wider columns, decrease for narrow layouts. Default: 50.0.
            min_text_length (int | Unset): Minimum text length (characters) to keep a block. Blocks with less text are
                filtered out. Helps remove noise and tiny fragments. Default: 20.
            base_confidence (float | Unset): Base confidence score for embedded (native) text. Penalties are subtracted for
                OCR artifacts, encoding issues, etc. Default: 0.85.
            min_confidence_for_vlm (float | Unset): Confidence threshold below which VLM correction is triggered. Blocks
                with confidence < this value get sent to VLM for correction. Only applies when use_vlm_correction=True. Default:
                0.6.
            use_vlm_correction (bool | Unset): Enable VLM (Vision Language Model) correction for low-confidence blocks. Uses
                Gemini/GPT-4V to correct OCR errors by analyzing the page image. Significantly slower (~1 page/sec) but improves
                accuracy for degraded docs. Default: True.
            fast_mode (bool | Unset): Skip VLM correction entirely for maximum throughput (~15 pages/sec). Overrides
                use_vlm_correction. Use when speed is more important than accuracy. Default: False.
            vlm_provider (str | Unset): LLM provider for VLM correction. Options: 'google' (Gemini), 'openai' (GPT-4V),
                'anthropic' (Claude). Google recommended for best vision quality. Default: 'google'.
            vlm_model (str | Unset): Specific model for VLM correction. Examples: 'gemini-2.0-flash', 'gpt-4o',
                'claude-3-5-sonnet'. Default: 'gemini-2.0-flash'.
            run_text_embedding (bool | Unset): Generate text embeddings for semantic search over block content. Uses
                E5-Large (1024-dim) for multilingual support. Default: True.
            render_dpi (int | Unset): DPI for page rendering (used for VLM correction). 72: Fast, lower quality. 150:
                Balanced (recommended). 300: High quality, slower. Default: 150.
            generate_thumbnails (bool | Unset): Generate thumbnail images for blocks. Useful for visual previews and UI
                display. Default: True.
            thumbnail_mode (str | Unset): Thumbnail generation mode. 'full_page': Low-res thumbnail of entire page.
                'segment': Cropped thumbnail of just the block's bounding box. 'both': Generate both types (recommended for
                flexibility). Default: 'both'.
            thumbnail_dpi (int | Unset): DPI for thumbnail generation. Lower DPI = smaller files. 72: Standard web quality.
                36: Very small thumbnails. Default: 72.
    """

    extractor_type: Literal["document_graph_extractor"] | Unset = "document_graph_extractor"
    use_layout_detection: bool | Unset = True
    vertical_threshold: float | Unset = 15.0
    horizontal_threshold: float | Unset = 50.0
    min_text_length: int | Unset = 20
    base_confidence: float | Unset = 0.85
    min_confidence_for_vlm: float | Unset = 0.6
    use_vlm_correction: bool | Unset = True
    fast_mode: bool | Unset = False
    vlm_provider: str | Unset = "google"
    vlm_model: str | Unset = "gemini-2.0-flash"
    run_text_embedding: bool | Unset = True
    render_dpi: int | Unset = 150
    generate_thumbnails: bool | Unset = True
    thumbnail_mode: str | Unset = "both"
    thumbnail_dpi: int | Unset = 72
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extractor_type = self.extractor_type

        use_layout_detection = self.use_layout_detection

        vertical_threshold = self.vertical_threshold

        horizontal_threshold = self.horizontal_threshold

        min_text_length = self.min_text_length

        base_confidence = self.base_confidence

        min_confidence_for_vlm = self.min_confidence_for_vlm

        use_vlm_correction = self.use_vlm_correction

        fast_mode = self.fast_mode

        vlm_provider = self.vlm_provider

        vlm_model = self.vlm_model

        run_text_embedding = self.run_text_embedding

        render_dpi = self.render_dpi

        generate_thumbnails = self.generate_thumbnails

        thumbnail_mode = self.thumbnail_mode

        thumbnail_dpi = self.thumbnail_dpi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extractor_type is not UNSET:
            field_dict["extractor_type"] = extractor_type
        if use_layout_detection is not UNSET:
            field_dict["use_layout_detection"] = use_layout_detection
        if vertical_threshold is not UNSET:
            field_dict["vertical_threshold"] = vertical_threshold
        if horizontal_threshold is not UNSET:
            field_dict["horizontal_threshold"] = horizontal_threshold
        if min_text_length is not UNSET:
            field_dict["min_text_length"] = min_text_length
        if base_confidence is not UNSET:
            field_dict["base_confidence"] = base_confidence
        if min_confidence_for_vlm is not UNSET:
            field_dict["min_confidence_for_vlm"] = min_confidence_for_vlm
        if use_vlm_correction is not UNSET:
            field_dict["use_vlm_correction"] = use_vlm_correction
        if fast_mode is not UNSET:
            field_dict["fast_mode"] = fast_mode
        if vlm_provider is not UNSET:
            field_dict["vlm_provider"] = vlm_provider
        if vlm_model is not UNSET:
            field_dict["vlm_model"] = vlm_model
        if run_text_embedding is not UNSET:
            field_dict["run_text_embedding"] = run_text_embedding
        if render_dpi is not UNSET:
            field_dict["render_dpi"] = render_dpi
        if generate_thumbnails is not UNSET:
            field_dict["generate_thumbnails"] = generate_thumbnails
        if thumbnail_mode is not UNSET:
            field_dict["thumbnail_mode"] = thumbnail_mode
        if thumbnail_dpi is not UNSET:
            field_dict["thumbnail_dpi"] = thumbnail_dpi

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        extractor_type = cast(Literal["document_graph_extractor"] | Unset, d.pop("extractor_type", UNSET))
        if extractor_type != "document_graph_extractor" and not isinstance(extractor_type, Unset):
            raise ValueError(f"extractor_type must match const 'document_graph_extractor', got '{extractor_type}'")

        use_layout_detection = d.pop("use_layout_detection", UNSET)

        vertical_threshold = d.pop("vertical_threshold", UNSET)

        horizontal_threshold = d.pop("horizontal_threshold", UNSET)

        min_text_length = d.pop("min_text_length", UNSET)

        base_confidence = d.pop("base_confidence", UNSET)

        min_confidence_for_vlm = d.pop("min_confidence_for_vlm", UNSET)

        use_vlm_correction = d.pop("use_vlm_correction", UNSET)

        fast_mode = d.pop("fast_mode", UNSET)

        vlm_provider = d.pop("vlm_provider", UNSET)

        vlm_model = d.pop("vlm_model", UNSET)

        run_text_embedding = d.pop("run_text_embedding", UNSET)

        render_dpi = d.pop("render_dpi", UNSET)

        generate_thumbnails = d.pop("generate_thumbnails", UNSET)

        thumbnail_mode = d.pop("thumbnail_mode", UNSET)

        thumbnail_dpi = d.pop("thumbnail_dpi", UNSET)

        document_graph_extractor_params = cls(
            extractor_type=extractor_type,
            use_layout_detection=use_layout_detection,
            vertical_threshold=vertical_threshold,
            horizontal_threshold=horizontal_threshold,
            min_text_length=min_text_length,
            base_confidence=base_confidence,
            min_confidence_for_vlm=min_confidence_for_vlm,
            use_vlm_correction=use_vlm_correction,
            fast_mode=fast_mode,
            vlm_provider=vlm_provider,
            vlm_model=vlm_model,
            run_text_embedding=run_text_embedding,
            render_dpi=render_dpi,
            generate_thumbnails=generate_thumbnails,
            thumbnail_mode=thumbnail_mode,
            thumbnail_dpi=thumbnail_dpi,
        )

        document_graph_extractor_params.additional_properties = d
        return document_graph_extractor_params

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
