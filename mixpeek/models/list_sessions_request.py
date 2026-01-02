from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.session_status import SessionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_sessions_request_filters_type_0 import ListSessionsRequestFiltersType0
    from ..models.list_sessions_request_sort_type_0 import ListSessionsRequestSortType0


T = TypeVar("T", bound="ListSessionsRequest")


@_attrs_define
class ListSessionsRequest:
    """Request payload for listing sessions.

    Attributes:
        status: Optional status filter
        filters: Optional additional filters
        sort: Optional sort configuration

    Example:
        ```python
        request = ListSessionsRequest(
            status="active",
            filters={"user_id": "user_123"}
        )
        ```

        Attributes:
            status (None | SessionStatus | Unset): Filter by session status
            filters (ListSessionsRequestFiltersType0 | None | Unset): Additional filters
            sort (ListSessionsRequestSortType0 | None | Unset): Sort configuration
    """

    status: None | SessionStatus | Unset = UNSET
    filters: ListSessionsRequestFiltersType0 | None | Unset = UNSET
    sort: ListSessionsRequestSortType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_sessions_request_filters_type_0 import ListSessionsRequestFiltersType0
        from ..models.list_sessions_request_sort_type_0 import ListSessionsRequestSortType0

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, SessionStatus):
            status = self.status.value
        else:
            status = self.status

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, ListSessionsRequestFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        sort: dict[str, Any] | None | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        elif isinstance(self.sort, ListSessionsRequestSortType0):
            sort = self.sort.to_dict()
        else:
            sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if filters is not UNSET:
            field_dict["filters"] = filters
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_sessions_request_filters_type_0 import ListSessionsRequestFiltersType0
        from ..models.list_sessions_request_sort_type_0 import ListSessionsRequestSortType0

        d = dict(src_dict)

        def _parse_status(data: object) -> None | SessionStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = SessionStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_filters(data: object) -> ListSessionsRequestFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = ListSessionsRequestFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListSessionsRequestFiltersType0 | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_sort(data: object) -> ListSessionsRequestSortType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sort_type_0 = ListSessionsRequestSortType0.from_dict(data)

                return sort_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListSessionsRequestSortType0 | None | Unset, data)

        sort = _parse_sort(d.pop("sort", UNSET))

        list_sessions_request = cls(
            status=status,
            filters=filters,
            sort=sort,
        )

        list_sessions_request.additional_properties = d
        return list_sessions_request

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
