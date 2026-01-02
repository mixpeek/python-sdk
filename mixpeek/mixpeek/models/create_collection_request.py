from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bucket_schema import BucketSchema
    from ..models.cluster_application_config import ClusterApplicationConfig
    from ..models.create_collection_request_metadata_type_0 import CreateCollectionRequestMetadataType0
    from ..models.feature_extractor_config import FeatureExtractorConfig
    from ..models.source_config import SourceConfig
    from ..models.taxonomy_application_config import TaxonomyApplicationConfig


T = TypeVar("T", bound="CreateCollectionRequest")


@_attrs_define
class CreateCollectionRequest:
    """Request model for creating a new collection.

    Collections process data from buckets or other collections using a single feature extractor.

    KEY ARCHITECTURAL CHANGE: Each collection has EXACTLY ONE feature extractor.
    - Use field_passthrough to include additional source fields in output documents
    - Multiple extractors = multiple collections
    - This simplifies processing and makes output schema deterministic

    CRITICAL: To use input_mappings:
    1. Your source bucket MUST have a bucket_schema defined
    2. The input_mappings reference fields from that bucket_schema
    3. The system validates that mapped fields exist in the source schema

    Example workflow:
    1. Create bucket with schema: { "properties": { "image": {"type": "image"}, "title": {"type": "string"} } }
    2. Upload objects conforming to that schema
    3. Create collection with:
       - input_mappings: { "image": "image" }
       - field_passthrough: [{"source_path": "title"}]
    4. Output documents will have both extractor outputs AND passthrough fields

    Schema Computation:
    - output_schema is computed IMMEDIATELY when collection is created
    - output_schema = field_passthrough fields + extractor output fields
    - No waiting for documents to be processed!

        Attributes:
            collection_name (str): Name of the collection to create
            source (SourceConfig): Configuration for collection source (bucket(s) or collection).

                Collections can process data from two types of sources:

                1. **Bucket Source**: Process raw objects from one or more buckets (first-stage processing)
                   - Use this to create your initial collections from uploaded data
                   - Can specify multiple buckets to consolidate data from different sources
                   - All buckets must have compatible schemas (validated at creation)
                   - Example: Videos from multiple regions → Frame extraction collection

                2. **Collection Source**: Process documents from another collection (decomposition trees)
                   - Use this to create multi-stage processing pipelines
                   - Example: Frames collection → Scene detection collection

                Multi-Bucket Requirements:
                - All buckets must have compatible schemas (same fields, types, and required status)
                - Schema compatibility is validated when the collection is created
                - Documents track which specific bucket they came from via root_bucket_id
                - Useful for consolidating data from multiple regions, teams, or environments

                The source determines:
                - What data the feature extractor receives as input
                - The input_schema available for input_mappings and field_passthrough
                - The lineage tracking in output documents

                Examples:
                    Single bucket: {"type": "bucket", "bucket_ids": ["bkt_products"]}
                    Multi-bucket: {"type": "bucket", "bucket_ids": ["bkt_us", "bkt_eu", "bkt_asia"]}
                    Collection: {"type": "collection", "collection_id": "col_frames"}
            feature_extractor (FeatureExtractorConfig): Configuration for a feature extractor with field passthrough
                support.

                A feature extractor processes source data (from buckets or collections) and
                produces features (embeddings, extracted text, detected objects, etc.).

                With field passthrough, you can also include selected source fields in the
                output documents alongside the computed features.

                Core Concepts:
                    1. **Feature Extraction**: Extractors compute features from input data
                       (e.g., text → embeddings, image → detections, video → scenes)
                    2. **Field Passthrough**: Selectively preserve source fields in output
                       (e.g., title, category, campaign_id from source → output documents)
                    3. **Output Schema**: Combination of passed-through fields + extractor outputs
                       (e.g., {title, category, text_embedding} all in one document)

                How Field Passthrough Works:
                    1. Define which source fields to include via field_passthrough list
                    2. During processing, these fields are extracted from source
                    3. They appear in output documents at root level
                    4. Combine with extractor outputs for complete documents
                    5. Use target_path to rename fields for cleaner schemas

                Field Selection Modes:
                    - **Explicit** (field_passthrough + include_all=False):
                      Only listed fields pass through. Clean, controlled output.
                      Example: passthrough=[title, category] → output has ONLY title, category, embedding

                    - **Inclusive** (include_all=True):
                      All source fields pass through, field_passthrough for renaming.
                      Example: source has 10 fields → output has all 10 + embedding

                    - **None** (no field_passthrough):
                      Only extractor outputs in documents.
                      Example: → output has ONLY embedding (no source fields)

                Use Cases:
                    - **Preserve Identifiers**: Keep campaign_id, product_sku, order_id for tracking
                    - **Enable Filtering**: Pass category, status, department for query filters
                    - **Maintain Context**: Include title, description for display
                    - **Track Metadata**: Preserve author, created_at, source for lineage
                    - **Business Logic**: Keep priority, region, type for application logic

                Common Patterns:
                    1. **Minimal Passthrough** (recommended):
                       field_passthrough=[{"source_path": "id"}], include_all=False
                       → Clean output, only ID + extractor features

                    2. **Metadata Preservation**:
                       field_passthrough=[
                           {"source_path": "title"},
                           {"source_path": "category"},
                           {"source_path": "created_at"}
                       ]
                       → Document has context for display and filtering

                    3. **Field Renaming**:
                       field_passthrough=[
                           {"source_path": "doc_title", "target_path": "title"},
                           {"source_path": "metadata.author", "target_path": "author"}
                       ]
                       → Cleaner output schema with flattened fields

                    4. **Required Fields**:
                       field_passthrough=[
                           {"source_path": "campaign_id", "required": True},
                           {"source_path": "priority", "default": 0}
                       ]
                       → Ensures critical fields always present

                Requirements:
                    - feature_extractor_name: REQUIRED - name of the extractor
                    - version: REQUIRED - extractor version (e.g., "v1")
                    - parameters: NOT REQUIRED - extractor-specific config (model, thresholds, etc.)
                    - input_mappings: NOT REQUIRED - maps extractor inputs to source fields
                    - field_passthrough: NOT REQUIRED - which source fields to preserve (default: none)
                    - include_all_source_fields: NOT REQUIRED - preserve all fields (default: false)
            description (None | str | Unset): Description of the collection
            input_schema (BucketSchema | None | Unset): Input schema for the collection. If not provided, inferred from
                source bucket's bucket_schema or source collection's output_schema. REQUIRED for input_mappings to work -
                defines what fields can be mapped to feature extractors.
            enabled (bool | Unset): Whether the collection is enabled Default: True.
            metadata (CreateCollectionRequestMetadataType0 | None | Unset): Additional metadata for the collection
            taxonomy_applications (list[TaxonomyApplicationConfig] | None | Unset): Optional taxonomy applications to
                automatically enrich documents in this collection. Each taxonomy will classify/enrich documents based on
                configured retriever matches.
            cluster_applications (list[ClusterApplicationConfig] | None | Unset): Optional cluster applications to
                automatically execute when batch processing completes. Each cluster enriches documents with cluster assignments
                (cluster_id, cluster_label, etc.).
    """

    collection_name: str
    source: SourceConfig
    feature_extractor: FeatureExtractorConfig
    description: None | str | Unset = UNSET
    input_schema: BucketSchema | None | Unset = UNSET
    enabled: bool | Unset = True
    metadata: CreateCollectionRequestMetadataType0 | None | Unset = UNSET
    taxonomy_applications: list[TaxonomyApplicationConfig] | None | Unset = UNSET
    cluster_applications: list[ClusterApplicationConfig] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bucket_schema import BucketSchema
        from ..models.create_collection_request_metadata_type_0 import CreateCollectionRequestMetadataType0

        collection_name = self.collection_name

        source = self.source.to_dict()

        feature_extractor = self.feature_extractor.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        input_schema: dict[str, Any] | None | Unset
        if isinstance(self.input_schema, Unset):
            input_schema = UNSET
        elif isinstance(self.input_schema, BucketSchema):
            input_schema = self.input_schema.to_dict()
        else:
            input_schema = self.input_schema

        enabled = self.enabled

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CreateCollectionRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        taxonomy_applications: list[dict[str, Any]] | None | Unset
        if isinstance(self.taxonomy_applications, Unset):
            taxonomy_applications = UNSET
        elif isinstance(self.taxonomy_applications, list):
            taxonomy_applications = []
            for taxonomy_applications_type_0_item_data in self.taxonomy_applications:
                taxonomy_applications_type_0_item = taxonomy_applications_type_0_item_data.to_dict()
                taxonomy_applications.append(taxonomy_applications_type_0_item)

        else:
            taxonomy_applications = self.taxonomy_applications

        cluster_applications: list[dict[str, Any]] | None | Unset
        if isinstance(self.cluster_applications, Unset):
            cluster_applications = UNSET
        elif isinstance(self.cluster_applications, list):
            cluster_applications = []
            for cluster_applications_type_0_item_data in self.cluster_applications:
                cluster_applications_type_0_item = cluster_applications_type_0_item_data.to_dict()
                cluster_applications.append(cluster_applications_type_0_item)

        else:
            cluster_applications = self.cluster_applications

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_name": collection_name,
                "source": source,
                "feature_extractor": feature_extractor,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if input_schema is not UNSET:
            field_dict["input_schema"] = input_schema
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if taxonomy_applications is not UNSET:
            field_dict["taxonomy_applications"] = taxonomy_applications
        if cluster_applications is not UNSET:
            field_dict["cluster_applications"] = cluster_applications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bucket_schema import BucketSchema
        from ..models.cluster_application_config import ClusterApplicationConfig
        from ..models.create_collection_request_metadata_type_0 import CreateCollectionRequestMetadataType0
        from ..models.feature_extractor_config import FeatureExtractorConfig
        from ..models.source_config import SourceConfig
        from ..models.taxonomy_application_config import TaxonomyApplicationConfig

        d = dict(src_dict)
        collection_name = d.pop("collection_name")

        source = SourceConfig.from_dict(d.pop("source"))

        feature_extractor = FeatureExtractorConfig.from_dict(d.pop("feature_extractor"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_input_schema(data: object) -> BucketSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_schema_type_0 = BucketSchema.from_dict(data)

                return input_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BucketSchema | None | Unset, data)

        input_schema = _parse_input_schema(d.pop("input_schema", UNSET))

        enabled = d.pop("enabled", UNSET)

        def _parse_metadata(data: object) -> CreateCollectionRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CreateCollectionRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateCollectionRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_taxonomy_applications(data: object) -> list[TaxonomyApplicationConfig] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                taxonomy_applications_type_0 = []
                _taxonomy_applications_type_0 = data
                for taxonomy_applications_type_0_item_data in _taxonomy_applications_type_0:
                    taxonomy_applications_type_0_item = TaxonomyApplicationConfig.from_dict(
                        taxonomy_applications_type_0_item_data
                    )

                    taxonomy_applications_type_0.append(taxonomy_applications_type_0_item)

                return taxonomy_applications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TaxonomyApplicationConfig] | None | Unset, data)

        taxonomy_applications = _parse_taxonomy_applications(d.pop("taxonomy_applications", UNSET))

        def _parse_cluster_applications(data: object) -> list[ClusterApplicationConfig] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cluster_applications_type_0 = []
                _cluster_applications_type_0 = data
                for cluster_applications_type_0_item_data in _cluster_applications_type_0:
                    cluster_applications_type_0_item = ClusterApplicationConfig.from_dict(
                        cluster_applications_type_0_item_data
                    )

                    cluster_applications_type_0.append(cluster_applications_type_0_item)

                return cluster_applications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClusterApplicationConfig] | None | Unset, data)

        cluster_applications = _parse_cluster_applications(d.pop("cluster_applications", UNSET))

        create_collection_request = cls(
            collection_name=collection_name,
            source=source,
            feature_extractor=feature_extractor,
            description=description,
            input_schema=input_schema,
            enabled=enabled,
            metadata=metadata,
            taxonomy_applications=taxonomy_applications,
            cluster_applications=cluster_applications,
        )

        create_collection_request.additional_properties = d
        return create_collection_request

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
