# StageParamsCodeExecution

Configuration for executing custom code in secure isolated sandboxes.  **Stage Category**: ENRICH (1-1 Enrichment)  **Transformation**: N documents → N documents (same count, expanded schema)  **Purpose**: Executes user-provided code in isolated sandboxes to compute custom enrichments for each document. The code receives all documents as a JSON array and must return a list of results matching the input length.  **When to Use**:     - Custom transformations not covered by built-in stages     - Data extraction (regex, parsing)     - Unit conversions and normalization     - Cross-document computations (relative scores, rankings)     - Prototyping custom enrichment logic     - Complex string manipulations  **When NOT to Use**:     - Simple field transformations (use json_transform)     - LLM-based enrichment (use llm_enrich)     - External API calls (use api_call stage)     - When deterministic built-in stages suffice  **Operational Behavior**:     - Creates ONE sandbox per stage execution (~200ms startup)     - Passes ALL documents as JSON array to user code     - User code must set `result` to list matching input length     - Merges results back into documents at output_field     - Supports Python, TypeScript, and JavaScript  **Template Support**:     - {{INPUT.*}}: Pipeline input parameters (evaluated before execution)     - {{CONTEXT.*}}: Execution context (namespace_id, internal_id)     - {{SECRET.*}}: Organization vault secrets (e.g., {{SECRET.api_key}})     - Documents are passed as runtime `docs` variable (NOT a template)  **Using Secrets**:     Secrets stored in your organization vault can be referenced in code and env:     - In env vars: {\"API_KEY\": \"{{SECRET.stripe_api_key}}\"}     - In code: \"api_key = '{{SECRET.my_key}}'\"  (less common, prefer env vars)     Secrets are automatically loaded from the vault and redacted in error messages.  Requirements:     - code: REQUIRED, code to execute (receives `docs`, must set `result`)     - output_field: REQUIRED, where to store computed results     - language: OPTIONAL, execution language (default: python)     - timeout_ms: OPTIONAL, execution timeout (default: 5000ms)  Examples:     Word count enrichment:         ```json         {             \"code\": \"result = [{'word_count': len(d.get('content', '').split())} for d in docs]\",             \"output_field\": \"text_stats\"         }         ```      Cross-document relative scores:         ```json         {             \"code\": \"avg = sum(d.get('score', 0) for d in docs) / len(docs)\\nresult = [{'relative': d.get('score', 0) / avg} for d in docs]\",             \"output_field\": \"score_analysis\"         }         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code to execute in the sandbox. Receives &#39;docs&#39; variable (list of document dicts). Must set &#39;result&#39; variable to a list matching input length. Supports {{INPUT.*}}, {{CONTEXT.*}}, and {{SECRET.*}} templates. | [optional] [default to 'result = [{\'word_count\': len(d.get(\'content\', \'\').split())} for d in docs]']
**language** | **str** | Execution language. Python recommended for most use cases. | [optional] [default to 'python']
**output_field** | **str** | Document field path where results are merged. Dot notation supported: &#39;metadata.computed&#39; | [optional] [default to 'metadata.computed']
**result_variable** | **str** | Variable name containing the output list in your code. Must be a JSON-serializable list with length &#x3D;&#x3D; len(docs). | [optional] [default to 'result']
**timeout_ms** | **int** | Execution timeout in milliseconds (100ms-30s, default 5s) | [optional] [default to 5000]
**max_output_size** | **int** | Max output size in bytes (default 100KB, max 1MB) | [optional] [default to 100000]
**env** | **Dict[str, str]** | Environment variables available during execution. Supports INPUT and SECRET templates: {&#39;API_KEY&#39;: &#39;{{SECRET.stripe_key}}&#39;, &#39;USER_ID&#39;: &#39;{{INPUT.user_id}}&#39;} | [optional] 
**on_error** | [**ErrorHandling**](ErrorHandling.md) | &#39;skip&#39;: On error, return input documents unchanged. &#39;raise&#39;: Fail entire pipeline on any error. | [optional] 

## Example

```python
from mixpeek.models.stage_params_code_execution import StageParamsCodeExecution

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsCodeExecution from a JSON string
stage_params_code_execution_instance = StageParamsCodeExecution.from_json(json)
# print the JSON string representation of the object
print(StageParamsCodeExecution.to_json())

# convert the object into a dict
stage_params_code_execution_dict = stage_params_code_execution_instance.to_dict()
# create an instance of StageParamsCodeExecution from a dict
stage_params_code_execution_from_dict = StageParamsCodeExecution.from_dict(stage_params_code_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


