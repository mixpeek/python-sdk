from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_status import TriggerStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_trigger_request_schedule_config_type_0 import UpdateTriggerRequestScheduleConfigType0


T = TypeVar("T", bound="UpdateTriggerRequest")


@_attrs_define
class UpdateTriggerRequest:
    """Request to update an existing trigger.

    Attributes:
        schedule_config (None | Unset | UpdateTriggerRequestScheduleConfigType0): Updated schedule configuration
        description (None | str | Unset): Updated description
        status (None | TriggerStatus | Unset): Updated status
    """

    schedule_config: None | Unset | UpdateTriggerRequestScheduleConfigType0 = UNSET
    description: None | str | Unset = UNSET
    status: None | TriggerStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_trigger_request_schedule_config_type_0 import UpdateTriggerRequestScheduleConfigType0

        schedule_config: dict[str, Any] | None | Unset
        if isinstance(self.schedule_config, Unset):
            schedule_config = UNSET
        elif isinstance(self.schedule_config, UpdateTriggerRequestScheduleConfigType0):
            schedule_config = self.schedule_config.to_dict()
        else:
            schedule_config = self.schedule_config

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, TriggerStatus):
            status = self.status.value
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule_config is not UNSET:
            field_dict["schedule_config"] = schedule_config
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_trigger_request_schedule_config_type_0 import UpdateTriggerRequestScheduleConfigType0

        d = dict(src_dict)

        def _parse_schedule_config(data: object) -> None | Unset | UpdateTriggerRequestScheduleConfigType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_config_type_0 = UpdateTriggerRequestScheduleConfigType0.from_dict(data)

                return schedule_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateTriggerRequestScheduleConfigType0, data)

        schedule_config = _parse_schedule_config(d.pop("schedule_config", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_status(data: object) -> None | TriggerStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = TriggerStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TriggerStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        update_trigger_request = cls(
            schedule_config=schedule_config,
            description=description,
            status=status,
        )

        update_trigger_request.additional_properties = d
        return update_trigger_request

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
