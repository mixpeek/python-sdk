from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigureCORSRequest")


@_attrs_define
class ConfigureCORSRequest:
    """Request model for configuring CORS on object storage.

    This allows administrators to configure CORS policies on the object storage
    bucket to enable browser-based uploads using presigned URLs.

        Attributes:
            allowed_origins (list[str]): List of allowed origins for CORS. These are the frontend URLs that will be allowed
                to upload directly to object storage. REQUIRED. Must be valid HTTP/HTTPS URLs. Examples:
                ['http://localhost:8080', 'https://app.example.com']
            allowed_methods (list[str] | None | Unset): HTTP methods to allow for CORS requests. OPTIONAL - defaults to
                ['GET', 'PUT', 'POST', 'HEAD', 'DELETE'] if not provided. Common methods: GET (download), PUT (upload), POST
                (multipart upload), HEAD (metadata check)
            allowed_headers (list[str] | None | Unset): Headers that are allowed in CORS requests. OPTIONAL - defaults to
                ['*'] (allow all headers) if not provided. Use ['*'] for maximum compatibility or specify specific headers.
            expose_headers (list[str] | None | Unset): Headers that browsers are allowed to access in responses. OPTIONAL -
                defaults to ['ETag', 'x-amz-request-id'] if not provided. 'ETag' is particularly important for upload
                confirmation.
            max_age_seconds (int | None | Unset): How long (in seconds) browsers should cache preflight request results.
                OPTIONAL - defaults to 3000 seconds (50 minutes) if not provided. Higher values reduce preflight requests but
                may delay policy updates.
    """

    allowed_origins: list[str]
    allowed_methods: list[str] | None | Unset = UNSET
    allowed_headers: list[str] | None | Unset = UNSET
    expose_headers: list[str] | None | Unset = UNSET
    max_age_seconds: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_origins = self.allowed_origins

        allowed_methods: list[str] | None | Unset
        if isinstance(self.allowed_methods, Unset):
            allowed_methods = UNSET
        elif isinstance(self.allowed_methods, list):
            allowed_methods = self.allowed_methods

        else:
            allowed_methods = self.allowed_methods

        allowed_headers: list[str] | None | Unset
        if isinstance(self.allowed_headers, Unset):
            allowed_headers = UNSET
        elif isinstance(self.allowed_headers, list):
            allowed_headers = self.allowed_headers

        else:
            allowed_headers = self.allowed_headers

        expose_headers: list[str] | None | Unset
        if isinstance(self.expose_headers, Unset):
            expose_headers = UNSET
        elif isinstance(self.expose_headers, list):
            expose_headers = self.expose_headers

        else:
            expose_headers = self.expose_headers

        max_age_seconds: int | None | Unset
        if isinstance(self.max_age_seconds, Unset):
            max_age_seconds = UNSET
        else:
            max_age_seconds = self.max_age_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowed_origins": allowed_origins,
            }
        )
        if allowed_methods is not UNSET:
            field_dict["allowed_methods"] = allowed_methods
        if allowed_headers is not UNSET:
            field_dict["allowed_headers"] = allowed_headers
        if expose_headers is not UNSET:
            field_dict["expose_headers"] = expose_headers
        if max_age_seconds is not UNSET:
            field_dict["max_age_seconds"] = max_age_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_origins = cast(list[str], d.pop("allowed_origins"))

        def _parse_allowed_methods(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_methods_type_0 = cast(list[str], data)

                return allowed_methods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_methods = _parse_allowed_methods(d.pop("allowed_methods", UNSET))

        def _parse_allowed_headers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_headers_type_0 = cast(list[str], data)

                return allowed_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_headers = _parse_allowed_headers(d.pop("allowed_headers", UNSET))

        def _parse_expose_headers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                expose_headers_type_0 = cast(list[str], data)

                return expose_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        expose_headers = _parse_expose_headers(d.pop("expose_headers", UNSET))

        def _parse_max_age_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_age_seconds = _parse_max_age_seconds(d.pop("max_age_seconds", UNSET))

        configure_cors_request = cls(
            allowed_origins=allowed_origins,
            allowed_methods=allowed_methods,
            allowed_headers=allowed_headers,
            expose_headers=expose_headers,
            max_age_seconds=max_age_seconds,
        )

        configure_cors_request.additional_properties = d
        return configure_cors_request

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
