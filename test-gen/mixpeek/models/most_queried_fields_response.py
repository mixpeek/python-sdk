from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.field_query_metrics import FieldQueryMetrics


T = TypeVar("T", bound="MostQueriedFieldsResponse")


@_attrs_define
class MostQueriedFieldsResponse:
    """Response for most queried fields endpoint.

    Attributes:
        namespace_id (str): Namespace ID analyzed
        time_range_days (int): Number of days analyzed
        fields (list[FieldQueryMetrics]): Most queried fields
        total_fields (int): Total unique fields found
    """

    namespace_id: str
    time_range_days: int
    fields: list[FieldQueryMetrics]
    total_fields: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace_id = self.namespace_id

        time_range_days = self.time_range_days

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        total_fields = self.total_fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace_id": namespace_id,
                "time_range_days": time_range_days,
                "fields": fields,
                "total_fields": total_fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_query_metrics import FieldQueryMetrics

        d = dict(src_dict)
        namespace_id = d.pop("namespace_id")

        time_range_days = d.pop("time_range_days")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = FieldQueryMetrics.from_dict(fields_item_data)

            fields.append(fields_item)

        total_fields = d.pop("total_fields")

        most_queried_fields_response = cls(
            namespace_id=namespace_id,
            time_range_days=time_range_days,
            fields=fields,
            total_fields=total_fields,
        )

        most_queried_fields_response.additional_properties = d
        return most_queried_fields_response

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
