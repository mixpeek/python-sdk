from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_dataset_request_metadata_type_0 import CreateDatasetRequestMetadataType0
    from ..models.ground_truth_query import GroundTruthQuery


T = TypeVar("T", bound="CreateDatasetRequest")


@_attrs_define
class CreateDatasetRequest:
    """Request model for creating a new evaluation dataset.

    Attributes:
        dataset_name (str): Unique name for this dataset
        queries (list[GroundTruthQuery]): List of queries with ground truth relevance labels
        description (None | str | Unset): Description of what this dataset measures
        metadata (CreateDatasetRequestMetadataType0 | None | Unset): Additional metadata
    """

    dataset_name: str
    queries: list[GroundTruthQuery]
    description: None | str | Unset = UNSET
    metadata: CreateDatasetRequestMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_dataset_request_metadata_type_0 import CreateDatasetRequestMetadataType0

        dataset_name = self.dataset_name

        queries = []
        for queries_item_data in self.queries:
            queries_item = queries_item_data.to_dict()
            queries.append(queries_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CreateDatasetRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataset_name": dataset_name,
                "queries": queries,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_dataset_request_metadata_type_0 import CreateDatasetRequestMetadataType0
        from ..models.ground_truth_query import GroundTruthQuery

        d = dict(src_dict)
        dataset_name = d.pop("dataset_name")

        queries = []
        _queries = d.pop("queries")
        for queries_item_data in _queries:
            queries_item = GroundTruthQuery.from_dict(queries_item_data)

            queries.append(queries_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_metadata(data: object) -> CreateDatasetRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CreateDatasetRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateDatasetRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        create_dataset_request = cls(
            dataset_name=dataset_name,
            queries=queries,
            description=description,
            metadata=metadata,
        )

        create_dataset_request.additional_properties = d
        return create_dataset_request

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
