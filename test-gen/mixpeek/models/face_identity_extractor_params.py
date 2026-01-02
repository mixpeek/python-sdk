from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.face_identity_extractor_params_detection_model import FaceIdentityExtractorParamsDetectionModel
from ..models.face_identity_extractor_params_output_mode import FaceIdentityExtractorParamsOutputMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="FaceIdentityExtractorParams")


@_attrs_define
class FaceIdentityExtractorParams:
    """Parameters for the Face Identity Extractor.

    The Face Identity Extractor processes images or video frames to detect, align,
    and embed faces using production-grade SOTA models (SCRFD + ArcFace).

    Core Pipeline:
    1. SCRFD Detection → Bounding boxes + 5 landmarks
    2. 5-Point Affine Alignment → 112×112 canonical face
    3. ArcFace Embedding → 512-d L2-normalized vector
    4. Optional Quality Scoring → Filter low-quality faces

    Use Cases:
        - Face verification (1:1 matching)
        - Face identification (1:N search)
        - Face clustering (group photos by person)
        - Duplicate face detection

        Attributes:
            extractor_type (Literal['face_identity_extractor'] | Unset): Discriminator field for parameter type
                identification. Must be 'face_identity_extractor'. Default: 'face_identity_extractor'.
            detection_model (FaceIdentityExtractorParamsDetectionModel | Unset): SCRFD model for face detection.
                'scrfd_500m': Fastest (2-3ms). 'scrfd_2.5g': Balanced (5-7ms), recommended. 'scrfd_10g': Highest accuracy
                (10-15ms). Default: FaceIdentityExtractorParamsDetectionModel.SCRFD_2_5G.
            min_face_size (int | Unset): Minimum face size in pixels to detect. 20px: Balanced. 40px: Higher quality. 10px:
                Maximum recall. Default: 20.
            detection_threshold (float | Unset): Confidence threshold for face detection (0.0-1.0). Default: 0.5.
            max_faces_per_image (int | None | Unset): Maximum number of faces to process per image. None: Process all.
            normalize_embeddings (bool | Unset): L2-normalize embeddings to unit vectors (recommended). Default: True.
            enable_quality_scoring (bool | Unset): Compute quality scores (blur, size, landmarks). Adds ~5ms per face.
                Default: True.
            quality_threshold (float | None | Unset): Minimum quality score to index faces. None: Index all faces. 0.5:
                Moderate filtering. 0.7: High quality only.
            max_video_length (int | Unset): Maximum video length in seconds. 60: Default. 10: Recommended for retrieval.
                300: Maximum (extraction only). Default: 60.
            video_sampling_fps (float | None | Unset): Frames per second to sample from video. 1.0: One frame per second
                (recommended). Default: 1.0.
            video_deduplication (bool | Unset): Remove duplicate faces across video frames (extraction only). Reduces 90-95%
                redundancy. NOT used in retrieval. Default: True.
            video_deduplication_threshold (float | Unset): Cosine similarity threshold for deduplication. 0.8: Conservative
                (default). Default: 0.8.
            output_mode (FaceIdentityExtractorParamsOutputMode | Unset): 'per_face': One document per face (recommended).
                'per_image': One doc per image with faces array. Default: FaceIdentityExtractorParamsOutputMode.PER_FACE.
            include_face_crops (bool | Unset): Include aligned 112×112 face crops as base64. Adds ~5KB per face. Default:
                False.
            store_detection_metadata (bool | Unset): Store bbox, landmarks, detection scores. Recommended for debugging.
                Default: True.
    """

    extractor_type: Literal["face_identity_extractor"] | Unset = "face_identity_extractor"
    detection_model: FaceIdentityExtractorParamsDetectionModel | Unset = (
        FaceIdentityExtractorParamsDetectionModel.SCRFD_2_5G
    )
    min_face_size: int | Unset = 20
    detection_threshold: float | Unset = 0.5
    max_faces_per_image: int | None | Unset = UNSET
    normalize_embeddings: bool | Unset = True
    enable_quality_scoring: bool | Unset = True
    quality_threshold: float | None | Unset = UNSET
    max_video_length: int | Unset = 60
    video_sampling_fps: float | None | Unset = 1.0
    video_deduplication: bool | Unset = True
    video_deduplication_threshold: float | Unset = 0.8
    output_mode: FaceIdentityExtractorParamsOutputMode | Unset = FaceIdentityExtractorParamsOutputMode.PER_FACE
    include_face_crops: bool | Unset = False
    store_detection_metadata: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extractor_type = self.extractor_type

        detection_model: str | Unset = UNSET
        if not isinstance(self.detection_model, Unset):
            detection_model = self.detection_model.value

        min_face_size = self.min_face_size

        detection_threshold = self.detection_threshold

        max_faces_per_image: int | None | Unset
        if isinstance(self.max_faces_per_image, Unset):
            max_faces_per_image = UNSET
        else:
            max_faces_per_image = self.max_faces_per_image

        normalize_embeddings = self.normalize_embeddings

        enable_quality_scoring = self.enable_quality_scoring

        quality_threshold: float | None | Unset
        if isinstance(self.quality_threshold, Unset):
            quality_threshold = UNSET
        else:
            quality_threshold = self.quality_threshold

        max_video_length = self.max_video_length

        video_sampling_fps: float | None | Unset
        if isinstance(self.video_sampling_fps, Unset):
            video_sampling_fps = UNSET
        else:
            video_sampling_fps = self.video_sampling_fps

        video_deduplication = self.video_deduplication

        video_deduplication_threshold = self.video_deduplication_threshold

        output_mode: str | Unset = UNSET
        if not isinstance(self.output_mode, Unset):
            output_mode = self.output_mode.value

        include_face_crops = self.include_face_crops

        store_detection_metadata = self.store_detection_metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extractor_type is not UNSET:
            field_dict["extractor_type"] = extractor_type
        if detection_model is not UNSET:
            field_dict["detection_model"] = detection_model
        if min_face_size is not UNSET:
            field_dict["min_face_size"] = min_face_size
        if detection_threshold is not UNSET:
            field_dict["detection_threshold"] = detection_threshold
        if max_faces_per_image is not UNSET:
            field_dict["max_faces_per_image"] = max_faces_per_image
        if normalize_embeddings is not UNSET:
            field_dict["normalize_embeddings"] = normalize_embeddings
        if enable_quality_scoring is not UNSET:
            field_dict["enable_quality_scoring"] = enable_quality_scoring
        if quality_threshold is not UNSET:
            field_dict["quality_threshold"] = quality_threshold
        if max_video_length is not UNSET:
            field_dict["max_video_length"] = max_video_length
        if video_sampling_fps is not UNSET:
            field_dict["video_sampling_fps"] = video_sampling_fps
        if video_deduplication is not UNSET:
            field_dict["video_deduplication"] = video_deduplication
        if video_deduplication_threshold is not UNSET:
            field_dict["video_deduplication_threshold"] = video_deduplication_threshold
        if output_mode is not UNSET:
            field_dict["output_mode"] = output_mode
        if include_face_crops is not UNSET:
            field_dict["include_face_crops"] = include_face_crops
        if store_detection_metadata is not UNSET:
            field_dict["store_detection_metadata"] = store_detection_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        extractor_type = cast(Literal["face_identity_extractor"] | Unset, d.pop("extractor_type", UNSET))
        if extractor_type != "face_identity_extractor" and not isinstance(extractor_type, Unset):
            raise ValueError(f"extractor_type must match const 'face_identity_extractor', got '{extractor_type}'")

        _detection_model = d.pop("detection_model", UNSET)
        detection_model: FaceIdentityExtractorParamsDetectionModel | Unset
        if isinstance(_detection_model, Unset):
            detection_model = UNSET
        else:
            detection_model = FaceIdentityExtractorParamsDetectionModel(_detection_model)

        min_face_size = d.pop("min_face_size", UNSET)

        detection_threshold = d.pop("detection_threshold", UNSET)

        def _parse_max_faces_per_image(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_faces_per_image = _parse_max_faces_per_image(d.pop("max_faces_per_image", UNSET))

        normalize_embeddings = d.pop("normalize_embeddings", UNSET)

        enable_quality_scoring = d.pop("enable_quality_scoring", UNSET)

        def _parse_quality_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        quality_threshold = _parse_quality_threshold(d.pop("quality_threshold", UNSET))

        max_video_length = d.pop("max_video_length", UNSET)

        def _parse_video_sampling_fps(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        video_sampling_fps = _parse_video_sampling_fps(d.pop("video_sampling_fps", UNSET))

        video_deduplication = d.pop("video_deduplication", UNSET)

        video_deduplication_threshold = d.pop("video_deduplication_threshold", UNSET)

        _output_mode = d.pop("output_mode", UNSET)
        output_mode: FaceIdentityExtractorParamsOutputMode | Unset
        if isinstance(_output_mode, Unset):
            output_mode = UNSET
        else:
            output_mode = FaceIdentityExtractorParamsOutputMode(_output_mode)

        include_face_crops = d.pop("include_face_crops", UNSET)

        store_detection_metadata = d.pop("store_detection_metadata", UNSET)

        face_identity_extractor_params = cls(
            extractor_type=extractor_type,
            detection_model=detection_model,
            min_face_size=min_face_size,
            detection_threshold=detection_threshold,
            max_faces_per_image=max_faces_per_image,
            normalize_embeddings=normalize_embeddings,
            enable_quality_scoring=enable_quality_scoring,
            quality_threshold=quality_threshold,
            max_video_length=max_video_length,
            video_sampling_fps=video_sampling_fps,
            video_deduplication=video_deduplication,
            video_deduplication_threshold=video_deduplication_threshold,
            output_mode=output_mode,
            include_face_crops=include_face_crops,
            store_detection_metadata=store_detection_metadata,
        )

        face_identity_extractor_params.additional_properties = d
        return face_identity_extractor_params

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
