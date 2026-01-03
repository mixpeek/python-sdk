# AgentConfig

Agent configuration for session.  This config is immutable after session creation (similar to RetrieverConfig). To change agent config, create a new session.  Attributes:     model: LLM model identifier. Supported models:         - claude-3-5-sonnet-20241022 (recommended)         - claude-3-haiku-20240307 (faster, cheaper)         - claude-3-opus-20240229 (most capable)     temperature: Sampling temperature for LLM responses (0.0-2.0)         - 0.0-0.3: More deterministic, focused responses         - 0.5-0.7: Balanced creativity and coherence         - 0.8-2.0: More creative, varied responses     max_tokens: Maximum tokens per response (1-100000)     system_prompt: System prompt that defines agent behavior and persona     available_tools: List of tools the agent can call  Available Tools:     RETRIEVER TOOLS:     - list_retrievers: List available search pipelines     - get_retriever: Get retriever configuration     - explain_retriever: Understand how a retriever processes queries     - execute_retriever: Run a search query     - search_retrievers: Search for retrievers      COLLECTION TOOLS:     - list_collections: List document collections     - get_collection: Get collection details     - create_collection: Create new collection     - update_collection: Update collection     - delete_collection: Delete collection      TAXONOMY TOOLS:     - list_taxonomies: List classification schemas     - get_taxonomy: Get taxonomy details     - create_taxonomy: Create new taxonomy     - update_taxonomy: Update taxonomy     - delete_taxonomy: Delete taxonomy      REGISTRY TOOLS:     - list_stages: List available retriever stage types     - list_extractors: List available feature extractors      INGEST TOOLS:     - ingest_document: Add documents to a collection  Example:     ```python     config = AgentConfig(         model=\"claude-3-5-sonnet-20241022\",         temperature=0.7,         max_tokens=4096,         system_prompt=\"You are a helpful video search assistant.\",         available_tools=[             \"list_retrievers\",             \"execute_retriever\",             \"list_collections\"         ]     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | LLM model identifier. Options: &#39;gemini-2.0-flash&#39; (fastest, cheapest), &#39;gemini-2.5-pro&#39; (better quality), &#39;gpt-4o-mini&#39;, &#39;gpt-4o&#39; | [optional] [default to 'gemini-2.0-flash']
**temperature** | **float** | Sampling temperature for LLM responses (0.0-2.0). Lower values (0.0-0.3) are more deterministic. Higher values (0.8-2.0) are more creative. | [optional] [default to 0.7]
**max_tokens** | **int** | Maximum tokens per response | [optional] [default to 4096]
**system_prompt** | **str** | System prompt that defines agent behavior and persona | [optional] [default to 'You are a helpful AI assistant with access to Mixpeek\'s data infrastructure.']
**available_tools** | **List[str]** | List of tool names the agent can call. Available tools: RETRIEVER: list_retrievers, get_retriever, explain_retriever, execute_retriever, search_retrievers. COLLECTION: list_collections, get_collection, create_collection, update_collection, delete_collection. TAXONOMY: list_taxonomies, get_taxonomy, create_taxonomy, update_taxonomy, delete_taxonomy. REGISTRY: list_stages, list_extractors. INGEST: ingest_document. CLUSTER: list_clusters. OBJECT: get_object. | [optional] 

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


