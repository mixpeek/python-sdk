from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patch_session_request_user_memory import PatchSessionRequestUserMemory


T = TypeVar("T", bound="PatchSessionRequest")


@_attrs_define
class PatchSessionRequest:
    """Request payload for updating session metadata.

    Only user_memory can be updated after session creation.
    To change agent_config or quotas, create a new session.

    Attributes:
        user_memory: Updated user memory/preferences

    Example:
        ```python
        request = PatchSessionRequest(
            user_memory={
                "preferences": {"language": "es", "domain": "science"},
                "learned_context": {"favorite_topics": ["AI", "robotics"]}
            }
        )
        ```

        Attributes:
            user_memory (PatchSessionRequestUserMemory): Updated user memory (REQUIRED)
    """

    user_memory: PatchSessionRequestUserMemory
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_memory = self.user_memory.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_memory": user_memory,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_session_request_user_memory import PatchSessionRequestUserMemory

        d = dict(src_dict)
        user_memory = PatchSessionRequestUserMemory.from_dict(d.pop("user_memory"))

        patch_session_request = cls(
            user_memory=user_memory,
        )

        patch_session_request.additional_properties = d
        return patch_session_request

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
