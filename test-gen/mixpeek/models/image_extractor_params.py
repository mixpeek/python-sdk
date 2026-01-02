from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageExtractorParams")


@_attrs_define
class ImageExtractorParams:
    """Parameters for the Image Extractor.

    The Image Extractor processes images to generate dense vector embeddings
    using Google's SigLIP (Sigmoid Language-Image Pre-training) model.

    **When to Use**:
        - Image search and similarity matching
        - Visual content discovery and recommendations
        - Image clustering and organization
        - Cross-modal search (find images from text queries via SigLIP text encoder)
        - E-commerce product image search
        - Stock photo/media library search

    **When NOT to Use**:
        - Face recognition (use face_identity_extractor instead)
        - Video content (use multimodal_extractor instead)
        - Text-heavy images requiring OCR (use multimodal_extractor with OCR enabled)

    **Model Details**:
        - Model: google/siglip-base-patch16-224
        - Embedding dimensions: 768
        - Input resolution: 224x224
        - Training: Sigmoid loss (improved over CLIP's contrastive loss)

    **Performance**:
        - Processing time: ~50-100ms per image
        - Batch processing: Up to 24 images per batch
        - GPU accelerated inference

        Attributes:
            extractor_type (Literal['image_extractor'] | Unset): Discriminator field for parameter type identification. Must
                be 'image_extractor'. Default: 'image_extractor'.
            enable_thumbnails (bool | Unset): Whether to generate thumbnail images. Thumbnails are resized/optimized
                versions uploaded to S3. Useful for UI previews and reducing bandwidth. Default: True.
            use_cdn (bool | Unset): Whether to use CloudFront CDN for thumbnail delivery. When True: Uploads to public
                bucket with CloudFront URLs. When False: Uses private bucket with presigned URLs. Default: False.
    """

    extractor_type: Literal["image_extractor"] | Unset = "image_extractor"
    enable_thumbnails: bool | Unset = True
    use_cdn: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extractor_type = self.extractor_type

        enable_thumbnails = self.enable_thumbnails

        use_cdn = self.use_cdn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extractor_type is not UNSET:
            field_dict["extractor_type"] = extractor_type
        if enable_thumbnails is not UNSET:
            field_dict["enable_thumbnails"] = enable_thumbnails
        if use_cdn is not UNSET:
            field_dict["use_cdn"] = use_cdn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        extractor_type = cast(Literal["image_extractor"] | Unset, d.pop("extractor_type", UNSET))
        if extractor_type != "image_extractor" and not isinstance(extractor_type, Unset):
            raise ValueError(f"extractor_type must match const 'image_extractor', got '{extractor_type}'")

        enable_thumbnails = d.pop("enable_thumbnails", UNSET)

        use_cdn = d.pop("use_cdn", UNSET)

        image_extractor_params = cls(
            extractor_type=extractor_type,
            enable_thumbnails=enable_thumbnails,
            use_cdn=use_cdn,
        )

        image_extractor_params.additional_properties = d
        return image_extractor_params

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
