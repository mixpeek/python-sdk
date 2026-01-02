from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_graph_extractor_params import DocumentGraphExtractorParams
    from ..models.face_identity_extractor_params import FaceIdentityExtractorParams
    from ..models.feature_extractor_config_input_mappings_type_0 import FeatureExtractorConfigInputMappingsType0
    from ..models.feature_extractor_config_params_type_0 import FeatureExtractorConfigParamsType0
    from ..models.field_passthrough import FieldPassthrough
    from ..models.image_extractor_params import ImageExtractorParams
    from ..models.input_mapping import InputMapping
    from ..models.multimodal_extractor_params import MultimodalExtractorParams
    from ..models.text_extractor_params import TextExtractorParams


T = TypeVar("T", bound="FeatureExtractorConfig")


@_attrs_define
class FeatureExtractorConfig:
    """Configuration for a feature extractor with field passthrough support.

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

        Attributes:
            feature_extractor_name (str): Name of the feature extractor
            version (str): Version of the feature extractor
            params (FeatureExtractorConfigParamsType0 | None | Unset): Optional extractor parameters that affect vector
                index configuration. Parameters set here are locked at namespace creation and determine vector dimensions in
                Qdrant. Collections using this extractor must use compatible params. Example: {'model': 'siglip_base'}
            parameters (DocumentGraphExtractorParams | FaceIdentityExtractorParams | ImageExtractorParams |
                MultimodalExtractorParams | None | TextExtractorParams | Unset): Parameters for the feature extractor. Each
                extractor type has specific parameters. See the schema for your chosen extractor (e.g.,
                MultimodalExtractorParams for multimodal_extractor).
            input_mappings (FeatureExtractorConfigInputMappingsType0 | list[InputMapping] | Unset): Mapping from extractor
                input names to source field paths. Tells the extractor which source fields to process. Example: {'image':
                'thumbnail_url', 'text': 'description'}
            field_passthrough (list[FieldPassthrough] | Unset): NOT REQUIRED. List of specific fields to pass through from
                source to output documents. These fields are included alongside extractor-computed features (embeddings,
                detections, etc.). Empty list = only extractor outputs in documents (default behavior). With entries = specified
                fields + extractor outputs in documents.

                How It Works:
                1. During processing, fields are extracted from source object/document
                2. They appear in output documents at the root level
                3. Field filtering happens automatically (only listed fields included)
                4. Use target_path to rename fields for cleaner schemas

                Common Use Cases:
                - Preserve identifiers: campaign_id, product_sku, order_id
                - Keep metadata: category, tags, author, created_at
                - Enable filtering: department, status, priority, region
                - Maintain context: title, description, source_url

                Behavior:
                - Works with include_all_source_fields=False (default): ONLY these fields included
                - Works with include_all_source_fields=True: These configs used for renaming/defaults
                - Fields must exist in source bucket_schema or upstream collection output_schema
                - Missing optional fields are omitted (unless default provided)
                - Missing required fields cause processing errors

                Output Schema:
                output_schema = field_passthrough fields + extractor output fields
                Example: ['title', 'category', 'text_extractor_v1_embedding']
            include_all_source_fields (bool | Unset): NOT REQUIRED. Whether to include ALL fields from source
                object/document in output. Default: False (only field_passthrough fields included).

                When False (RECOMMENDED):
                - Only fields listed in field_passthrough are included in output
                - Creates clean, predictable output schemas
                - Prevents data leakage of unwanted fields
                - Output = field_passthrough fields + extractor outputs

                When True (USE WITH CAUTION):
                - ALL source fields are included in output documents
                - field_passthrough still used for renaming/defaults/requirements
                - Can result in large documents if source has many fields
                - Can leak sensitive or unnecessary data
                - Output = all source fields + extractor outputs

                Use True When:
                - You want to preserve complete source data
                - Source has limited, well-defined fields
                - Downstream processing needs all context

                Use False When (MOST CASES):
                - You want clean, controlled output schemas
                - Source has many fields you don't need
                - You want explicit field selection
                - You're concerned about document size

                Examples:
                False: source={a,b,c,d} + passthrough=[a,b] → output={a,b,embedding}
                True:  source={a,b,c,d} + passthrough=[a→x] → output={x,b,c,d,embedding} Default: False.
    """

    feature_extractor_name: str
    version: str
    params: FeatureExtractorConfigParamsType0 | None | Unset = UNSET
    parameters: (
        DocumentGraphExtractorParams
        | FaceIdentityExtractorParams
        | ImageExtractorParams
        | MultimodalExtractorParams
        | None
        | TextExtractorParams
        | Unset
    ) = UNSET
    input_mappings: FeatureExtractorConfigInputMappingsType0 | list[InputMapping] | Unset = UNSET
    field_passthrough: list[FieldPassthrough] | Unset = UNSET
    include_all_source_fields: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.document_graph_extractor_params import DocumentGraphExtractorParams
        from ..models.face_identity_extractor_params import FaceIdentityExtractorParams
        from ..models.feature_extractor_config_input_mappings_type_0 import FeatureExtractorConfigInputMappingsType0
        from ..models.feature_extractor_config_params_type_0 import FeatureExtractorConfigParamsType0
        from ..models.image_extractor_params import ImageExtractorParams
        from ..models.multimodal_extractor_params import MultimodalExtractorParams
        from ..models.text_extractor_params import TextExtractorParams

        feature_extractor_name = self.feature_extractor_name

        version = self.version

        params: dict[str, Any] | None | Unset
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, FeatureExtractorConfigParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        parameters: dict[str, Any] | None | Unset
        if isinstance(self.parameters, Unset):
            parameters = UNSET
        elif isinstance(self.parameters, TextExtractorParams):
            parameters = self.parameters.to_dict()
        elif isinstance(self.parameters, MultimodalExtractorParams):
            parameters = self.parameters.to_dict()
        elif isinstance(self.parameters, FaceIdentityExtractorParams):
            parameters = self.parameters.to_dict()
        elif isinstance(self.parameters, ImageExtractorParams):
            parameters = self.parameters.to_dict()
        elif isinstance(self.parameters, DocumentGraphExtractorParams):
            parameters = self.parameters.to_dict()
        else:
            parameters = self.parameters

        input_mappings: dict[str, Any] | list[dict[str, Any]] | Unset
        if isinstance(self.input_mappings, Unset):
            input_mappings = UNSET
        elif isinstance(self.input_mappings, FeatureExtractorConfigInputMappingsType0):
            input_mappings = self.input_mappings.to_dict()
        else:
            input_mappings = []
            for input_mappings_type_1_item_data in self.input_mappings:
                input_mappings_type_1_item = input_mappings_type_1_item_data.to_dict()
                input_mappings.append(input_mappings_type_1_item)

        field_passthrough: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.field_passthrough, Unset):
            field_passthrough = []
            for field_passthrough_item_data in self.field_passthrough:
                field_passthrough_item = field_passthrough_item_data.to_dict()
                field_passthrough.append(field_passthrough_item)

        include_all_source_fields = self.include_all_source_fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feature_extractor_name": feature_extractor_name,
                "version": version,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if input_mappings is not UNSET:
            field_dict["input_mappings"] = input_mappings
        if field_passthrough is not UNSET:
            field_dict["field_passthrough"] = field_passthrough
        if include_all_source_fields is not UNSET:
            field_dict["include_all_source_fields"] = include_all_source_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_graph_extractor_params import DocumentGraphExtractorParams
        from ..models.face_identity_extractor_params import FaceIdentityExtractorParams
        from ..models.feature_extractor_config_input_mappings_type_0 import FeatureExtractorConfigInputMappingsType0
        from ..models.feature_extractor_config_params_type_0 import FeatureExtractorConfigParamsType0
        from ..models.field_passthrough import FieldPassthrough
        from ..models.image_extractor_params import ImageExtractorParams
        from ..models.input_mapping import InputMapping
        from ..models.multimodal_extractor_params import MultimodalExtractorParams
        from ..models.text_extractor_params import TextExtractorParams

        d = dict(src_dict)
        feature_extractor_name = d.pop("feature_extractor_name")

        version = d.pop("version")

        def _parse_params(data: object) -> FeatureExtractorConfigParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = FeatureExtractorConfigParamsType0.from_dict(data)

                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FeatureExtractorConfigParamsType0 | None | Unset, data)

        params = _parse_params(d.pop("params", UNSET))

        def _parse_parameters(
            data: object,
        ) -> (
            DocumentGraphExtractorParams
            | FaceIdentityExtractorParams
            | ImageExtractorParams
            | MultimodalExtractorParams
            | None
            | TextExtractorParams
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parameters_type_0_type_0 = TextExtractorParams.from_dict(data)

                return parameters_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parameters_type_0_type_1 = MultimodalExtractorParams.from_dict(data)

                return parameters_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parameters_type_0_type_2 = FaceIdentityExtractorParams.from_dict(data)

                return parameters_type_0_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parameters_type_0_type_3 = ImageExtractorParams.from_dict(data)

                return parameters_type_0_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parameters_type_0_type_4 = DocumentGraphExtractorParams.from_dict(data)

                return parameters_type_0_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DocumentGraphExtractorParams
                | FaceIdentityExtractorParams
                | ImageExtractorParams
                | MultimodalExtractorParams
                | None
                | TextExtractorParams
                | Unset,
                data,
            )

        parameters = _parse_parameters(d.pop("parameters", UNSET))

        def _parse_input_mappings(
            data: object,
        ) -> FeatureExtractorConfigInputMappingsType0 | list[InputMapping] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_mappings_type_0 = FeatureExtractorConfigInputMappingsType0.from_dict(data)

                return input_mappings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            input_mappings_type_1 = []
            _input_mappings_type_1 = data
            for input_mappings_type_1_item_data in _input_mappings_type_1:
                input_mappings_type_1_item = InputMapping.from_dict(input_mappings_type_1_item_data)

                input_mappings_type_1.append(input_mappings_type_1_item)

            return input_mappings_type_1

        input_mappings = _parse_input_mappings(d.pop("input_mappings", UNSET))

        _field_passthrough = d.pop("field_passthrough", UNSET)
        field_passthrough: list[FieldPassthrough] | Unset = UNSET
        if _field_passthrough is not UNSET:
            field_passthrough = []
            for field_passthrough_item_data in _field_passthrough:
                field_passthrough_item = FieldPassthrough.from_dict(field_passthrough_item_data)

                field_passthrough.append(field_passthrough_item)

        include_all_source_fields = d.pop("include_all_source_fields", UNSET)

        feature_extractor_config = cls(
            feature_extractor_name=feature_extractor_name,
            version=version,
            params=params,
            parameters=parameters,
            input_mappings=input_mappings,
            field_passthrough=field_passthrough,
            include_all_source_fields=include_all_source_fields,
        )

        feature_extractor_config.additional_properties = d
        return feature_extractor_config

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
