from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logical_operator import LogicalOperator
    from ..models.stage_instance_config_parameters import StageInstanceConfigParameters
    from ..models.stage_performance import StagePerformance


T = TypeVar("T", bound="StageInstanceConfig")


@_attrs_define
class StageInstanceConfig:
    """User-provided configuration for a stage instance in a retriever pipeline.

    This model is used when creating a retriever to define the specific
    parameters for each stage.

        Attributes:
            stage_name (str):
            stage_id (None | str | Unset): Stage implementation ID (overrides stage_name for lookups)
            parameters (StageInstanceConfigParameters | Unset): Stage parameters
            pre_filters (LogicalOperator | None | Unset): Filters to apply to the documents *before* this stage is
                executed.These filters are combined with any global retriever filters.
            post_filters (LogicalOperator | None | Unset): Filters to apply to the documents *after* this stage is
                executed.These filters are applied to the results of this stage before passing to the next.
            stats (None | StagePerformance | Unset): Performance statistics for this stage
    """

    stage_name: str
    stage_id: None | str | Unset = UNSET
    parameters: StageInstanceConfigParameters | Unset = UNSET
    pre_filters: LogicalOperator | None | Unset = UNSET
    post_filters: LogicalOperator | None | Unset = UNSET
    stats: None | StagePerformance | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_operator import LogicalOperator
        from ..models.stage_performance import StagePerformance

        stage_name = self.stage_name

        stage_id: None | str | Unset
        if isinstance(self.stage_id, Unset):
            stage_id = UNSET
        else:
            stage_id = self.stage_id

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        pre_filters: dict[str, Any] | None | Unset
        if isinstance(self.pre_filters, Unset):
            pre_filters = UNSET
        elif isinstance(self.pre_filters, LogicalOperator):
            pre_filters = self.pre_filters.to_dict()
        else:
            pre_filters = self.pre_filters

        post_filters: dict[str, Any] | None | Unset
        if isinstance(self.post_filters, Unset):
            post_filters = UNSET
        elif isinstance(self.post_filters, LogicalOperator):
            post_filters = self.post_filters.to_dict()
        else:
            post_filters = self.post_filters

        stats: dict[str, Any] | None | Unset
        if isinstance(self.stats, Unset):
            stats = UNSET
        elif isinstance(self.stats, StagePerformance):
            stats = self.stats.to_dict()
        else:
            stats = self.stats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage_name": stage_name,
            }
        )
        if stage_id is not UNSET:
            field_dict["stage_id"] = stage_id
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if pre_filters is not UNSET:
            field_dict["pre_filters"] = pre_filters
        if post_filters is not UNSET:
            field_dict["post_filters"] = post_filters
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logical_operator import LogicalOperator
        from ..models.stage_instance_config_parameters import StageInstanceConfigParameters
        from ..models.stage_performance import StagePerformance

        d = dict(src_dict)
        stage_name = d.pop("stage_name")

        def _parse_stage_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage_id = _parse_stage_id(d.pop("stage_id", UNSET))

        _parameters = d.pop("parameters", UNSET)
        parameters: StageInstanceConfigParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = StageInstanceConfigParameters.from_dict(_parameters)

        def _parse_pre_filters(data: object) -> LogicalOperator | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pre_filters_type_0 = LogicalOperator.from_dict(data)

                return pre_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LogicalOperator | None | Unset, data)

        pre_filters = _parse_pre_filters(d.pop("pre_filters", UNSET))

        def _parse_post_filters(data: object) -> LogicalOperator | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                post_filters_type_0 = LogicalOperator.from_dict(data)

                return post_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LogicalOperator | None | Unset, data)

        post_filters = _parse_post_filters(d.pop("post_filters", UNSET))

        def _parse_stats(data: object) -> None | StagePerformance | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stats_type_0 = StagePerformance.from_dict(data)

                return stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StagePerformance | Unset, data)

        stats = _parse_stats(d.pop("stats", UNSET))

        stage_instance_config = cls(
            stage_name=stage_name,
            stage_id=stage_id,
            parameters=parameters,
            pre_filters=pre_filters,
            post_filters=post_filters,
            stats=stats,
        )

        stage_instance_config.additional_properties = d
        return stage_instance_config

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
