# AgentConfig

Agent configuration for session.  This config is immutable after session creation (similar to RetrieverConfig). To change agent config, create a new session.  Attributes:     model: LLM model identifier. Supported models:         - gemini-2.0-flash (fastest, cheapest)         - gemini-2.5-pro (better quality)         - gpt-4o-mini, gpt-4o     temperature: Sampling temperature for LLM responses (0.0-2.0)         - 0.0-0.3: More deterministic, focused responses         - 0.5-0.7: Balanced creativity and coherence         - 0.8-2.0: More creative, varied responses     max_tokens: Maximum tokens per response (1-100000)     system_prompt: System prompt that defines agent behavior and persona     available_tools: List of tools the agent can call (see AvailableTool enum)  Example:     ```python     config = AgentConfig(         model=\"gemini-2.0-flash\",         temperature=0.7,         max_tokens=4096,         system_prompt=\"You are a helpful video search assistant.\",         available_tools=[             \"smart_search\",             \"execute_retriever\",             \"list_collections\"         ]     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | LLM model identifier. Options: &#39;gemini-2.0-flash&#39; (fastest, cheapest), &#39;gemini-2.5-pro&#39; (better quality), &#39;gpt-4o-mini&#39;, &#39;gpt-4o&#39; | [optional] [default to 'gemini-2.0-flash']
**temperature** | **float** | Sampling temperature for LLM responses (0.0-2.0). Lower values (0.0-0.3) are more deterministic. Higher values (0.8-2.0) are more creative. | [optional] [default to 0.7]
**max_tokens** | **int** | Maximum tokens per response | [optional] [default to 4096]
**system_prompt** | **str** | System prompt that defines agent behavior and persona | [optional] [default to 'You are a helpful AI assistant with access to Mixpeek\'s data infrastructure.']
**available_tools** | **List[str]** | List of tool names the agent can call. See AvailableTool enum for full list. Key tools: smart_search (natural language search), execute_retriever, execute_adhoc_retriever, list_collections, list_retrievers, list_buckets, create_upload, analyze_sample_with_pipeline, export_manifest, generate_manifest, detect_intent. | [optional] 

## Example

```python
from mixpeek.models.agent_config import AgentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AgentConfig from a JSON string
agent_config_instance = AgentConfig.from_json(json)
# print the JSON string representation of the object
print(AgentConfig.to_json())

# convert the object into a dict
agent_config_dict = agent_config_instance.to_dict()
# create an instance of AgentConfig from a dict
agent_config_from_dict = AgentConfig.from_dict(agent_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


