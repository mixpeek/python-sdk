from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RetrieverExecutionRequestInputs")


@_attrs_define
class RetrieverExecutionRequestInputs:
    """Runtime inputs for the retriever mapped to the input schema. Keys must match the retriever's input_schema field
    names. Values depend on field types (text, vector, filters, etc.). REQUIRED unless all retriever inputs have
    defaults.

    Common input keys:
    - 'query': Text search query
    - 'embedding': Pre-computed vector for search
    - 'top_k': Number of results to return
    - 'min_score': Minimum relevance threshold
    - Any custom fields defined in input_schema


    **Template Syntax** (Jinja2):

    Namespaces (uppercase or lowercase):
    - `INPUT` / `input`: Query inputs (e.g., `{{INPUT.query}}`)
    - `DOC` / `doc`: Document fields (e.g., `{{DOC.payload.title}}`)
    - `CONTEXT` / `context`: Execution context
    - `STAGE` / `stage`: Stage configuration
    - `SECRET` / `secret`: Vault secrets (e.g., `{{SECRET.api_key}}`)

    Accessing Data:
    - Dot notation: `{{DOC.payload.metadata.title}}`
    - Bracket notation: `{{DOC.payload['special-key']}}`
    - Array index: `{{DOC.items[0]}}`, `{{DOC.tags[2]}}`
    - Array first/last: `{{DOC.items | first}}`, `{{DOC.items | last}}`

    Array Operations:
    - Iterate: `{% for item in DOC.tags %}{{item}}{% endfor %}`
    - Extract key: `{{DOC.items | map(attribute='name') | list}}`
    - Join: `{{DOC.tags | join(', ')}}`
    - Length: `{{DOC.items | length}}`
    - Slice: `{{DOC.items[:5]}}`

    Conditionals:
    - If: `{% if DOC.status == 'active' %}...{% endif %}`
    - If-else: `{% if DOC.score > 0.8 %}high{% else %}low{% endif %}`
    - Ternary: `{{'yes' if DOC.enabled else 'no'}}`

    Built-in Functions: `max`, `min`, `abs`, `round`, `ceil`, `floor`
    Custom Filters: `slugify` (URL-safe), `bool` (truthy coercion), `tojson` (JSON encode)

    S3 URLs: Internal S3 URLs (s3://bucket/key) are automatically presigned when accessed via DOC namespace.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retriever_execution_request_inputs = cls()

        retriever_execution_request_inputs.additional_properties = d
        return retriever_execution_request_inputs

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
