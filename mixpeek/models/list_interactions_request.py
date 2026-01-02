from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logical_operator import LogicalOperator
    from ..models.sort_option import SortOption


T = TypeVar("T", bound="ListInteractionsRequest")


@_attrs_define
class ListInteractionsRequest:
    """Request for listing interactions with filters.

    Supports both simple field filters (for common queries) and advanced
    LogicalOperator filters (for complex analytics). This hybrid approach
    follows the same pattern as the Tasks module.

    Common Queries (Simple Fields):
        - Filter by execution: {"execution_id": "exec_abc"}
        - Filter by session: {"session_id": "sess_xyz"}
        - Filter by user: {"user_id": "user_123"}

    Advanced Queries (LogicalOperator):
        - Range queries: {"filters": {"position": {"lte": 5}}}
        - Complex logic: {"filters": {"AND": [...]}}
        - Time ranges: {"filters": {"created_at": {"gte": "2025-01-01"}}}

        Attributes:
            execution_id (None | str | Unset): Filter by retriever execution ID. Most common query: find all interactions
                from a specific search execution. Example: 'exec_abc123'
            retriever_id (None | str | Unset): Filter by retriever ID. Compare performance across different retriever
                configurations. Example: 'ret_product_search_v2'
            session_id (None | str | Unset): Filter by session ID. Track user journey across multiple searches within a
                session. Example: 'sess_xyz789'
            user_id (None | str | Unset): Filter by user ID. Analyze behavior of specific users for personalization
                insights. Example: 'user_456'
            feature_id (None | str | Unset): Filter by feature/document ID. Find all interactions with a specific document
                across all searches. Example: 'doc_abc123'
            interaction_type (None | str | Unset): Filter by interaction type. Use to find specific behaviors like clicks,
                purchases, or feedback. Example: 'click', 'positive_feedback'
            filters (LogicalOperator | None | Unset): Advanced filters using LogicalOperator for complex analytics queries.
                Supports shorthand syntax and complex AND/OR/NOT logic. Use this for: range queries, complex conditions,
                metadata filtering. Examples:   - Position range: {'position': {'lte': 5}}   - Time range: {'timestamp': {'gte':
                '2025-01-01'}}   - Complex: {'AND': [{'field': 'position', 'operator': 'lte', 'value': 5},
                {'field': 'interaction_type', 'operator': 'in', 'value': ['click', 'purchase']}]} See LogicalOperator
                documentation for full syntax.
            sort (None | SortOption | Unset): Sort options for ordering results. Default: timestamp descending (newest
                first). Examples:   - Sort by timestamp: {'field': 'timestamp', 'direction': 'desc'}   - Sort by position:
                {'field': 'position', 'direction': 'asc'}
            search (None | str | Unset): Full-text search across metadata fields. NOT REQUIRED. Use to search interaction
                metadata content.
    """

    execution_id: None | str | Unset = UNSET
    retriever_id: None | str | Unset = UNSET
    session_id: None | str | Unset = UNSET
    user_id: None | str | Unset = UNSET
    feature_id: None | str | Unset = UNSET
    interaction_type: None | str | Unset = UNSET
    filters: LogicalOperator | None | Unset = UNSET
    sort: None | SortOption | Unset = UNSET
    search: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_operator import LogicalOperator
        from ..models.sort_option import SortOption

        execution_id: None | str | Unset
        if isinstance(self.execution_id, Unset):
            execution_id = UNSET
        else:
            execution_id = self.execution_id

        retriever_id: None | str | Unset
        if isinstance(self.retriever_id, Unset):
            retriever_id = UNSET
        else:
            retriever_id = self.retriever_id

        session_id: None | str | Unset
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        feature_id: None | str | Unset
        if isinstance(self.feature_id, Unset):
            feature_id = UNSET
        else:
            feature_id = self.feature_id

        interaction_type: None | str | Unset
        if isinstance(self.interaction_type, Unset):
            interaction_type = UNSET
        else:
            interaction_type = self.interaction_type

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, LogicalOperator):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        sort: dict[str, Any] | None | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        elif isinstance(self.sort, SortOption):
            sort = self.sort.to_dict()
        else:
            sort = self.sort

        search: None | str | Unset
        if isinstance(self.search, Unset):
            search = UNSET
        else:
            search = self.search

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_id is not UNSET:
            field_dict["execution_id"] = execution_id
        if retriever_id is not UNSET:
            field_dict["retriever_id"] = retriever_id
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if feature_id is not UNSET:
            field_dict["feature_id"] = feature_id
        if interaction_type is not UNSET:
            field_dict["interaction_type"] = interaction_type
        if filters is not UNSET:
            field_dict["filters"] = filters
        if sort is not UNSET:
            field_dict["sort"] = sort
        if search is not UNSET:
            field_dict["search"] = search

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logical_operator import LogicalOperator
        from ..models.sort_option import SortOption

        d = dict(src_dict)

        def _parse_execution_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        execution_id = _parse_execution_id(d.pop("execution_id", UNSET))

        def _parse_retriever_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retriever_id = _parse_retriever_id(d.pop("retriever_id", UNSET))

        def _parse_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_id = _parse_session_id(d.pop("session_id", UNSET))

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_feature_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feature_id = _parse_feature_id(d.pop("feature_id", UNSET))

        def _parse_interaction_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        interaction_type = _parse_interaction_type(d.pop("interaction_type", UNSET))

        def _parse_filters(data: object) -> LogicalOperator | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = LogicalOperator.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LogicalOperator | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_sort(data: object) -> None | SortOption | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sort_type_0 = SortOption.from_dict(data)

                return sort_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SortOption | Unset, data)

        sort = _parse_sort(d.pop("sort", UNSET))

        def _parse_search(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search = _parse_search(d.pop("search", UNSET))

        list_interactions_request = cls(
            execution_id=execution_id,
            retriever_id=retriever_id,
            session_id=session_id,
            user_id=user_id,
            feature_id=feature_id,
            interaction_type=interaction_type,
            filters=filters,
            sort=sort,
            search=search,
        )

        list_interactions_request.additional_properties = d
        return list_interactions_request

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
