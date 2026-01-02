from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.trigger_execution_history_item import TriggerExecutionHistoryItem


T = TypeVar("T", bound="TriggerHistoryResponse")


@_attrs_define
class TriggerHistoryResponse:
    """Response for trigger execution history.

    Attributes:
        trigger_id (str): Trigger ID
        executions (list[TriggerExecutionHistoryItem]): Execution history
        total (int): Total executions
        offset (int): Current offset
        limit (int): Current limit
    """

    trigger_id: str
    executions: list[TriggerExecutionHistoryItem]
    total: int
    offset: int
    limit: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger_id = self.trigger_id

        executions = []
        for executions_item_data in self.executions:
            executions_item = executions_item_data.to_dict()
            executions.append(executions_item)

        total = self.total

        offset = self.offset

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trigger_id": trigger_id,
                "executions": executions,
                "total": total,
                "offset": offset,
                "limit": limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_execution_history_item import TriggerExecutionHistoryItem

        d = dict(src_dict)
        trigger_id = d.pop("trigger_id")

        executions = []
        _executions = d.pop("executions")
        for executions_item_data in _executions:
            executions_item = TriggerExecutionHistoryItem.from_dict(executions_item_data)

            executions.append(executions_item)

        total = d.pop("total")

        offset = d.pop("offset")

        limit = d.pop("limit")

        trigger_history_response = cls(
            trigger_id=trigger_id,
            executions=executions,
            total=total,
            offset=offset,
            limit=limit,
        )

        trigger_history_response.additional_properties = d
        return trigger_history_response

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
