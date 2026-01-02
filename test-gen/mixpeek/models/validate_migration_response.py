from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dependency_graph import DependencyGraph
    from ..models.validation_result import ValidationResult


T = TypeVar("T", bound="ValidateMigrationResponse")


@_attrs_define
class ValidateMigrationResponse:
    """Response for migration validation.

    Example:
        {'message': 'Configuration is valid with 1 warning', 'validation_result': {'errors': [],
            'estimated_duration_seconds': 1800, 'estimated_resources': {'collection': 5, 'taxonomy': 2}, 'valid': True,
            'warnings': [{'error_code': 'RE_EXTRACT_COST_WARNING', 'message': 'RE_EXTRACT migration will reprocess all
            documents and incur processing costs', 'severity': 'warning'}]}}

    Attributes:
        validation_result (ValidationResult): Result of pre-flight validation.
        message (str): Human-readable message
        dependency_graph (DependencyGraph | None | Unset): Dependency graph if validation passed
    """

    validation_result: ValidationResult
    message: str
    dependency_graph: DependencyGraph | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dependency_graph import DependencyGraph

        validation_result = self.validation_result.to_dict()

        message = self.message

        dependency_graph: dict[str, Any] | None | Unset
        if isinstance(self.dependency_graph, Unset):
            dependency_graph = UNSET
        elif isinstance(self.dependency_graph, DependencyGraph):
            dependency_graph = self.dependency_graph.to_dict()
        else:
            dependency_graph = self.dependency_graph

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "validation_result": validation_result,
                "message": message,
            }
        )
        if dependency_graph is not UNSET:
            field_dict["dependency_graph"] = dependency_graph

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dependency_graph import DependencyGraph
        from ..models.validation_result import ValidationResult

        d = dict(src_dict)
        validation_result = ValidationResult.from_dict(d.pop("validation_result"))

        message = d.pop("message")

        def _parse_dependency_graph(data: object) -> DependencyGraph | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dependency_graph_type_0 = DependencyGraph.from_dict(data)

                return dependency_graph_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DependencyGraph | None | Unset, data)

        dependency_graph = _parse_dependency_graph(d.pop("dependency_graph", UNSET))

        validate_migration_response = cls(
            validation_result=validation_result,
            message=message,
            dependency_graph=dependency_graph,
        )

        validate_migration_response.additional_properties = d
        return validate_migration_response

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
