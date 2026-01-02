from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_executions_request_filters_type_0 import ListExecutionsRequestFiltersType0
    from ..models.list_executions_request_sorts_type_0_item import ListExecutionsRequestSortsType0Item


T = TypeVar("T", bound="ListExecutionsRequest")


@_attrs_define
class ListExecutionsRequest:
    """Request to list retriever executions.

    Attributes:
        filters (ListExecutionsRequestFiltersType0 | None | Unset):
        sorts (list[ListExecutionsRequestSortsType0Item] | None | Unset):
        status (None | str | Unset): Optional status filter (completed, failed, running).
    """

    filters: ListExecutionsRequestFiltersType0 | None | Unset = UNSET
    sorts: list[ListExecutionsRequestSortsType0Item] | None | Unset = UNSET
    status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_executions_request_filters_type_0 import ListExecutionsRequestFiltersType0

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, ListExecutionsRequestFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        sorts: list[dict[str, Any]] | None | Unset
        if isinstance(self.sorts, Unset):
            sorts = UNSET
        elif isinstance(self.sorts, list):
            sorts = []
            for sorts_type_0_item_data in self.sorts:
                sorts_type_0_item = sorts_type_0_item_data.to_dict()
                sorts.append(sorts_type_0_item)

        else:
            sorts = self.sorts

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters
        if sorts is not UNSET:
            field_dict["sorts"] = sorts
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_executions_request_filters_type_0 import ListExecutionsRequestFiltersType0
        from ..models.list_executions_request_sorts_type_0_item import ListExecutionsRequestSortsType0Item

        d = dict(src_dict)

        def _parse_filters(data: object) -> ListExecutionsRequestFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = ListExecutionsRequestFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListExecutionsRequestFiltersType0 | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_sorts(data: object) -> list[ListExecutionsRequestSortsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sorts_type_0 = []
                _sorts_type_0 = data
                for sorts_type_0_item_data in _sorts_type_0:
                    sorts_type_0_item = ListExecutionsRequestSortsType0Item.from_dict(sorts_type_0_item_data)

                    sorts_type_0.append(sorts_type_0_item)

                return sorts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ListExecutionsRequestSortsType0Item] | None | Unset, data)

        sorts = _parse_sorts(d.pop("sorts", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        list_executions_request = cls(
            filters=filters,
            sorts=sorts,
            status=status,
        )

        list_executions_request.additional_properties = d
        return list_executions_request

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
