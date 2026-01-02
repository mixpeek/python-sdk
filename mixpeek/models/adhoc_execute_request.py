from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adhoc_execute_request_input_schema import AdhocExecuteRequestInputSchema
    from ..models.adhoc_execute_request_inputs import AdhocExecuteRequestInputs
    from ..models.budget_limits import BudgetLimits
    from ..models.stage_config import StageConfig


T = TypeVar("T", bound="AdhocExecuteRequest")


@_attrs_define
class AdhocExecuteRequest:
    r"""Request to execute a retriever ad-hoc without persistence.

    This combines retriever creation parameters with execution inputs to allow
    one-time retrieval without saving the retriever configuration.

    Use Cases:
        - One-time queries without polluting retriever registry
        - Testing retriever configurations before persisting
        - Dynamic retrieval with varying stage configurations
        - Temporary search operations

    Behavior:
        - Retriever is NOT saved to database
        - Execution history is logged but marked as ad-hoc
        - Response includes X-Execution-Mode: adhoc header
        - execution_metadata.retriever_persisted = False

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
        - statistics: Stage metrics (duration_ms, input_count, output_count, etc.)
        - budget_used: Cumulative resource consumption (credits, time, tokens)

        Response Headers (streaming):
        - Content-Type: text/event-stream
        - Cache-Control: no-cache
        - Connection: keep-alive
        - X-Execution-Mode: adhoc

        Example streaming request:
        ```python
        response = requests.post(
            '/v1/retrievers/execute',
            json={
                'collection_identifiers': ['my_collection'],
                'input_schema': {'query': {'type': 'text', 'required': True}},
                'stages': [...],
                'inputs': {'query': 'machine learning'},
                'stream': True
            },
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

    Examples:
        Simple ad-hoc search:
            {
                "collection_identifiers": ["col_123"],
                "input_schema": {"query": {"type": "text", "required": True}},
                "stages": [{
                    "stage_name": "search",
                    "stage_type": "filter",
                    "config": {
                        "stage_id": "feature_search",
                        "parameters": {
                            "searches": [{
                                "feature_uri": "mixpeek://text_extractor@v1/embedding",
                                "query": {
                                    "input_mode": "text",
                                    "text": "{{INPUT.query}}"
                                },
                                "top_k": 100
                            }],
                            "final_top_k": 10
                        }
                    }
                }],
                "inputs": {"query": "machine learning"},
                "stream": false
            }

        Attributes:
            input_schema (AdhocExecuteRequestInputSchema): REQUIRED. Input schema defining expected inputs. Each key is an
                input name, value is a RetrieverInputSchemaField.
            stages (list[StageConfig]): REQUIRED. Ordered list of stage configurations. At least one stage is required for
                execution.
            inputs (AdhocExecuteRequestInputs): REQUIRED. Input values matching the input_schema. These values are passed to
                stages for parameterization.
            collection_identifiers (list[str] | Unset): Collection identifiers (names or IDs) to query. Can be collection
                names or IDs. Names are automatically resolved. Can be empty for query-only inference mode (e.g., LLM query
                analysis without documents).
            budget_limits (BudgetLimits | None | Unset): OPTIONAL. Budget limits for execution.
            stream (bool | Unset): Enable streaming execution to receive real-time stage updates via Server-Sent Events
                (SSE). NOT REQUIRED - defaults to False for standard execution.

                When stream=True:
                - Response Content-Type: text/event-stream
                - Events emitted: stage_start, stage_complete, stage_error, execution_complete, execution_error
                - Each event is formatted as: data: {json}\n\n
                - StreamStageEvent contains: event_type, execution_id, stage_name, stage_index, total_stages, documents
                (intermediate), statistics, budget_used


                When to use streaming:
                - Progress tracking for multi-stage pipelines
                - Displaying intermediate results as stages complete
                - Real-time budget and performance monitoring
                - Debugging pipeline execution


                When to skip streaming:
                - Single-stage or fast pipelines (<100ms)
                - No need for intermediate results
                - Minimizing overhead is critical Default: False.
    """

    input_schema: AdhocExecuteRequestInputSchema
    stages: list[StageConfig]
    inputs: AdhocExecuteRequestInputs
    collection_identifiers: list[str] | Unset = UNSET
    budget_limits: BudgetLimits | None | Unset = UNSET
    stream: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.budget_limits import BudgetLimits

        input_schema = self.input_schema.to_dict()

        stages = []
        for stages_item_data in self.stages:
            stages_item = stages_item_data.to_dict()
            stages.append(stages_item)

        inputs = self.inputs.to_dict()

        collection_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.collection_identifiers, Unset):
            collection_identifiers = self.collection_identifiers

        budget_limits: dict[str, Any] | None | Unset
        if isinstance(self.budget_limits, Unset):
            budget_limits = UNSET
        elif isinstance(self.budget_limits, BudgetLimits):
            budget_limits = self.budget_limits.to_dict()
        else:
            budget_limits = self.budget_limits

        stream = self.stream

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input_schema": input_schema,
                "stages": stages,
                "inputs": inputs,
            }
        )
        if collection_identifiers is not UNSET:
            field_dict["collection_identifiers"] = collection_identifiers
        if budget_limits is not UNSET:
            field_dict["budget_limits"] = budget_limits
        if stream is not UNSET:
            field_dict["stream"] = stream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adhoc_execute_request_input_schema import AdhocExecuteRequestInputSchema
        from ..models.adhoc_execute_request_inputs import AdhocExecuteRequestInputs
        from ..models.budget_limits import BudgetLimits
        from ..models.stage_config import StageConfig

        d = dict(src_dict)
        input_schema = AdhocExecuteRequestInputSchema.from_dict(d.pop("input_schema"))

        stages = []
        _stages = d.pop("stages")
        for stages_item_data in _stages:
            stages_item = StageConfig.from_dict(stages_item_data)

            stages.append(stages_item)

        inputs = AdhocExecuteRequestInputs.from_dict(d.pop("inputs"))

        collection_identifiers = cast(list[str], d.pop("collection_identifiers", UNSET))

        def _parse_budget_limits(data: object) -> BudgetLimits | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                budget_limits_type_0 = BudgetLimits.from_dict(data)

                return budget_limits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BudgetLimits | None | Unset, data)

        budget_limits = _parse_budget_limits(d.pop("budget_limits", UNSET))

        stream = d.pop("stream", UNSET)

        adhoc_execute_request = cls(
            input_schema=input_schema,
            stages=stages,
            inputs=inputs,
            collection_identifiers=collection_identifiers,
            budget_limits=budget_limits,
            stream=stream,
        )

        adhoc_execute_request.additional_properties = d
        return adhoc_execute_request

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
