# AdhocExecuteRequest

Request to execute a retriever ad-hoc without persistence.  This combines retriever creation parameters with execution inputs to allow one-time retrieval without saving the retriever configuration.  Use Cases:     - One-time queries without polluting retriever registry     - Testing retriever configurations before persisting     - Dynamic retrieval with varying stage configurations     - Temporary search operations  Behavior:     - Retriever is NOT saved to database     - Execution history is logged but marked as ad-hoc     - Response includes X-Execution-Mode: adhoc header     - execution_metadata.retriever_persisted = False  Streaming Execution (stream=True):     When streaming is enabled, the response uses Server-Sent Events (SSE) format     with Content-Type: text/event-stream. Each stage emits events as it executes:      Event Types:     - stage_start: Emitted when a stage begins execution     - stage_complete: Emitted when a stage finishes with results     - stage_error: Emitted if a stage encounters an error     - execution_complete: Emitted after all stages finish successfully     - execution_error: Emitted if the entire execution fails      Each event is a StreamStageEvent containing:     - event_type: The type of event     - execution_id: Unique execution identifier     - stage_name: Human-readable stage name     - stage_index: Zero-based stage position     - total_stages: Total number of stages     - documents: Intermediate results (for stage_complete)     - statistics: Stage metrics (duration_ms, input_count, output_count, etc.)     - budget_used: Cumulative resource consumption (credits, time, tokens)      Response Headers (streaming):     - Content-Type: text/event-stream     - Cache-Control: no-cache     - Connection: keep-alive     - X-Execution-Mode: adhoc      Example streaming request:     ```python     response = requests.post(         '/v1/retrievers/execute',         json={             'collection_identifiers': ['my_collection'],             'input_schema': {'query': {'type': 'text', 'required': True}},             'stages': [...],             'inputs': {'query': 'machine learning'},             'stream': True         },         stream=True     )     for line in response.iter_lines():         if line.startswith(b'data: '):             event = json.loads(line[6:])             print(f\"{event['event_type']}: {event.get('stage_name')}\")     ```  Standard Execution (stream=False, default):     Returns a single ExecuteRetrieverResponse with final documents,     pagination, and aggregate statistics after all stages complete.  Examples:     Simple ad-hoc search:         {             \"collection_identifiers\": [\"col_123\"],             \"input_schema\": {\"query\": {\"type\": \"text\", \"required\": True}},             \"stages\": [{                 \"stage_name\": \"search\",                 \"stage_type\": \"filter\",                 \"config\": {                     \"stage_id\": \"feature_search\",                     \"parameters\": {                         \"searches\": [{                             \"feature_uri\": \"mixpeek://text_extractor@v1/embedding\",                             \"query\": {                                 \"input_mode\": \"text\",                                 \"text\": \"{{INPUT.query}}\"                             },                             \"top_k\": 100                         }],                         \"final_top_k\": 10                     }                 }             }],             \"inputs\": {\"query\": \"machine learning\"},             \"stream\": false         }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_identifiers** | **List[str]** | Collection identifiers (names or IDs) to query. Can be collection names or IDs. Names are automatically resolved. Can be empty for query-only inference mode (e.g., LLM query analysis without documents). | [optional] 
**input_schema** | [**Dict[str, RetrieverInputSchemaFieldInput]**](RetrieverInputSchemaFieldInput.md) | REQUIRED. Input schema defining expected inputs. Each key is an input name, value is a RetrieverInputSchemaField. | 
**stages** | [**List[StageConfig]**](StageConfig.md) | REQUIRED. Ordered list of stage configurations. At least one stage is required for execution. | 
**inputs** | **Dict[str, object]** | REQUIRED. Input values matching the input_schema. These values are passed to stages for parameterization. | 
**budget_limits** | [**BudgetLimits**](BudgetLimits.md) | OPTIONAL. Budget limits for execution. | [optional] 
**stream** | **bool** | Enable streaming execution to receive real-time stage updates via Server-Sent Events (SSE). NOT REQUIRED - defaults to False for standard execution.   When stream&#x3D;True: - Response Content-Type: text/event-stream - Events emitted: stage_start, stage_complete, stage_error, execution_complete, execution_error - Each event is formatted as: data: {json}\\n\\n - StreamStageEvent contains: event_type, execution_id, stage_name, stage_index, total_stages, documents (intermediate), statistics, budget_used   When to use streaming: - Progress tracking for multi-stage pipelines - Displaying intermediate results as stages complete - Real-time budget and performance monitoring - Debugging pipeline execution   When to skip streaming: - Single-stage or fast pipelines (&lt;100ms) - No need for intermediate results - Minimizing overhead is critical | [optional] [default to False]

## Example

```python
from mixpeek.models.adhoc_execute_request import AdhocExecuteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdhocExecuteRequest from a JSON string
adhoc_execute_request_instance = AdhocExecuteRequest.from_json(json)
# print the JSON string representation of the object
print(AdhocExecuteRequest.to_json())

# convert the object into a dict
adhoc_execute_request_dict = adhoc_execute_request_instance.to_dict()
# create an instance of AdhocExecuteRequest from a dict
adhoc_execute_request_from_dict = AdhocExecuteRequest.from_dict(adhoc_execute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


