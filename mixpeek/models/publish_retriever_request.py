from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.display_config import DisplayConfig
    from ..models.rate_limit_config import RateLimitConfig


T = TypeVar("T", bound="PublishRetrieverRequest")


@_attrs_define
class PublishRetrieverRequest:
    """Request to publish a retriever.

    Requires public_name. display_config is optional - if not provided, the retriever's
    stored display_config will be used (if available).

        Attributes:
            public_name (str): Public URL-safe name (lowercase, numbers, hyphens only). Must start and end with alphanumeric
                character. Will be used in URL: apps.mixpeek.com/r/{public_name}
            display_config (DisplayConfig | None | Unset): Display configuration defining how the public UI should be
                rendered. Includes input fields, theme, layout, and exposed result fields. If not provided, uses the retriever's
                stored display_config.
            rate_limit_config (RateLimitConfig | Unset): Rate limiting configuration for public retriever API.

                Controls how many requests can be made to the public endpoint
                to prevent abuse and manage infrastructure costs.

                You can either use a preset tier or specify custom limits.
                If both tier and custom limits are provided, custom limits override the tier defaults.
            password_secret_name (None | str | Unset): OPTIONAL. Name of organization secret containing password for access
                protection. If provided, users must send password via X-Retriever-Password header.
            include_metadata (bool | Unset): Whether to capture and store retriever metadata (stages, collections,
                capabilities). Recommended: True for better developer experience and debugging. Default: True. Default: True.
    """

    public_name: str
    display_config: DisplayConfig | None | Unset = UNSET
    rate_limit_config: RateLimitConfig | Unset = UNSET
    password_secret_name: None | str | Unset = UNSET
    include_metadata: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.display_config import DisplayConfig

        public_name = self.public_name

        display_config: dict[str, Any] | None | Unset
        if isinstance(self.display_config, Unset):
            display_config = UNSET
        elif isinstance(self.display_config, DisplayConfig):
            display_config = self.display_config.to_dict()
        else:
            display_config = self.display_config

        rate_limit_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_limit_config, Unset):
            rate_limit_config = self.rate_limit_config.to_dict()

        password_secret_name: None | str | Unset
        if isinstance(self.password_secret_name, Unset):
            password_secret_name = UNSET
        else:
            password_secret_name = self.password_secret_name

        include_metadata = self.include_metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_name": public_name,
            }
        )
        if display_config is not UNSET:
            field_dict["display_config"] = display_config
        if rate_limit_config is not UNSET:
            field_dict["rate_limit_config"] = rate_limit_config
        if password_secret_name is not UNSET:
            field_dict["password_secret_name"] = password_secret_name
        if include_metadata is not UNSET:
            field_dict["include_metadata"] = include_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.display_config import DisplayConfig
        from ..models.rate_limit_config import RateLimitConfig

        d = dict(src_dict)
        public_name = d.pop("public_name")

        def _parse_display_config(data: object) -> DisplayConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                display_config_type_0 = DisplayConfig.from_dict(data)

                return display_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DisplayConfig | None | Unset, data)

        display_config = _parse_display_config(d.pop("display_config", UNSET))

        _rate_limit_config = d.pop("rate_limit_config", UNSET)
        rate_limit_config: RateLimitConfig | Unset
        if isinstance(_rate_limit_config, Unset):
            rate_limit_config = UNSET
        else:
            rate_limit_config = RateLimitConfig.from_dict(_rate_limit_config)

        def _parse_password_secret_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password_secret_name = _parse_password_secret_name(d.pop("password_secret_name", UNSET))

        include_metadata = d.pop("include_metadata", UNSET)

        publish_retriever_request = cls(
            public_name=public_name,
            display_config=display_config,
            rate_limit_config=rate_limit_config,
            password_secret_name=password_secret_name,
            include_metadata=include_metadata,
        )

        publish_retriever_request.additional_properties = d
        return publish_retriever_request

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
