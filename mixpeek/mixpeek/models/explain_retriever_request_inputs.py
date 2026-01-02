from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExplainRetrieverRequestInputs")


@_attrs_define
class ExplainRetrieverRequestInputs:
    """Hypothetical inputs for tailored execution plan estimation. These values are used to analyze stage behavior and
    estimate costs.

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

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        explain_retriever_request_inputs = cls()

        explain_retriever_request_inputs.additional_properties = d
        return explain_retriever_request_inputs

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
