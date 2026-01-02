from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dense_vector import DenseVector
    from ..models.feature_model_payload import FeatureModelPayload
    from ..models.multi_dense_vector import MultiDenseVector
    from ..models.named_dense_vectors import NamedDenseVectors
    from ..models.sparse_vector import SparseVector


T = TypeVar("T", bound="FeatureModel")


@_attrs_define
class FeatureModel:
    """Response from a feature extractor.

    Attributes:
        feature_extractor_id (str): ID of the feature extractor that produced this response
        payload (FeatureModelPayload | Unset): Metadata of the feature
        vectors (DenseVector | MultiDenseVector | NamedDenseVectors | None | SparseVector | Unset): Vector
            representation of the feature. Can be any supported vector type.
    """

    feature_extractor_id: str
    payload: FeatureModelPayload | Unset = UNSET
    vectors: DenseVector | MultiDenseVector | NamedDenseVectors | None | SparseVector | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dense_vector import DenseVector
        from ..models.multi_dense_vector import MultiDenseVector
        from ..models.named_dense_vectors import NamedDenseVectors
        from ..models.sparse_vector import SparseVector

        feature_extractor_id = self.feature_extractor_id

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        vectors: dict[str, Any] | None | Unset
        if isinstance(self.vectors, Unset):
            vectors = UNSET
        elif isinstance(self.vectors, DenseVector):
            vectors = self.vectors.to_dict()
        elif isinstance(self.vectors, SparseVector):
            vectors = self.vectors.to_dict()
        elif isinstance(self.vectors, MultiDenseVector):
            vectors = self.vectors.to_dict()
        elif isinstance(self.vectors, NamedDenseVectors):
            vectors = self.vectors.to_dict()
        else:
            vectors = self.vectors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feature_extractor_id": feature_extractor_id,
            }
        )
        if payload is not UNSET:
            field_dict["payload"] = payload
        if vectors is not UNSET:
            field_dict["vectors"] = vectors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dense_vector import DenseVector
        from ..models.feature_model_payload import FeatureModelPayload
        from ..models.multi_dense_vector import MultiDenseVector
        from ..models.named_dense_vectors import NamedDenseVectors
        from ..models.sparse_vector import SparseVector

        d = dict(src_dict)
        feature_extractor_id = d.pop("feature_extractor_id")

        _payload = d.pop("payload", UNSET)
        payload: FeatureModelPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = FeatureModelPayload.from_dict(_payload)

        def _parse_vectors(
            data: object,
        ) -> DenseVector | MultiDenseVector | NamedDenseVectors | None | SparseVector | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vectors_type_0 = DenseVector.from_dict(data)

                return vectors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vectors_type_1 = SparseVector.from_dict(data)

                return vectors_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vectors_type_2 = MultiDenseVector.from_dict(data)

                return vectors_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vectors_type_3 = NamedDenseVectors.from_dict(data)

                return vectors_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DenseVector | MultiDenseVector | NamedDenseVectors | None | SparseVector | Unset, data)

        vectors = _parse_vectors(d.pop("vectors", UNSET))

        feature_model = cls(
            feature_extractor_id=feature_extractor_id,
            payload=payload,
            vectors=vectors,
        )

        feature_model.additional_properties = d
        return feature_model

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
