from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.evaluation_config import EvaluationConfig


T = TypeVar("T", bound="StartEvaluationRequest")


@_attrs_define
class StartEvaluationRequest:
    """Request to start an evaluation.

    Attributes:
        dataset_name (str): Name of the evaluation dataset to use
        evaluation_config (EvaluationConfig | None | Unset): Optional evaluation configuration (uses defaults if not
            provided)
    """

    dataset_name: str
    evaluation_config: EvaluationConfig | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.evaluation_config import EvaluationConfig

        dataset_name = self.dataset_name

        evaluation_config: dict[str, Any] | None | Unset
        if isinstance(self.evaluation_config, Unset):
            evaluation_config = UNSET
        elif isinstance(self.evaluation_config, EvaluationConfig):
            evaluation_config = self.evaluation_config.to_dict()
        else:
            evaluation_config = self.evaluation_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataset_name": dataset_name,
            }
        )
        if evaluation_config is not UNSET:
            field_dict["evaluation_config"] = evaluation_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evaluation_config import EvaluationConfig

        d = dict(src_dict)
        dataset_name = d.pop("dataset_name")

        def _parse_evaluation_config(data: object) -> EvaluationConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                evaluation_config_type_0 = EvaluationConfig.from_dict(data)

                return evaluation_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EvaluationConfig | None | Unset, data)

        evaluation_config = _parse_evaluation_config(d.pop("evaluation_config", UNSET))

        start_evaluation_request = cls(
            dataset_name=dataset_name,
            evaluation_config=evaluation_config,
        )

        start_evaluation_request.additional_properties = d
        return start_evaluation_request

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
