from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_config_headers import WebhookConfigHeaders
    from ..models.webhook_config_payload_template_type_0 import WebhookConfigPayloadTemplateType0


T = TypeVar("T", bound="WebhookConfig")


@_attrs_define
class WebhookConfig:
    """Configuration for webhook notifications.

    Attributes:
        url (str): The URL to which the webhook will be sent.
        headers (WebhookConfigHeaders | Unset): Custom headers to include in the webhook request.
        payload_template (None | Unset | WebhookConfigPayloadTemplateType0): A Jinja2 template for the JSON payload.
        timeout (float | Unset): Request timeout in seconds. Default: 10.0.
    """

    url: str
    headers: WebhookConfigHeaders | Unset = UNSET
    payload_template: None | Unset | WebhookConfigPayloadTemplateType0 = UNSET
    timeout: float | Unset = 10.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_config_payload_template_type_0 import WebhookConfigPayloadTemplateType0

        url = self.url

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        payload_template: dict[str, Any] | None | Unset
        if isinstance(self.payload_template, Unset):
            payload_template = UNSET
        elif isinstance(self.payload_template, WebhookConfigPayloadTemplateType0):
            payload_template = self.payload_template.to_dict()
        else:
            payload_template = self.payload_template

        timeout = self.timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers
        if payload_template is not UNSET:
            field_dict["payload_template"] = payload_template
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_config_headers import WebhookConfigHeaders
        from ..models.webhook_config_payload_template_type_0 import WebhookConfigPayloadTemplateType0

        d = dict(src_dict)
        url = d.pop("url")

        _headers = d.pop("headers", UNSET)
        headers: WebhookConfigHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = WebhookConfigHeaders.from_dict(_headers)

        def _parse_payload_template(data: object) -> None | Unset | WebhookConfigPayloadTemplateType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_template_type_0 = WebhookConfigPayloadTemplateType0.from_dict(data)

                return payload_template_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WebhookConfigPayloadTemplateType0, data)

        payload_template = _parse_payload_template(d.pop("payload_template", UNSET))

        timeout = d.pop("timeout", UNSET)

        webhook_config = cls(
            url=url,
            headers=headers,
            payload_template=payload_template,
            timeout=timeout,
        )

        webhook_config.additional_properties = d
        return webhook_config

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
