from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditEventResponse")


@_attrs_define
class AuditEventResponse:
    """Single audit event in list response.

    Attributes:
        audit_id (str): Unique audit event identifier
        timestamp (Any): When the event occurred
        resource_type (str): Type of resource affected
        resource_id (str): ID of the affected resource
        action (str): Action performed
        actor_id (str): Who performed the action
        actor_type (str | Unset): Type of actor Default: 'user'.
        status (str | Unset): Status of the action Default: 'success'.
        changes (Any | Unset): What changed
        ip_address (None | str | Unset): Request IP address
        user_agent (None | str | Unset): Request user agent
    """

    audit_id: str
    timestamp: Any
    resource_type: str
    resource_id: str
    action: str
    actor_id: str
    actor_type: str | Unset = "user"
    status: str | Unset = "success"
    changes: Any | Unset = UNSET
    ip_address: None | str | Unset = UNSET
    user_agent: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audit_id = self.audit_id

        timestamp = self.timestamp

        resource_type = self.resource_type

        resource_id = self.resource_id

        action = self.action

        actor_id = self.actor_id

        actor_type = self.actor_type

        status = self.status

        changes = self.changes

        ip_address: None | str | Unset
        if isinstance(self.ip_address, Unset):
            ip_address = UNSET
        else:
            ip_address = self.ip_address

        user_agent: None | str | Unset
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audit_id": audit_id,
                "timestamp": timestamp,
                "resource_type": resource_type,
                "resource_id": resource_id,
                "action": action,
                "actor_id": actor_id,
            }
        )
        if actor_type is not UNSET:
            field_dict["actor_type"] = actor_type
        if status is not UNSET:
            field_dict["status"] = status
        if changes is not UNSET:
            field_dict["changes"] = changes
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audit_id = d.pop("audit_id")

        timestamp = d.pop("timestamp")

        resource_type = d.pop("resource_type")

        resource_id = d.pop("resource_id")

        action = d.pop("action")

        actor_id = d.pop("actor_id")

        actor_type = d.pop("actor_type", UNSET)

        status = d.pop("status", UNSET)

        changes = d.pop("changes", UNSET)

        def _parse_ip_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_address = _parse_ip_address(d.pop("ip_address", UNSET))

        def _parse_user_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_agent = _parse_user_agent(d.pop("user_agent", UNSET))

        audit_event_response = cls(
            audit_id=audit_id,
            timestamp=timestamp,
            resource_type=resource_type,
            resource_id=resource_id,
            action=action,
            actor_id=actor_id,
            actor_type=actor_type,
            status=status,
            changes=changes,
            ip_address=ip_address,
            user_agent=user_agent,
        )

        audit_event_response.additional_properties = d
        return audit_event_response

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
