from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.session_status import SessionStatus

T = TypeVar("T", bound="TerminateSessionResponse")


@_attrs_define
class TerminateSessionResponse:
    """Response for session termination.

    Attributes:
        session_id: Session identifier
        status: New session status (terminated)
        terminated_at: Termination timestamp

        Attributes:
            session_id (str): Session identifier
            status (SessionStatus): Session lifecycle states.

                Attributes:
                    ACTIVE: Session is actively processing messages
                    IDLE: Session exists but no recent activity
                    ARCHIVED: Session archived (read-only)
                    TERMINATED: Session permanently closed
            terminated_at (datetime.datetime): Termination timestamp
    """

    session_id: str
    status: SessionStatus
    terminated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        status = self.status.value

        terminated_at = self.terminated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_id": session_id,
                "status": status,
                "terminated_at": terminated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("session_id")

        status = SessionStatus(d.pop("status"))

        terminated_at = isoparse(d.pop("terminated_at"))

        terminate_session_response = cls(
            session_id=session_id,
            status=status,
            terminated_at=terminated_at,
        )

        terminate_session_response.additional_properties = d
        return terminate_session_response

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
