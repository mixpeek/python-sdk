from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JsonTransformParameters")


@_attrs_define
class JsonTransformParameters:
    r"""Configuration for JSON Jinja template transformation stage.

    Stage Category: APPLY (1-1 transformation)

    Transformation: N documents → N documents (or fewer with fail_on_error=False)

    Purpose: Applies a Jinja2 template to each document in the retrieval pipeline,
    rendering the template with full document context and replacing the document
    with the parsed JSON output. Useful for reformatting documents to match
    external API schemas or restructuring data for downstream consumers.

    Performance: Template rendering is fast (<1ms per document). No caching is
    implemented as re-rendering is faster than cache overhead for typical
    document sizes. Processes documents sequentially with error handling.

    When to Use:
        - Reformat documents for external API calls (webhooks, workflows)
        - Rename or reorganize document fields for client consumption
        - Drop unnecessary properties to reduce response size
        - Expand or flatten nested arrays/objects
        - Apply conditional field inclusion based on document values
        - Create custom response schemas from standard document format

    When NOT to Use:
        - For filtering documents (use FILTER stages: structured_filter, llm_filter)
        - For sorting documents (use SORT stages: sort_relevance, rerank)
        - For enriching with new data (use APPLY stages: document_enrich)
        - For joining external data (use APPLY 1-N stages: taxonomy_enrich)

    Template Context:
        Templates have access to the full retriever template context:
        - DOC (or doc): Current document fields and metadata
        - INPUT (or input/inputs): Original query inputs from the search request
        - CONTEXT (or context): Execution context (namespace_id, internal_id, etc.)
        - STAGE (or stage): Current stage execution data and metadata

    Template Features:
        - Standard Jinja2 syntax with all built-in filters (tojson, length, etc.)
        - Conditional logic ({% if %}, {% elif %}, {% else %})
        - Loops and iteration ({% for item in items %})
        - Variable access with dot notation (DOC.metadata.field)
        - JSON filters for proper escaping ({{ value | tojson }})

    Error Handling:
        Documents that fail template rendering or JSON parsing can either
        skip with a warning (default) or fail the entire retrieval pipeline.
        Failed documents are tracked in stage metadata for observability.

    Operational Behavior:
        - Fast stage: runs in API layer (no Engine delegation)
        - Sequential processing: documents transformed one at a time
        - Error isolation: one document failure doesn't affect others (unless fail_on_error=True)
        - Schema replacement: output schema completely defined by template
        - Reports metrics to ClickHouse for performance monitoring

    Common Pipeline Position: FILTER → SORT → APPLY (this stage)

    Requirements:
        - template: REQUIRED
        - fail_on_error: OPTIONAL (defaults to False)

    Use Cases:
        - External API formatting: Format documents for webhook payloads
        - Response optimization: Remove unused fields to reduce bandwidth
        - Schema adaptation: Convert internal format to client-specific format
        - Conditional outputs: Include fields based on document properties
        - Array flattening: Transform nested structures to flat arrays

    Examples:
        Basic field selection and renaming:
        >>> template = '{"id": "{{ DOC.document_id }}", "text": "{{ DOC.content }}"}'

        Conditional field inclusion for external API:
        >>> template = '''
        ... {
        ...   "workflow": "{{ DOC.workflow_name }}",
        ...   "inputs": [
        ...     {"name": "variant_id", "value": "{{ DOC.variant_id }}"}
        ...     {% if DOC.asset_type == "VIDEO" %},
        ...     {"name": "video", "value": {"src": "{{ DOC.asset_url }}"}}
        ...     {% endif %}
        ...   ]
        ... }
        ... '''

        Array expansion with iteration:
        >>> template = '''
        ... {
        ...   "items": [
        ...     {% for item in DOC.tags %}
        ...     "{{ item }}"{% if not loop.last %},{% endif %}
        ...     {% endfor %}
        ...   ]
        ... }
        ... '''

        Nested field access and JSON escaping:
        >>> template = '{"user": "{{ DOC.metadata.user_id }}", "data": {{ DOC.raw_data | tojson }}}'

        Attributes:
            template (str | Unset): Jinja2 template string that must render to valid JSON. The template has access to full
                retriever context: - DOC (or doc): Current document fields and metadata - INPUT (or input/inputs): Original
                query inputs from search request - CONTEXT (or context): Execution context (namespace_id, internal_id) - STAGE
                (or stage): Current stage execution data Both uppercase and lowercase namespace formats work identically (DOC ==
                doc). The template must produce valid JSON syntax when rendered - invalid JSON will cause document to be skipped
                (unless fail_on_error=True). Supports all Jinja2 features: conditionals ({% if %}), loops ({% for %}), filters
                (| tojson, | length), variable access (DOC.metadata.field). Common patterns: - Field selection: {'id': '{{
                DOC.document_id }}'} - Conditional inclusion: {% if DOC.type == 'video' %}...{% endif %} - Array iteration: {%
                for item in DOC.tags %}...{% endfor %} - JSON escaping: {{ DOC.data | tojson }} Use cases: API formatting, field
                renaming, property filtering, structure flattening. Default: '{\\"id\\": \\"{{ DOC.document_id }}\\",
                \\"content\\": {{ DOC.content | tojson }}, \\"score\\": {{ DOC.score }}}'.
            fail_on_error (bool | Unset): OPTIONAL. Whether to fail the entire retrieval pipeline if any document
                transformation fails. Default: False. False (default): Skip failed documents with warning logged, continue
                processing remaining documents. Failed documents are tracked in stage metadata for observability and debugging.
                Use for lenient pipelines where partial results are acceptable (e.g., best-effort reformatting). True: Fail
                entire retrieval on first transformation error. Use for strict pipelines where all documents must transform
                successfully (e.g., critical API integrations where incomplete data would cause downstream failures). Failure
                causes: invalid template syntax, template rendering errors (missing fields), invalid JSON output from template,
                document missing required fields. Typical values: False for public APIs (resilient), True for internal workflows
                (data integrity critical). Default: False.
    """

    template: str | Unset = (
        '{\\"id\\": \\"{{ DOC.document_id }}\\", \\"content\\": {{ DOC.content | tojson }}, \\"score\\": {{ DOC.score }}}'
    )
    fail_on_error: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template = self.template

        fail_on_error = self.fail_on_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template is not UNSET:
            field_dict["template"] = template
        if fail_on_error is not UNSET:
            field_dict["fail_on_error"] = fail_on_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template = d.pop("template", UNSET)

        fail_on_error = d.pop("fail_on_error", UNSET)

        json_transform_parameters = cls(
            template=template,
            fail_on_error=fail_on_error,
        )

        json_transform_parameters.additional_properties = d
        return json_transform_parameters

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
