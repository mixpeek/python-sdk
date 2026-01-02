from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PublishRetrieverResponse")


@_attrs_define
class PublishRetrieverResponse:
    """Response after successfully publishing a retriever.

    Attributes:
        public_id (str): Public identifier for this published retriever
        retriever_id (str): ID of the underlying retriever
        public_url (str): Full public URL to the retriever page
        short_url (str): Short URL via mxp.co redirect
        public_api_key (str): Public API key for accessing this retriever. IMPORTANT: Save this key - it's needed for
            all API requests. It's safe to share since it's scoped to this retriever only.
    """

    public_id: str
    retriever_id: str
    public_url: str
    short_url: str
    public_api_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_id = self.public_id

        retriever_id = self.retriever_id

        public_url = self.public_url

        short_url = self.short_url

        public_api_key = self.public_api_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_id": public_id,
                "retriever_id": retriever_id,
                "public_url": public_url,
                "short_url": short_url,
                "public_api_key": public_api_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        public_id = d.pop("public_id")

        retriever_id = d.pop("retriever_id")

        public_url = d.pop("public_url")

        short_url = d.pop("short_url")

        public_api_key = d.pop("public_api_key")

        publish_retriever_response = cls(
            public_id=public_id,
            retriever_id=retriever_id,
            public_url=public_url,
            short_url=short_url,
            public_api_key=public_api_key,
        )

        publish_retriever_response.additional_properties = d
        return publish_retriever_response

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
