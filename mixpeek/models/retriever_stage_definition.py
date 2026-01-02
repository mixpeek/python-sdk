from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stage_category import StageCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retriever_stage_definition_parameter_schema_type_0 import RetrieverStageDefinitionParameterSchemaType0


T = TypeVar("T", bound="RetrieverStageDefinition")


@_attrs_define
class RetrieverStageDefinition:
    """Public definition of a retriever stage available in the system.

    Each stage represents a specific operation in a retrieval pipeline (filter, sort,
    enrich, etc). Use the `/v1/retrievers/stages` endpoint to discover available stages
    and their parameter schemas before creating retrievers.

    Stage Registration:
        - Stages are registered in the retriever stage registry
        - Each stage has a unique ID, category, and parameter schema
        - Parameter schemas are Pydantic models with full validation

    Usage Flow:
        1. Call GET /v1/retrievers/stages to list all available stages
        2. Review parameter_schema for each stage to understand requirements
        3. Compose stages into a retrieval pipeline
        4. Create retriever via POST /v1/collections/{id}/retrievers

    Example Workflow:
        ```
        # 1. Discover stages
        GET /v1/retrievers/stages

        # 2. Review attribute_filter schema
        {
          "stage_id": "attribute_filter",
          "description": "Filter documents by attribute conditions",
          "category": "filter",
          "parameter_schema": {
            "type": "object",
            "properties": {
              "field": {"type": "string"},
              "operator": {"enum": ["eq", "ne", "gt", "gte", "lt", "lte", "in", "nin"]},
              "value": {}
            }
          }
        }

        # 3. Create retriever using discovered stage
        POST /v1/collections/col_123/retrievers
        {
          "stages": [
            {
              "stage_name": "filter_active",
              "stage_type": "filter",
              "config": {
                "stage_id": "attribute_filter",
                "parameters": {
                  "field": "status",
                  "operator": "eq",
                  "value": "active"
                }
              }
            }
          ]
        }
        ```

    Requirements:
        - stage_id: REQUIRED, unique identifier for the stage
        - description: REQUIRED, human-readable description of stage purpose
        - category: REQUIRED, transformation category (filter/sort/reduce/apply)
        - icon: REQUIRED, UI icon identifier (Lucide React)
        - parameter_schema: OPTIONAL, JSON Schema for stage parameters (null if no params)

        Attributes:
            stage_id (str): REQUIRED. Unique identifier for the stage type. Use this ID in the 'stage_id' field when
                configuring stages in a retriever. Common stage IDs: 'attribute_filter', 'feature_filter', 'llm_filter',
                'sort_relevance', 'document_enrich', 'taxonomy_enrich'. Stage IDs are immutable and versioned separately from
                implementation.
            description (str): REQUIRED. Human-readable description of what the stage does. Explains the stage's purpose,
                behavior, and when to use it. Use this to understand stage capabilities before using in pipelines.
            category (StageCategory): Retriever stage categories organized by transformation pattern.

                Values:
                    FILTER: Subset of input documents (N → ≤N, same schema)
                        - Removes documents that don't match criteria
                        - Examples: attribute_filter, feature_filter, llm_filter
                        - Use for: Removing irrelevant results, applying business rules
                        - Performance: Fast (attribute) to slow (LLM)

                    SORT: Reorders documents (N → N, same schema, different order)
                        - Changes document ordering based on criteria
                        - Examples: sort_relevance, sort_attribute
                        - Use for: Ordering by relevance, recency, custom fields
                        - Performance: Fast (in-memory sort)

                    REDUCE: Aggregates to summary (N → 1, new schema)
                        - Combines multiple documents into one summary
                        - Examples: aggregate_stats, group_by
                        - Use for: Summaries, statistics, reports
                        - Performance: Varies by aggregation logic

                    APPLY: Enrichment or expansion (N → N or N*M)
                        - 1-1: Enriches each doc (N → N, expanded schema)
                        - 1-N: Expands each doc (N → N*M, new/same schema)
                        - Examples: document_enrich, taxonomy_enrich, llm_enrich
                        - Use for: Adding related data, tagging, recursive lookups
                        - Performance: Moderate (DB) to slow (LLM)

                    ENRICH: Document enrichment (N → N, potentially expanded schema)
                        - Adds computed fields to each document
                        - Examples: code_execution, llm_enrich, taxonomy_enrich
                        - Use for: Custom transformations, data extraction, LLM processing
                        - Performance: Varies (fast for code, slow for LLM)

                Pipeline Patterns:
                    - Basic: FILTER → SORT
                    - Enriched: FILTER → SORT → APPLY
                    - Tag expansion: FILTER → APPLY (1-N)
                    - Summary: FILTER → SORT → REDUCE
            icon (str): REQUIRED. Lucide React icon identifier for UI rendering. Used by frontend clients to display stage
                icons in pipeline builders. See https://lucide.dev for available icon names. Common icons: 'filter'
                (attribute_filter), 'search' (semantic), 'brain-circuit' (LLM), 'arrow-up-down' (sort).
            parameter_schema (None | RetrieverStageDefinitionParameterSchemaType0 | Unset): OPTIONAL. JSON Schema defining
                the parameters this stage accepts. Contains full Pydantic schema including types, descriptions, examples, and
                validation rules for all stage parameters. Use this schema to validate stage configurations before submission.
                Null if stage requires no parameters (rare). Schema includes: field types, required fields, defaults, validation
                constraints, field descriptions, and usage examples.
    """

    stage_id: str
    description: str
    category: StageCategory
    icon: str
    parameter_schema: None | RetrieverStageDefinitionParameterSchemaType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.retriever_stage_definition_parameter_schema_type_0 import (
            RetrieverStageDefinitionParameterSchemaType0,
        )

        stage_id = self.stage_id

        description = self.description

        category = self.category.value

        icon = self.icon

        parameter_schema: dict[str, Any] | None | Unset
        if isinstance(self.parameter_schema, Unset):
            parameter_schema = UNSET
        elif isinstance(self.parameter_schema, RetrieverStageDefinitionParameterSchemaType0):
            parameter_schema = self.parameter_schema.to_dict()
        else:
            parameter_schema = self.parameter_schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage_id": stage_id,
                "description": description,
                "category": category,
                "icon": icon,
            }
        )
        if parameter_schema is not UNSET:
            field_dict["parameter_schema"] = parameter_schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.retriever_stage_definition_parameter_schema_type_0 import (
            RetrieverStageDefinitionParameterSchemaType0,
        )

        d = dict(src_dict)
        stage_id = d.pop("stage_id")

        description = d.pop("description")

        category = StageCategory(d.pop("category"))

        icon = d.pop("icon")

        def _parse_parameter_schema(data: object) -> None | RetrieverStageDefinitionParameterSchemaType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parameter_schema_type_0 = RetrieverStageDefinitionParameterSchemaType0.from_dict(data)

                return parameter_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RetrieverStageDefinitionParameterSchemaType0 | Unset, data)

        parameter_schema = _parse_parameter_schema(d.pop("parameter_schema", UNSET))

        retriever_stage_definition = cls(
            stage_id=stage_id,
            description=description,
            category=category,
            icon=icon,
            parameter_schema=parameter_schema,
        )

        retriever_stage_definition.additional_properties = d
        return retriever_stage_definition

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
