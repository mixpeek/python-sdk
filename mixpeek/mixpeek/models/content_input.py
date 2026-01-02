from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentInput")


@_attrs_define
class ContentInput:
    """Generic content input for automatic content-type detection.

    Used for URL or base64 inputs where the content type is not known upfront.
    The system will automatically detect the content type (image, video, text, etc.)
    and route to the appropriate feature extractor.

    **IMPORTANT**: Exactly one of `url` or `base64` must be provided (mutually exclusive).

    Use Cases:
        - User provides a URL without specifying content type
        - Client sends base64-encoded content
        - Generic search where query can be any modality

    Requirements:
        - Provide exactly ONE: url OR base64 (mutually exclusive)
        - System performs automatic content type detection
        - Supported content types: images, videos, audio, documents

    Examples:
        URL input:
            ```json
            {"url": "https://example.com/image.jpg"}
            ```

        Base64 image input:
            ```json
            {"base64": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."}
            ```

        Base64 video input:
            ```json
            {"base64": "data:video/mp4;base64,AAAAIGZ0eXBpc2..."}
            ```

        Attributes:
            url (None | str | Unset): OPTIONAL. URL to content for embedding generation. Mutually exclusive with base64 -
                provide exactly one. System will automatically detect content type (image, video, text, etc.) via HTTP HEAD
                request and/or file extension analysis. Supported protocols: HTTP, HTTPS, S3 (for Mixpeek-managed buckets). S3
                URLs must point to the configured AWS_BUCKET. Examples: image URL, video URL, text file URL, S3 object path.
            base64 (None | str | Unset): OPTIONAL. Base64-encoded content for embedding generation. Mutually exclusive with
                url - provide exactly one. Can include data URI scheme (data:mime/type;base64,...) or just base64 string. System
                will automatically detect content type from data URI or by decoding. Supported types: images, videos, audio,
                documents. Maximum size: Limited by your namespace configuration.
    """

    url: None | str | Unset = UNSET
    base64: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        base64: None | str | Unset
        if isinstance(self.base64, Unset):
            base64 = UNSET
        else:
            base64 = self.base64

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if base64 is not UNSET:
            field_dict["base64"] = base64

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_base64(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base64 = _parse_base64(d.pop("base64", UNSET))

        content_input = cls(
            url=url,
            base64=base64,
        )

        content_input.additional_properties = d
        return content_input

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
