from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.field_usage_stat import FieldUsageStat


T = TypeVar("T", bound="FieldUsageResponse")


@_attrs_define
class FieldUsageResponse:
    """Response containing field usage statistics.

    Attributes:
        namespace_id (str): Namespace being analyzed
        period (str): Analysis period (24h, 7d, 30d)
        fields (list[FieldUsageStat]): Field usage statistics
        total_fields (int): Total number of fields found
        indexed_fields (int): Number of indexed fields
        unindexed_fields (int): Number of unindexed fields
    """

    namespace_id: str
    period: str
    fields: list[FieldUsageStat]
    total_fields: int
    indexed_fields: int
    unindexed_fields: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace_id = self.namespace_id

        period = self.period

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        total_fields = self.total_fields

        indexed_fields = self.indexed_fields

        unindexed_fields = self.unindexed_fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace_id": namespace_id,
                "period": period,
                "fields": fields,
                "total_fields": total_fields,
                "indexed_fields": indexed_fields,
                "unindexed_fields": unindexed_fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_usage_stat import FieldUsageStat

        d = dict(src_dict)
        namespace_id = d.pop("namespace_id")

        period = d.pop("period")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = FieldUsageStat.from_dict(fields_item_data)

            fields.append(fields_item)

        total_fields = d.pop("total_fields")

        indexed_fields = d.pop("indexed_fields")

        unindexed_fields = d.pop("unindexed_fields")

        field_usage_response = cls(
            namespace_id=namespace_id,
            period=period,
            fields=fields,
            total_fields=total_fields,
            indexed_fields=indexed_fields,
            unindexed_fields=unindexed_fields,
        )

        field_usage_response.additional_properties = d
        return field_usage_response

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
