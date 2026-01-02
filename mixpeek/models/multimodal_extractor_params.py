from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.split_method import SplitMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generation_config import GenerationConfig
    from ..models.multimodal_extractor_params_response_shape_type_1 import MultimodalExtractorParamsResponseShapeType1


T = TypeVar("T", bound="MultimodalExtractorParams")


@_attrs_define
class MultimodalExtractorParams:
    """Parameters for the multimodal extractor.

    The multimodal extractor processes video, audio, image, text, and GIF content in a unified embedding space.
    Videos/GIFs/Audio are decomposed into segments with transcription, visual analysis (video only), OCR, and
    embeddings.
    Images and text are embedded directly without decomposition.

    **When to Use**:
        - Video content libraries requiring searchable segments
        - Audio content (podcasts, lectures, music) requiring transcription and search
        - Media platforms with search across spoken and visual content
        - Educational content with lecture videos and demonstrations
        - Surveillance/security footage requiring event detection
        - Social media platforms with user-generated video content
        - Broadcasting/streaming services with large video catalogs
        - Training video repositories with instructional content
        - Marketing/advertising analytics for video campaigns

    **When NOT to Use**:
        - Static image collections → Use image_extractor instead
        - Very short videos (<5 seconds) → Overhead not worth it
        - Real-time live streams → Use specialized streaming extractors
        - Extremely high-resolution videos (8K+) → Consider downsampling first

    **Decomposition Methods**:

        | Method | Use Case | Accuracy | Segments/Min | Best For |
        |--------|----------|----------|--------------|----------|
        | **TIME** | Fixed intervals | N/A | 60/interval_sec | General purpose, audio/video chunking |
        | **SCENE** | Visual changes | 85-90% | Variable (2-20) | Movies, dynamic content (video only) |
        | **SILENCE** | Audio pauses | 80-85% | Variable (5-30) | Lectures, presentations, audio/video |

    **Feature Extraction Options**:
        - Transcription: Speech-to-text using Whisper (95%+ accuracy)
        - Multimodal Embeddings: Unified embeddings from Vertex AI (1408D) for video/image/gif/text
        - Transcription Embeddings: Text embeddings from E5-Large (1024D)
        - OCR: Text extraction from video frames using Gemini Vision
        - Descriptions: AI-generated segment summaries using Gemini
        - Thumbnails: Visual preview images for each segment

    **Performance Characteristics**:
        - Processing Speed: 0.5-2x realtime (depends on features enabled)
        - Example: 10min video → 5-20 minutes processing time
        - Transcription: ~200ms per second of audio
        - Visual Embedding: ~50ms per segment
        - OCR: ~300ms per segment
        - Description: ~2s per segment (if enabled)

    Requirements:
        - video URL: REQUIRED (accessible video file)
        - All feature parameters: OPTIONAL (defaults provided)

        Attributes:
            extractor_type (Literal['multimodal_extractor'] | Unset): Discriminator field for parameter type identification.
                Must be 'multimodal_extractor'. Default: 'multimodal_extractor'.
            split_method (SplitMethod | Unset): Split methods for video extraction.
            description_prompt (str | Unset): The prompt to use for description generation. Default: 'Describe the video
                segment in detail.'.
            time_split_interval (int | None | Unset): Interval in seconds for 'time' splitting. Used when
                split_method='time'. Default: 10.
            silence_db_threshold (int | None | Unset): The decibel level below which audio is considered silent. Used when
                split_method='silence'. Recommended value: -40 (auto-applied if not specified). Lower values (e.g., -50) detect
                more silence, higher values (e.g., -30) detect less.
            scene_detection_threshold (float | None | Unset): The threshold for scene detection (0.0-1.0). Used when
                split_method='scene'. Recommended value: 0.5 (auto-applied if not specified). Lower values (e.g., 0.3) detect
                more scenes, higher values (e.g., 0.7) detect fewer scenes.
            run_transcription (bool | Unset): Whether to run transcription on video segments. Default: False.
            transcription_language (str | Unset): The language of the transcription. Used when run_transcription is True.
                Default: 'en'.
            run_video_description (bool | Unset): Whether to generate descriptions for video segments. OPTIMIZED: Defaults
                to False as descriptions add 1-2 minutes. Enable only when needed. Default: False.
            run_transcription_embedding (bool | Unset): Whether to generate embeddings for transcriptions. Useful for
                semantic search over spoken content. Default: False.
            run_multimodal_embedding (bool | Unset): Whether to generate multimodal embeddings for all content types
                (video/image/gif/text). Uses Google Vertex AI to create unified 1408D embeddings in a shared semantic space.
                Useful for cross-modal semantic search across all media types. Default: True.
            run_ocr (bool | Unset): Whether to run OCR to extract text from video frames. OPTIMIZED: Defaults to False as
                OCR adds significant processing time. Enable only when text extraction from video is required. Default: False.
            sensitivity (str | Unset): The sensitivity of the scene detection. Default: 'low'.
            enable_thumbnails (bool | Unset): Whether to generate thumbnail images for video segments and images. Thumbnails
                provide visual previews for navigation and UI display. For videos: Extracts a frame from each segment. For
                images: Creates an optimized thumbnail version.  Default: True.
            use_cdn (bool | Unset): Whether to use CloudFront CDN for thumbnail delivery. When True: Uploads to public
                bucket and returns CloudFront URLs. When False (default): Uploads to private bucket with presigned S3 URLs.
                Benefits of CDN: faster global delivery, permanent URLs, reduced bandwidth costs. Requires
                CLOUDFRONT_PUBLIC_DOMAIN to be configured in settings. Only applies when enable_thumbnails=True. Default: False.
            generation_config (GenerationConfig | Unset): Configuration for generative models.
            response_shape (MultimodalExtractorParamsResponseShapeType1 | None | str | Unset): OPTIONAL. Define custom
                structured output using Gemini's JSON mode. NOT REQUIRED - by default, descriptions are stored as plain text.
                When provided, Gemini will extract structured data matching this schema.

                Two modes supported:
                1. Natural language prompt (string): Describe desired output in plain English
                   - Gemini automatically infers JSON schema from your description
                   - Example: 'Extract product names, colors, and aesthetic labels'

                2. Explicit JSON schema (dict): Provide complete JSON schema for output structure
                   - Full control over output structure, types, and constraints
                   - Use response_mime_type='application/json' in generation_config
                   - Example: {'type': 'object', 'properties': {'products': {'type': 'array', ...}}}


                Use when:
                  - Need to extract structured product/entity information from videos
                  - Want consistent, parseable output format (not free-form text)
                  - Require specific fields like visibility_percentage, product categories, etc.
                  - Building e-commerce, fashion, or product discovery applications


                Output fields are automatically added to collection schema and stored in document metadata.
                Note: When using response_shape, set description_prompt to describe the extraction task.
    """

    extractor_type: Literal["multimodal_extractor"] | Unset = "multimodal_extractor"
    split_method: SplitMethod | Unset = UNSET
    description_prompt: str | Unset = "Describe the video segment in detail."
    time_split_interval: int | None | Unset = 10
    silence_db_threshold: int | None | Unset = UNSET
    scene_detection_threshold: float | None | Unset = UNSET
    run_transcription: bool | Unset = False
    transcription_language: str | Unset = "en"
    run_video_description: bool | Unset = False
    run_transcription_embedding: bool | Unset = False
    run_multimodal_embedding: bool | Unset = True
    run_ocr: bool | Unset = False
    sensitivity: str | Unset = "low"
    enable_thumbnails: bool | Unset = True
    use_cdn: bool | Unset = False
    generation_config: GenerationConfig | Unset = UNSET
    response_shape: MultimodalExtractorParamsResponseShapeType1 | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.multimodal_extractor_params_response_shape_type_1 import (
            MultimodalExtractorParamsResponseShapeType1,
        )

        extractor_type = self.extractor_type

        split_method: str | Unset = UNSET
        if not isinstance(self.split_method, Unset):
            split_method = self.split_method.value

        description_prompt = self.description_prompt

        time_split_interval: int | None | Unset
        if isinstance(self.time_split_interval, Unset):
            time_split_interval = UNSET
        else:
            time_split_interval = self.time_split_interval

        silence_db_threshold: int | None | Unset
        if isinstance(self.silence_db_threshold, Unset):
            silence_db_threshold = UNSET
        else:
            silence_db_threshold = self.silence_db_threshold

        scene_detection_threshold: float | None | Unset
        if isinstance(self.scene_detection_threshold, Unset):
            scene_detection_threshold = UNSET
        else:
            scene_detection_threshold = self.scene_detection_threshold

        run_transcription = self.run_transcription

        transcription_language = self.transcription_language

        run_video_description = self.run_video_description

        run_transcription_embedding = self.run_transcription_embedding

        run_multimodal_embedding = self.run_multimodal_embedding

        run_ocr = self.run_ocr

        sensitivity = self.sensitivity

        enable_thumbnails = self.enable_thumbnails

        use_cdn = self.use_cdn

        generation_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.generation_config, Unset):
            generation_config = self.generation_config.to_dict()

        response_shape: dict[str, Any] | None | str | Unset
        if isinstance(self.response_shape, Unset):
            response_shape = UNSET
        elif isinstance(self.response_shape, MultimodalExtractorParamsResponseShapeType1):
            response_shape = self.response_shape.to_dict()
        else:
            response_shape = self.response_shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extractor_type is not UNSET:
            field_dict["extractor_type"] = extractor_type
        if split_method is not UNSET:
            field_dict["split_method"] = split_method
        if description_prompt is not UNSET:
            field_dict["description_prompt"] = description_prompt
        if time_split_interval is not UNSET:
            field_dict["time_split_interval"] = time_split_interval
        if silence_db_threshold is not UNSET:
            field_dict["silence_db_threshold"] = silence_db_threshold
        if scene_detection_threshold is not UNSET:
            field_dict["scene_detection_threshold"] = scene_detection_threshold
        if run_transcription is not UNSET:
            field_dict["run_transcription"] = run_transcription
        if transcription_language is not UNSET:
            field_dict["transcription_language"] = transcription_language
        if run_video_description is not UNSET:
            field_dict["run_video_description"] = run_video_description
        if run_transcription_embedding is not UNSET:
            field_dict["run_transcription_embedding"] = run_transcription_embedding
        if run_multimodal_embedding is not UNSET:
            field_dict["run_multimodal_embedding"] = run_multimodal_embedding
        if run_ocr is not UNSET:
            field_dict["run_ocr"] = run_ocr
        if sensitivity is not UNSET:
            field_dict["sensitivity"] = sensitivity
        if enable_thumbnails is not UNSET:
            field_dict["enable_thumbnails"] = enable_thumbnails
        if use_cdn is not UNSET:
            field_dict["use_cdn"] = use_cdn
        if generation_config is not UNSET:
            field_dict["generation_config"] = generation_config
        if response_shape is not UNSET:
            field_dict["response_shape"] = response_shape

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generation_config import GenerationConfig
        from ..models.multimodal_extractor_params_response_shape_type_1 import (
            MultimodalExtractorParamsResponseShapeType1,
        )

        d = dict(src_dict)
        extractor_type = cast(Literal["multimodal_extractor"] | Unset, d.pop("extractor_type", UNSET))
        if extractor_type != "multimodal_extractor" and not isinstance(extractor_type, Unset):
            raise ValueError(f"extractor_type must match const 'multimodal_extractor', got '{extractor_type}'")

        _split_method = d.pop("split_method", UNSET)
        split_method: SplitMethod | Unset
        if isinstance(_split_method, Unset):
            split_method = UNSET
        else:
            split_method = SplitMethod(_split_method)

        description_prompt = d.pop("description_prompt", UNSET)

        def _parse_time_split_interval(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_split_interval = _parse_time_split_interval(d.pop("time_split_interval", UNSET))

        def _parse_silence_db_threshold(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        silence_db_threshold = _parse_silence_db_threshold(d.pop("silence_db_threshold", UNSET))

        def _parse_scene_detection_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        scene_detection_threshold = _parse_scene_detection_threshold(d.pop("scene_detection_threshold", UNSET))

        run_transcription = d.pop("run_transcription", UNSET)

        transcription_language = d.pop("transcription_language", UNSET)

        run_video_description = d.pop("run_video_description", UNSET)

        run_transcription_embedding = d.pop("run_transcription_embedding", UNSET)

        run_multimodal_embedding = d.pop("run_multimodal_embedding", UNSET)

        run_ocr = d.pop("run_ocr", UNSET)

        sensitivity = d.pop("sensitivity", UNSET)

        enable_thumbnails = d.pop("enable_thumbnails", UNSET)

        use_cdn = d.pop("use_cdn", UNSET)

        _generation_config = d.pop("generation_config", UNSET)
        generation_config: GenerationConfig | Unset
        if isinstance(_generation_config, Unset):
            generation_config = UNSET
        else:
            generation_config = GenerationConfig.from_dict(_generation_config)

        def _parse_response_shape(data: object) -> MultimodalExtractorParamsResponseShapeType1 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_shape_type_1 = MultimodalExtractorParamsResponseShapeType1.from_dict(data)

                return response_shape_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MultimodalExtractorParamsResponseShapeType1 | None | str | Unset, data)

        response_shape = _parse_response_shape(d.pop("response_shape", UNSET))

        multimodal_extractor_params = cls(
            extractor_type=extractor_type,
            split_method=split_method,
            description_prompt=description_prompt,
            time_split_interval=time_split_interval,
            silence_db_threshold=silence_db_threshold,
            scene_detection_threshold=scene_detection_threshold,
            run_transcription=run_transcription,
            transcription_language=transcription_language,
            run_video_description=run_video_description,
            run_transcription_embedding=run_transcription_embedding,
            run_multimodal_embedding=run_multimodal_embedding,
            run_ocr=run_ocr,
            sensitivity=sensitivity,
            enable_thumbnails=enable_thumbnails,
            use_cdn=use_cdn,
            generation_config=generation_config,
            response_shape=response_shape,
        )

        multimodal_extractor_params.additional_properties = d
        return multimodal_extractor_params

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
