from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.namespace_operation import NamespaceOperation
from ..models.resource_type import ResourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceScope")


@_attrs_define
class ResourceScope:
    """Fine-grained restriction applied to an API key.

    Attributes:
        resource_type (ResourceType): Resource surfaces supported by scoped API keys and audit events.

            These resource types can be used in:
            - API key scopes to restrict access to specific resources
            - Audit logs to identify what type of resource was affected
            - Permission systems to grant/deny access to resource categories

            Resource hierarchy:
                ORGANIZATION -> USER, API_KEY, STORAGE_CONNECTION
                NAMESPACE -> COLLECTION, BUCKET, RETRIEVER, CLUSTER, TAXONOMY

            Resource types:
                - ORGANIZATION: Top-level tenant entity
                - USER: Organization member with authentication credentials
                - API_KEY: Authentication token for programmatic access
                - NAMESPACE: Isolated environment for data and compute resources
                - COLLECTION: Vector database collection for searchable documents
                - BUCKET: Object storage container for raw files
                - RETRIEVER: Configured search/retrieval pipeline
                - CLUSTER: Ray compute cluster for distributed processing
                - TAXONOMY: Hierarchical classification system for documents
                - STORAGE_CONNECTION: External storage provider integration
        resource_id (str): Identifier or pattern for the resource. Accepts a literal ID (e.g. 'ns_production') or
            wildcard forms such as '*' or 'ns_customer_*'.
        operations (list[NamespaceOperation] | None | Unset): Subset of operations allowed within the scope. When
            omitted the key may perform any operation permitted by its Permission list.
    """

    resource_type: ResourceType
    resource_id: str
    operations: list[NamespaceOperation] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_type = self.resource_type.value

        resource_id = self.resource_id

        operations: list[str] | None | Unset
        if isinstance(self.operations, Unset):
            operations = UNSET
        elif isinstance(self.operations, list):
            operations = []
            for operations_type_0_item_data in self.operations:
                operations_type_0_item = operations_type_0_item_data.value
                operations.append(operations_type_0_item)

        else:
            operations = self.operations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_type": resource_type,
                "resource_id": resource_id,
            }
        )
        if operations is not UNSET:
            field_dict["operations"] = operations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_type = ResourceType(d.pop("resource_type"))

        resource_id = d.pop("resource_id")

        def _parse_operations(data: object) -> list[NamespaceOperation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                operations_type_0 = []
                _operations_type_0 = data
                for operations_type_0_item_data in _operations_type_0:
                    operations_type_0_item = NamespaceOperation(operations_type_0_item_data)

                    operations_type_0.append(operations_type_0_item)

                return operations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NamespaceOperation] | None | Unset, data)

        operations = _parse_operations(d.pop("operations", UNSET))

        resource_scope = cls(
            resource_type=resource_type,
            resource_id=resource_id,
            operations=operations,
        )

        resource_scope.additional_properties = d
        return resource_scope

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
