from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplyTaxonomyResponse")


@_attrs_define
class ApplyTaxonomyResponse:
    """Response from applying taxonomy to collection.

    Returns statistics about the materialization process.

        Attributes:
            task_id (str): ID of the Ray task executing the materialization
            status (str): Status of the materialization task
            collection_id (str): Collection ID where taxonomy is being applied
            taxonomy_id (str): Taxonomy ID being applied
            estimated_documents (int | None | Unset): Estimated number of documents to process (if available)
    """

    task_id: str
    status: str
    collection_id: str
    taxonomy_id: str
    estimated_documents: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        status = self.status

        collection_id = self.collection_id

        taxonomy_id = self.taxonomy_id

        estimated_documents: int | None | Unset
        if isinstance(self.estimated_documents, Unset):
            estimated_documents = UNSET
        else:
            estimated_documents = self.estimated_documents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_id": task_id,
                "status": status,
                "collection_id": collection_id,
                "taxonomy_id": taxonomy_id,
            }
        )
        if estimated_documents is not UNSET:
            field_dict["estimated_documents"] = estimated_documents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = d.pop("task_id")

        status = d.pop("status")

        collection_id = d.pop("collection_id")

        taxonomy_id = d.pop("taxonomy_id")

        def _parse_estimated_documents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        estimated_documents = _parse_estimated_documents(d.pop("estimated_documents", UNSET))

        apply_taxonomy_response = cls(
            task_id=task_id,
            status=status,
            collection_id=collection_id,
            taxonomy_id=taxonomy_id,
            estimated_documents=estimated_documents,
        )

        apply_taxonomy_response.additional_properties = d
        return apply_taxonomy_response

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
