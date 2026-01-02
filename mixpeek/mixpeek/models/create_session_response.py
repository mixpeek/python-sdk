from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.session_status import SessionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSessionResponse")


@_attrs_define
class CreateSessionResponse:
    """Response for session creation.

    Attributes:
        session_id: Unique session identifier
        namespace_id: Namespace identifier
        internal_id: Organization internal ID
        session_name: Auto-generated session name (null until first message)
        status: Session status
        created_at: Session creation timestamp
        expires_at: Session expiration timestamp

    Example:
        ```python
        response = CreateSessionResponse(
            session_id="ses_abc123",
            namespace_id="ns_xyz789",
            internal_id="int_abc123",
            session_name=None,  # Will be set after first message
            status="active",
            created_at=datetime.utcnow(),
            expires_at=datetime.utcnow() + timedelta(days=7)
        )
        ```

        Attributes:
            session_id (str): Unique session identifier
            namespace_id (str): Namespace identifier
            internal_id (str): Organization internal ID
            status (SessionStatus): Session lifecycle states.

                Attributes:
                    ACTIVE: Session is actively processing messages
                    IDLE: Session exists but no recent activity
                    ARCHIVED: Session archived (read-only)
                    TERMINATED: Session permanently closed
            created_at (datetime.datetime): Session creation timestamp
            expires_at (datetime.datetime): Session expiration timestamp
            session_name (None | str | Unset): Auto-generated session name based on first conversation (set after first
                message)
    """

    session_id: str
    namespace_id: str
    internal_id: str
    status: SessionStatus
    created_at: datetime.datetime
    expires_at: datetime.datetime
    session_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        namespace_id = self.namespace_id

        internal_id = self.internal_id

        status = self.status.value

        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        session_name: None | str | Unset
        if isinstance(self.session_name, Unset):
            session_name = UNSET
        else:
            session_name = self.session_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_id": session_id,
                "namespace_id": namespace_id,
                "internal_id": internal_id,
                "status": status,
                "created_at": created_at,
                "expires_at": expires_at,
            }
        )
        if session_name is not UNSET:
            field_dict["session_name"] = session_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("session_id")

        namespace_id = d.pop("namespace_id")

        internal_id = d.pop("internal_id")

        status = SessionStatus(d.pop("status"))

        created_at = isoparse(d.pop("created_at"))

        expires_at = isoparse(d.pop("expires_at"))

        def _parse_session_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_name = _parse_session_name(d.pop("session_name", UNSET))

        create_session_response = cls(
            session_id=session_id,
            namespace_id=namespace_id,
            internal_id=internal_id,
            status=status,
            created_at=created_at,
            expires_at=expires_at,
            session_name=session_name,
        )

        create_session_response.additional_properties = d
        return create_session_response

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
