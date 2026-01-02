from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.taxonomy_execution_mode import TaxonomyExecutionMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logical_operator import LogicalOperator


T = TypeVar("T", bound="TaxonomyApplicationConfig")


@_attrs_define
class TaxonomyApplicationConfig:
    """Configuration block that attaches a taxonomy to a collection.

    Attributes:
        taxonomy_id (str): ID of the `TaxonomyModel` to execute.
        execution_mode (TaxonomyExecutionMode | Unset): How a taxonomy should be executed when attached to a collection.
        target_collection_id (None | str | Unset): Optional collection to persist results into when `execution_mode` is
            'materialize'. If omitted, the source collection is updated in-place.
        scroll_filters (LogicalOperator | None | Unset): Additional filters applied when scrolling the source collection
            before enrichment.
    """

    taxonomy_id: str
    execution_mode: TaxonomyExecutionMode | Unset = UNSET
    target_collection_id: None | str | Unset = UNSET
    scroll_filters: LogicalOperator | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_operator import LogicalOperator

        taxonomy_id = self.taxonomy_id

        execution_mode: str | Unset = UNSET
        if not isinstance(self.execution_mode, Unset):
            execution_mode = self.execution_mode.value

        target_collection_id: None | str | Unset
        if isinstance(self.target_collection_id, Unset):
            target_collection_id = UNSET
        else:
            target_collection_id = self.target_collection_id

        scroll_filters: dict[str, Any] | None | Unset
        if isinstance(self.scroll_filters, Unset):
            scroll_filters = UNSET
        elif isinstance(self.scroll_filters, LogicalOperator):
            scroll_filters = self.scroll_filters.to_dict()
        else:
            scroll_filters = self.scroll_filters

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "taxonomy_id": taxonomy_id,
            }
        )
        if execution_mode is not UNSET:
            field_dict["execution_mode"] = execution_mode
        if target_collection_id is not UNSET:
            field_dict["target_collection_id"] = target_collection_id
        if scroll_filters is not UNSET:
            field_dict["scroll_filters"] = scroll_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logical_operator import LogicalOperator

        d = dict(src_dict)
        taxonomy_id = d.pop("taxonomy_id")

        _execution_mode = d.pop("execution_mode", UNSET)
        execution_mode: TaxonomyExecutionMode | Unset
        if isinstance(_execution_mode, Unset):
            execution_mode = UNSET
        else:
            execution_mode = TaxonomyExecutionMode(_execution_mode)

        def _parse_target_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_collection_id = _parse_target_collection_id(d.pop("target_collection_id", UNSET))

        def _parse_scroll_filters(data: object) -> LogicalOperator | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scroll_filters_type_0 = LogicalOperator.from_dict(data)

                return scroll_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LogicalOperator | None | Unset, data)

        scroll_filters = _parse_scroll_filters(d.pop("scroll_filters", UNSET))

        taxonomy_application_config = cls(
            taxonomy_id=taxonomy_id,
            execution_mode=execution_mode,
            target_collection_id=target_collection_id,
            scroll_filters=scroll_filters,
        )

        return taxonomy_application_config
