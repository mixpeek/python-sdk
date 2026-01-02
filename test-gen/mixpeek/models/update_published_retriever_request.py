from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.display_config import DisplayConfig
    from ..models.rate_limit_config import RateLimitConfig


T = TypeVar("T", bound="UpdatePublishedRetrieverRequest")


@_attrs_define
class UpdatePublishedRetrieverRequest:
    """Request to update a published retriever configuration.

    Attributes:
        display_config (DisplayConfig | None | Unset): Update the display configuration
        rate_limit_config (None | RateLimitConfig | Unset): Update rate limiting configuration
        password_secret_name (None | str | Unset): Update or remove password protection (set to empty string to remove)
        is_active (bool | None | Unset): Activate or deactivate the published retriever
    """

    display_config: DisplayConfig | None | Unset = UNSET
    rate_limit_config: None | RateLimitConfig | Unset = UNSET
    password_secret_name: None | str | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.display_config import DisplayConfig
        from ..models.rate_limit_config import RateLimitConfig

        display_config: dict[str, Any] | None | Unset
        if isinstance(self.display_config, Unset):
            display_config = UNSET
        elif isinstance(self.display_config, DisplayConfig):
            display_config = self.display_config.to_dict()
        else:
            display_config = self.display_config

        rate_limit_config: dict[str, Any] | None | Unset
        if isinstance(self.rate_limit_config, Unset):
            rate_limit_config = UNSET
        elif isinstance(self.rate_limit_config, RateLimitConfig):
            rate_limit_config = self.rate_limit_config.to_dict()
        else:
            rate_limit_config = self.rate_limit_config

        password_secret_name: None | str | Unset
        if isinstance(self.password_secret_name, Unset):
            password_secret_name = UNSET
        else:
            password_secret_name = self.password_secret_name

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_config is not UNSET:
            field_dict["display_config"] = display_config
        if rate_limit_config is not UNSET:
            field_dict["rate_limit_config"] = rate_limit_config
        if password_secret_name is not UNSET:
            field_dict["password_secret_name"] = password_secret_name
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.display_config import DisplayConfig
        from ..models.rate_limit_config import RateLimitConfig

        d = dict(src_dict)

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

        def _parse_rate_limit_config(data: object) -> None | RateLimitConfig | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rate_limit_config_type_0 = RateLimitConfig.from_dict(data)

                return rate_limit_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RateLimitConfig | Unset, data)

        rate_limit_config = _parse_rate_limit_config(d.pop("rate_limit_config", UNSET))

        def _parse_password_secret_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password_secret_name = _parse_password_secret_name(d.pop("password_secret_name", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        update_published_retriever_request = cls(
            display_config=display_config,
            rate_limit_config=rate_limit_config,
            password_secret_name=password_secret_name,
            is_active=is_active,
        )

        update_published_retriever_request.additional_properties = d
        return update_published_retriever_request

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
