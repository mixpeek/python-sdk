from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.evaluation_dataset_metadata_type_0 import EvaluationDatasetMetadataType0
    from ..models.ground_truth_query import GroundTruthQuery


T = TypeVar("T", bound="EvaluationDataset")


@_attrs_define
class EvaluationDataset:
    """Complete evaluation dataset with metadata.

    An evaluation dataset is a collection of queries with ground truth relevance labels,
    used to measure retriever quality.

        Attributes:
            dataset_id (str): Unique dataset identifier
            dataset_name (str): Human-readable dataset name
            queries (list[GroundTruthQuery]): List of queries with ground truth
            created_at (datetime.datetime): When dataset was created
            updated_at (datetime.datetime): Last update timestamp
            namespace_id (str): Namespace this dataset belongs to
            internal_id (str): Internal organization ID
            query_count (int): Number of queries in dataset
            description (None | str | Unset): Dataset description
            metadata (EvaluationDatasetMetadataType0 | None | Unset): Additional metadata (e.g., labeling instructions,
                version info)
    """

    dataset_id: str
    dataset_name: str
    queries: list[GroundTruthQuery]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    namespace_id: str
    internal_id: str
    query_count: int
    description: None | str | Unset = UNSET
    metadata: EvaluationDatasetMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.evaluation_dataset_metadata_type_0 import EvaluationDatasetMetadataType0

        dataset_id = self.dataset_id

        dataset_name = self.dataset_name

        queries = []
        for queries_item_data in self.queries:
            queries_item = queries_item_data.to_dict()
            queries.append(queries_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        namespace_id = self.namespace_id

        internal_id = self.internal_id

        query_count = self.query_count

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, EvaluationDatasetMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataset_id": dataset_id,
                "dataset_name": dataset_name,
                "queries": queries,
                "created_at": created_at,
                "updated_at": updated_at,
                "namespace_id": namespace_id,
                "internal_id": internal_id,
                "query_count": query_count,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evaluation_dataset_metadata_type_0 import EvaluationDatasetMetadataType0
        from ..models.ground_truth_query import GroundTruthQuery

        d = dict(src_dict)
        dataset_id = d.pop("dataset_id")

        dataset_name = d.pop("dataset_name")

        queries = []
        _queries = d.pop("queries")
        for queries_item_data in _queries:
            queries_item = GroundTruthQuery.from_dict(queries_item_data)

            queries.append(queries_item)

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        namespace_id = d.pop("namespace_id")

        internal_id = d.pop("internal_id")

        query_count = d.pop("query_count")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_metadata(data: object) -> EvaluationDatasetMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = EvaluationDatasetMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EvaluationDatasetMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        evaluation_dataset = cls(
            dataset_id=dataset_id,
            dataset_name=dataset_name,
            queries=queries,
            created_at=created_at,
            updated_at=updated_at,
            namespace_id=namespace_id,
            internal_id=internal_id,
            query_count=query_count,
            description=description,
            metadata=metadata,
        )

        evaluation_dataset.additional_properties = d
        return evaluation_dataset

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
