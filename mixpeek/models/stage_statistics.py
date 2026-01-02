from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stage_statistics_metadata import StageStatisticsMetadata


T = TypeVar("T", bound="StageStatistics")


@_attrs_define
class StageStatistics:
    """Execution metrics for a single stage in a retriever execution run.

    Attributes:
        input_count (int): Number of documents received by the stage (REQUIRED).
        output_count (int): Number of documents emitted by the stage (REQUIRED).
        duration_ms (float): Wall-clock duration in milliseconds (REQUIRED).
        efficiency (float): Output/Input ratio. 0 when input_count is 0 (REQUIRED).
        cache_hit (bool | None | Unset): Indicates whether the result originated from stage cache (OPTIONAL).
        error (None | str | Unset): Stage-specific error message if execution failed but retriever execution continued
            (OPTIONAL).
        llm_calls (int | None | Unset): Number of LLM invocations performed by the stage (OPTIONAL).
        tokens_used (int | None | Unset): Total tokens consumed by the stage (OPTIONAL, only for LLM stages).
        metadata (StageStatisticsMetadata | Unset): Stage-specific metadata containing additional execution details
            (OPTIONAL). For example, join stages include: join_strategy, join_type, matched_count, match_rate, etc. LLM
            stages may include: model_name, temperature, max_tokens, etc.
    """

    input_count: int
    output_count: int
    duration_ms: float
    efficiency: float
    cache_hit: bool | None | Unset = UNSET
    error: None | str | Unset = UNSET
    llm_calls: int | None | Unset = UNSET
    tokens_used: int | None | Unset = UNSET
    metadata: StageStatisticsMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_count = self.input_count

        output_count = self.output_count

        duration_ms = self.duration_ms

        efficiency = self.efficiency

        cache_hit: bool | None | Unset
        if isinstance(self.cache_hit, Unset):
            cache_hit = UNSET
        else:
            cache_hit = self.cache_hit

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        llm_calls: int | None | Unset
        if isinstance(self.llm_calls, Unset):
            llm_calls = UNSET
        else:
            llm_calls = self.llm_calls

        tokens_used: int | None | Unset
        if isinstance(self.tokens_used, Unset):
            tokens_used = UNSET
        else:
            tokens_used = self.tokens_used

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input_count": input_count,
                "output_count": output_count,
                "duration_ms": duration_ms,
                "efficiency": efficiency,
            }
        )
        if cache_hit is not UNSET:
            field_dict["cache_hit"] = cache_hit
        if error is not UNSET:
            field_dict["error"] = error
        if llm_calls is not UNSET:
            field_dict["llm_calls"] = llm_calls
        if tokens_used is not UNSET:
            field_dict["tokens_used"] = tokens_used
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stage_statistics_metadata import StageStatisticsMetadata

        d = dict(src_dict)
        input_count = d.pop("input_count")

        output_count = d.pop("output_count")

        duration_ms = d.pop("duration_ms")

        efficiency = d.pop("efficiency")

        def _parse_cache_hit(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        cache_hit = _parse_cache_hit(d.pop("cache_hit", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_llm_calls(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        llm_calls = _parse_llm_calls(d.pop("llm_calls", UNSET))

        def _parse_tokens_used(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tokens_used = _parse_tokens_used(d.pop("tokens_used", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: StageStatisticsMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = StageStatisticsMetadata.from_dict(_metadata)

        stage_statistics = cls(
            input_count=input_count,
            output_count=output_count,
            duration_ms=duration_ms,
            efficiency=efficiency,
            cache_hit=cache_hit,
            error=error,
            llm_calls=llm_calls,
            tokens_used=tokens_used,
            metadata=metadata,
        )

        stage_statistics.additional_properties = d
        return stage_statistics

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
