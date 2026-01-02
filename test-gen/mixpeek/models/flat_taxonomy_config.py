from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.input_mapping import InputMapping
    from ..models.source_collection import SourceCollection
    from ..models.step_analytics_config import StepAnalyticsConfig


T = TypeVar("T", bound="FlatTaxonomyConfig")


@_attrs_define
class FlatTaxonomyConfig:
    """Configuration for a *flat* taxonomy - single source collection with one retriever.

    Attributes:
        retriever_id (str): The retriever to use for matching against the source collection.
        input_mappings (list[InputMapping]): Input mappings defining how to construct retriever inputs.
        source_collection (SourceCollection): A source collection for a flat taxonomy.
        taxonomy_type (Literal['flat'] | Unset): Discriminator identifying this as a flat taxonomy. Default: 'flat'.
        step_analytics (None | StepAnalyticsConfig | Unset): Optional configuration for step transition analytics.
            Enables tracking how documents progress through taxonomy labels over time (e.g., email thread progression from
            'inquiry' to 'closed_won'). If not provided, only basic assignment events are logged.
    """

    retriever_id: str
    input_mappings: list[InputMapping]
    source_collection: SourceCollection
    taxonomy_type: Literal["flat"] | Unset = "flat"
    step_analytics: None | StepAnalyticsConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.step_analytics_config import StepAnalyticsConfig

        retriever_id = self.retriever_id

        input_mappings = []
        for input_mappings_item_data in self.input_mappings:
            input_mappings_item = input_mappings_item_data.to_dict()
            input_mappings.append(input_mappings_item)

        source_collection = self.source_collection.to_dict()

        taxonomy_type = self.taxonomy_type

        step_analytics: dict[str, Any] | None | Unset
        if isinstance(self.step_analytics, Unset):
            step_analytics = UNSET
        elif isinstance(self.step_analytics, StepAnalyticsConfig):
            step_analytics = self.step_analytics.to_dict()
        else:
            step_analytics = self.step_analytics

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retriever_id": retriever_id,
                "input_mappings": input_mappings,
                "source_collection": source_collection,
            }
        )
        if taxonomy_type is not UNSET:
            field_dict["taxonomy_type"] = taxonomy_type
        if step_analytics is not UNSET:
            field_dict["step_analytics"] = step_analytics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_mapping import InputMapping
        from ..models.source_collection import SourceCollection
        from ..models.step_analytics_config import StepAnalyticsConfig

        d = dict(src_dict)
        retriever_id = d.pop("retriever_id")

        input_mappings = []
        _input_mappings = d.pop("input_mappings")
        for input_mappings_item_data in _input_mappings:
            input_mappings_item = InputMapping.from_dict(input_mappings_item_data)

            input_mappings.append(input_mappings_item)

        source_collection = SourceCollection.from_dict(d.pop("source_collection"))

        taxonomy_type = cast(Literal["flat"] | Unset, d.pop("taxonomy_type", UNSET))
        if taxonomy_type != "flat" and not isinstance(taxonomy_type, Unset):
            raise ValueError(f"taxonomy_type must match const 'flat', got '{taxonomy_type}'")

        def _parse_step_analytics(data: object) -> None | StepAnalyticsConfig | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                step_analytics_type_0 = StepAnalyticsConfig.from_dict(data)

                return step_analytics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StepAnalyticsConfig | Unset, data)

        step_analytics = _parse_step_analytics(d.pop("step_analytics", UNSET))

        flat_taxonomy_config = cls(
            retriever_id=retriever_id,
            input_mappings=input_mappings,
            source_collection=source_collection,
            taxonomy_type=taxonomy_type,
            step_analytics=step_analytics,
        )

        flat_taxonomy_config.additional_properties = d
        return flat_taxonomy_config

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
