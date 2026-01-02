from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cursor_pagination_params import CursorPaginationParams
    from ..models.execute_retriever_request_inputs import ExecuteRetrieverRequestInputs
    from ..models.keyset_pagination_params import KeysetPaginationParams
    from ..models.offset_pagination_params import OffsetPaginationParams
    from ..models.scroll_pagination_params import ScrollPaginationParams


T = TypeVar("T", bound="ExecuteRetrieverRequest")


@_attrs_define
class ExecuteRetrieverRequest:
    """Request to execute a retriever with optional streaming support.

    Inherits all fields from RetrieverExecutionRequest including:
    - inputs: Runtime input values matching the retriever's input_schema
    - pagination: Pagination configuration (cursor, offset, etc.)
    - stream: Enable SSE streaming for real-time stage updates

    Streaming Execution (stream=True):
        When streaming is enabled, the response uses Server-Sent Events (SSE) format
        with Content-Type: text/event-stream. Each stage emits events as it executes:

        Event Types:
        - stage_start: Emitted when a stage begins execution
        - stage_complete: Emitted when a stage finishes with results
        - stage_error: Emitted if a stage encounters an error
        - execution_complete: Emitted after all stages finish successfully
        - execution_error: Emitted if the entire execution fails

        Each event is a StreamStageEvent containing:
        - event_type: The type of event
        - execution_id: Unique execution identifier
        - stage_name: Human-readable stage name
        - stage_index: Zero-based stage position
        - total_stages: Total number of stages
        - documents: Intermediate results (for stage_complete)
        - statistics: Stage metrics (duration, counts, etc.)
        - budget_used: Cumulative resource consumption

        Example streaming client:
        ```python
        response = requests.post(
            '/v1/retrievers/{id}/execute',
            json={'inputs': {...}, 'stream': True},
            stream=True
        )
        for line in response.iter_lines():
            if line.startswith(b'data: '):
                event = json.loads(line[6:])
                print(f"{event['event_type']}: {event.get('stage_name')}")
        ```

    Standard Execution (stream=False, default):
        Returns a single ExecuteRetrieverResponse with final documents,
        pagination, and aggregate statistics after all stages complete.

        Attributes:
            inputs (ExecuteRetrieverRequestInputs | Unset): Runtime inputs for the retriever mapped to the input schema.
                Keys must match the retriever's input_schema field names. Values depend on field types (text, vector, filters,
                etc.). REQUIRED unless all retriever inputs have defaults.

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
            pagination (CursorPaginationParams | KeysetPaginationParams | OffsetPaginationParams | ScrollPaginationParams |
                Unset): Pagination strategy configuration. Defaults to cursor-based pagination with limit=20.

                IMPORTANT: Pagination params do NOT support template variables ({{INPUT.x}} or {{DOCUMENT.x}}). Pagination is a
                request-level parameter for slicing results, separate from pipeline business logic. Pass cursor/limit values
                directly from your client code. Cursor values come from the previous response's pagination.cursor field.

                Supported Methods:
                - CURSOR (default): Best for infinite scroll, stateless, opaque token
                - KEYSET: Most efficient, requires stable sort, stateless
                - OFFSET: Traditional page numbers, can have drift issues
                - SCROLL: Server-side state, best for bulk exports


                Use CURSOR for:
                - Infinite scroll UIs (mobile apps, feeds, timelines)
                - Real-time updates where consistency matters
                - When you can't jump to arbitrary pages


                Use KEYSET for:
                - Maximum performance with large result sets
                - Stable sort fields (e.g., score DESC, id ASC)
                - When you need truly stateless pagination


                Use OFFSET for:
                - Traditional page UIs with page numbers
                - When users need to jump to specific pages
                - Smaller result sets where drift is acceptable


                Use SCROLL for:
                - Bulk exports or processing large datasets
                - When you need to iterate through all results
                - Background jobs with progress tracking


                Example (cursor - first page):
                {"method": "cursor", "limit": 20, "cursor": null}

                Example (cursor - next page, using cursor from previous response):
                {"method": "cursor", "limit": 20, "cursor": "eyJvZmZzZXQiOjIwfQ=="}

                Example (offset):
                {"method": "offset", "page_size": 25, "page_number": 2}

                Example (keyset):
                {"method": "keyset", "limit": 20, "after": {"score": 0.73, "id": "doc_20"}}
            stream (bool | Unset): Enable streaming execution to receive real-time stage updates via Server-Sent Events
                (SSE). NOT REQUIRED - defaults to False for standard execution.

                When stream=True:
                - Response uses text/event-stream content type
                - Each stage completion emits a StreamStageEvent
                - Events include: stage_start, stage_complete, stage_error, execution_complete
                - Clients receive intermediate results and statistics as stages execute
                - Useful for progress tracking, debugging, and partial result display


                When stream=False (default):
                - Response returns after all stages complete
                - Returns a single RetrieverExecutionResponse with final results
                - Lower overhead for simple queries


                Use streaming when:
                - You want to show real-time progress to users
                - You need to display intermediate results
                - Pipeline has many stages or long-running operations
                - Debugging or monitoring pipeline performance


                Example streaming client (JavaScript):
                ```javascript
                const eventSource = new EventSource('/v1/retrievers/ret_123/execute?stream=true');
                eventSource.onmessage = (event) => {
                  const stageEvent = JSON.parse(event.data);
                  if (stageEvent.event_type === 'stage_complete') {
                    console.log(`Stage ${stageEvent.stage_name} completed`);
                    console.log(`Documents: ${stageEvent.documents.length}`);
                  }
                };
                ```


                Example streaming client (Python):
                ```python
                import requests
                response = requests.post('/v1/retrievers/ret_123/execute',
                                        json={'inputs': {...}, 'stream': True},
                                        stream=True)
                for line in response.iter_lines():
                    if line.startswith(b'data: '):
                        event = json.loads(line[6:])
                        print(f"Stage {event['stage_name']}: {event['event_type']}")
                ``` Default: False.
    """

    inputs: ExecuteRetrieverRequestInputs | Unset = UNSET
    pagination: (
        CursorPaginationParams | KeysetPaginationParams | OffsetPaginationParams | ScrollPaginationParams | Unset
    ) = UNSET
    stream: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cursor_pagination_params import CursorPaginationParams
        from ..models.offset_pagination_params import OffsetPaginationParams
        from ..models.scroll_pagination_params import ScrollPaginationParams

        inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        pagination: dict[str, Any] | Unset
        if isinstance(self.pagination, Unset):
            pagination = UNSET
        elif isinstance(self.pagination, OffsetPaginationParams):
            pagination = self.pagination.to_dict()
        elif isinstance(self.pagination, CursorPaginationParams):
            pagination = self.pagination.to_dict()
        elif isinstance(self.pagination, ScrollPaginationParams):
            pagination = self.pagination.to_dict()
        else:
            pagination = self.pagination.to_dict()

        stream = self.stream

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if stream is not UNSET:
            field_dict["stream"] = stream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_pagination_params import CursorPaginationParams
        from ..models.execute_retriever_request_inputs import ExecuteRetrieverRequestInputs
        from ..models.keyset_pagination_params import KeysetPaginationParams
        from ..models.offset_pagination_params import OffsetPaginationParams
        from ..models.scroll_pagination_params import ScrollPaginationParams

        d = dict(src_dict)
        _inputs = d.pop("inputs", UNSET)
        inputs: ExecuteRetrieverRequestInputs | Unset
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = ExecuteRetrieverRequestInputs.from_dict(_inputs)

        def _parse_pagination(
            data: object,
        ) -> CursorPaginationParams | KeysetPaginationParams | OffsetPaginationParams | ScrollPaginationParams | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pagination_type_0 = OffsetPaginationParams.from_dict(data)

                return pagination_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pagination_type_1 = CursorPaginationParams.from_dict(data)

                return pagination_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pagination_type_2 = ScrollPaginationParams.from_dict(data)

                return pagination_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            pagination_type_3 = KeysetPaginationParams.from_dict(data)

            return pagination_type_3

        pagination = _parse_pagination(d.pop("pagination", UNSET))

        stream = d.pop("stream", UNSET)

        execute_retriever_request = cls(
            inputs=inputs,
            pagination=pagination,
            stream=stream,
        )

        execute_retriever_request.additional_properties = d
        return execute_retriever_request

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
