from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.explain_retriever_request_inputs import ExplainRetrieverRequestInputs


T = TypeVar("T", bound="ExplainRetrieverRequest")


@_attrs_define
class ExplainRetrieverRequest:
    """Request to get execution plan for a retriever.

    Provides optional hypothetical inputs to tailor the execution plan estimation.
    The explain endpoint analyzes your retriever configuration and returns cost/latency
    estimates without actually executing the query.

    Use Cases:
        - See how plan changes with different input values
        - Estimate costs for different query patterns
        - Understand impact of parameter changes (e.g., top_k)
        - Test stage behavior with representative inputs

    Behavior:
        - If inputs are provided, they're used for tailored estimation
        - If inputs are not provided, default/representative values are used
        - Inputs do NOT need to match your input_schema exactly
        - No actual retrieval is performed (explain is analysis only)

        Attributes:
            inputs (ExplainRetrieverRequestInputs | Unset): Hypothetical inputs for tailored execution plan estimation.
                These values are used to analyze stage behavior and estimate costs.

                NOT REQUIRED - if omitted, default/representative values are used.

                Common inputs:
                - 'query': Search query text (for semantic search stages)
                - 'top_k': Number of results to return (affects search scope)
                - Filter parameters: Category, price range, etc.


                Examples:
                - {'query': 'laptop'} - Simple text query
                - {'query': 'laptop', 'top_k': 100} - Query with custom limit
                - {'query': 'laptop', 'category': 'electronics', 'price_max': 1000} - Query with filters


                Note: Inputs are for estimation only. No actual search is performed.
    """

    inputs: ExplainRetrieverRequestInputs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inputs is not UNSET:
            field_dict["inputs"] = inputs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.explain_retriever_request_inputs import ExplainRetrieverRequestInputs

        d = dict(src_dict)
        _inputs = d.pop("inputs", UNSET)
        inputs: ExplainRetrieverRequestInputs | Unset
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = ExplainRetrieverRequestInputs.from_dict(_inputs)

        explain_retriever_request = cls(
            inputs=inputs,
        )

        explain_retriever_request.additional_properties = d
        return explain_retriever_request

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
