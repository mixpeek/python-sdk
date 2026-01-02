from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bucket_schema_field_type import BucketSchemaFieldType
from ..models.vector_data_type import VectorDataType
from ..models.vector_type import VectorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VectorIndex")


@_attrs_define
class VectorIndex:
    """Configuration for a single vector index in Qdrant.

    Defines the fully-qualified vector index including storage name, dimensions,
    distance metric, and inference service. This is the actual index that gets
    created in Qdrant and used for vector similarity search.

    Key Concepts:
        - The `name` field is the FULL qualified name used as the Qdrant collection name
        - Format: {extractor}_{version}_{output} (e.g., "text_extractor_v1_embedding")
        - This ensures namespace isolation between extractors and versions
        - Different from VectorIndexDefinition.name which is the short user-facing name

    Use Cases:
        - Define vector storage configuration for feature extractors
        - Specify inference service and model parameters
        - Configure distance metrics for similarity search
        - Set storage optimization (on-disk for large vectors)

    Requirements:
        - name: REQUIRED - Must be unique across all extractors in namespace
        - description: REQUIRED - Explain what this vector represents
        - dimensions: REQUIRED for DENSE vectors, OPTIONAL for SPARSE
        - type: REQUIRED - Must match VectorType enum
        - inference_name: REQUIRED - Must reference a valid inference service

        Attributes:
            name (str): REQUIRED. Fully-qualified vector index name (Qdrant collection name). Format:
                {extractor}_{version}_{output} (e.g., 'text_extractor_v1_embedding'). This is the STORAGE name used internally
                in Qdrant, NOT the user-facing short name. Must be unique across all extractors in the namespace to prevent
                collisions. Different versions of same extractor use different names for isolation.
            description (str): REQUIRED. Human-readable description of what this vector index represents. Explain the
                content type, use cases, and search characteristics. Shown in API documentation and collection metadata. Be
                specific about what embeddings are stored here.
            type_ (VectorType): Vector types supported by the Mixpeek system.

                Defines the storage format and structure of embeddings in Qdrant.

                Values:
                    DENSE: Traditional float array embeddings (e.g., [0.1, 0.2, 0.3]).
                           Most common format. Used by: text_extractor, multimodal_extractor, image_extractor.
                           Storage: ~4KB per 1024-dim vector. Fast cosine/dot similarity search.

                    SPARSE: Index-value pairs for sparse embeddings (e.g., SPLADE, BM25).
                            Only stores non-zero dimensions. Format: {indices: [1,5,9], values: [0.8,0.6,0.4]}.
                            Storage: ~20KB. Keyword-based semantic search.

                    MULTI_DENSE: List of dense vectors for late interaction models (e.g., ColBERT).
                                 Each document has multiple embeddings. Format: [[0.1,0.2], [0.3,0.4], ...].
                                 Storage: ~500KB. High-precision retrieval.

                Examples:
                    - DENSE for general semantic search (text_extractor, multimodal_extractor)
                    - SPARSE for keyword expansion and explainability
                    - MULTI_DENSE for maximum precision retrieval
            dimensions (int | None | Unset): Number of vector dimensions. REQUIRED for DENSE vectors (e.g., 1024 for
                E5-Large, 1408 for multimodal). NOT REQUIRED for SPARSE vectors (dimensions determined dynamically). Must match
                the output dimensions of the inference service. Cannot be changed after index creation without recreating the
                collection.
            distance (None | str | Unset): Distance metric for similarity search. OPTIONAL - defaults to 'cosine'
                (normalized dot product). Options: 'cosine' (most common, normalized), 'dot' (raw dot product), 'euclidean' (L2
                distance), 'manhattan' (L1 distance). Cosine recommended for most embeddings as it's scale-invariant. Must match
                the metric your model was trained with. Default: 'cosine'.
            datatype (None | Unset | VectorDataType): Data type for storing vector values. OPTIONAL - defaults to FLOAT32
                (standard precision). Use FLOAT32 for general use (4 bytes per dimension). Use FLOAT16 to save 50% storage with
                minimal quality loss. Use UINT8 for maximum compression (quantization, ~2% quality loss). Lower precision =
                smaller storage + faster search, slightly lower accuracy. Default: VectorDataType.FLOAT32.
            on_disk (bool | None | Unset): OPTIONAL. If true, vectors stored on disk instead of RAM. Use for very large
                vectors (>2GB total) to save memory. Trade-off: ~10x slower search, but unlimited capacity. Defaults to false
                (RAM storage) for fast search. Enable for: massive datasets, high-dimensional vectors (>2048 dims), or when RAM
                is constrained. Recommended for ColBERT (500KB/doc).
            supported_inputs (list[BucketSchemaFieldType] | None | Unset): OPTIONAL. List of bucket schema field types this
                vector can process. Validates that input fields are compatible with this index. Examples: TEXT and STRING for
                text embeddings, VIDEO and IMAGE for multimodal embeddings, DOCUMENT for PDF extractors. Used for validation
                during collection creation.
            inference_name (None | str | Unset): REQUIRED. Identifier of the inference service to generate embeddings. Must
                reference a valid inference service registered in the system. Examples: 'multilingual_e5_large_instruct_v1' for
                text, 'vertex_multimodal_embedding' for video, 'laion_clip_vit_l_14_v1' for images. This determines which model
                creates the vectors during ingestion. Cannot be changed after collection creation.
    """

    name: str
    description: str
    type_: VectorType
    dimensions: int | None | Unset = UNSET
    distance: None | str | Unset = "cosine"
    datatype: None | Unset | VectorDataType = VectorDataType.FLOAT32
    on_disk: bool | None | Unset = UNSET
    supported_inputs: list[BucketSchemaFieldType] | None | Unset = UNSET
    inference_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        type_ = self.type_.value

        dimensions: int | None | Unset
        if isinstance(self.dimensions, Unset):
            dimensions = UNSET
        else:
            dimensions = self.dimensions

        distance: None | str | Unset
        if isinstance(self.distance, Unset):
            distance = UNSET
        else:
            distance = self.distance

        datatype: None | str | Unset
        if isinstance(self.datatype, Unset):
            datatype = UNSET
        elif isinstance(self.datatype, VectorDataType):
            datatype = self.datatype.value
        else:
            datatype = self.datatype

        on_disk: bool | None | Unset
        if isinstance(self.on_disk, Unset):
            on_disk = UNSET
        else:
            on_disk = self.on_disk

        supported_inputs: list[str] | None | Unset
        if isinstance(self.supported_inputs, Unset):
            supported_inputs = UNSET
        elif isinstance(self.supported_inputs, list):
            supported_inputs = []
            for supported_inputs_type_0_item_data in self.supported_inputs:
                supported_inputs_type_0_item = supported_inputs_type_0_item_data.value
                supported_inputs.append(supported_inputs_type_0_item)

        else:
            supported_inputs = self.supported_inputs

        inference_name: None | str | Unset
        if isinstance(self.inference_name, Unset):
            inference_name = UNSET
        else:
            inference_name = self.inference_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "type": type_,
            }
        )
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if distance is not UNSET:
            field_dict["distance"] = distance
        if datatype is not UNSET:
            field_dict["datatype"] = datatype
        if on_disk is not UNSET:
            field_dict["on_disk"] = on_disk
        if supported_inputs is not UNSET:
            field_dict["supported_inputs"] = supported_inputs
        if inference_name is not UNSET:
            field_dict["inference_name"] = inference_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        type_ = VectorType(d.pop("type"))

        def _parse_dimensions(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dimensions = _parse_dimensions(d.pop("dimensions", UNSET))

        def _parse_distance(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        distance = _parse_distance(d.pop("distance", UNSET))

        def _parse_datatype(data: object) -> None | Unset | VectorDataType:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                datatype_type_0 = VectorDataType(data)

                return datatype_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VectorDataType, data)

        datatype = _parse_datatype(d.pop("datatype", UNSET))

        def _parse_on_disk(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        on_disk = _parse_on_disk(d.pop("on_disk", UNSET))

        def _parse_supported_inputs(data: object) -> list[BucketSchemaFieldType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supported_inputs_type_0 = []
                _supported_inputs_type_0 = data
                for supported_inputs_type_0_item_data in _supported_inputs_type_0:
                    supported_inputs_type_0_item = BucketSchemaFieldType(supported_inputs_type_0_item_data)

                    supported_inputs_type_0.append(supported_inputs_type_0_item)

                return supported_inputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BucketSchemaFieldType] | None | Unset, data)

        supported_inputs = _parse_supported_inputs(d.pop("supported_inputs", UNSET))

        def _parse_inference_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inference_name = _parse_inference_name(d.pop("inference_name", UNSET))

        vector_index = cls(
            name=name,
            description=description,
            type_=type_,
            dimensions=dimensions,
            distance=distance,
            datatype=datatype,
            on_disk=on_disk,
            supported_inputs=supported_inputs,
            inference_name=inference_name,
        )

        vector_index.additional_properties = d
        return vector_index

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
