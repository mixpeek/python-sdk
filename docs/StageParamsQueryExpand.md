# StageParamsQueryExpand

Parameters for query expansion stage.  This stage: 1. Takes your original query 2. Uses an LLM to generate semantically similar query variations 3. Executes feature_search for each variation (original + expansions) 4. Fuses results using Reciprocal Rank Fusion (RRF)  Example - Basic query expansion (copy and run):     ```python     {         \"stages\": [             {                 \"stage\": \"query_expand\",                 \"parameters\": {                     \"num_expansions\": 3,                     \"feature_search_config\": {                         \"query\": {\"text\": \"{{INPUT.query}}\"},                         \"feature_extractors\": [                             {\"field_name\": \"content.text\", \"embedding_model\": \"text\"}                         ],                         \"top_k\": 10                     }                 }             }         ]     }     ```  Example - With custom expansion prompt:     ```python     {         \"stages\": [             {                 \"stage\": \"query_expand\",                 \"parameters\": {                     \"num_expansions\": 5,                     \"expansion_prompt\": \"Generate {{NUM_EXPANSIONS}} alternative search queries for: {{QUERY}}. Focus on synonyms and related concepts. Return one query per line.\",                     \"feature_search_config\": {                         \"query\": {\"text\": \"{{INPUT.query}}\"},                         \"feature_extractors\": [                             {\"field_name\": \"content.text\", \"embedding_model\": \"text\"}                         ],                         \"top_k\": 20                     },                     \"rrf_k\": 60                 }             }         ]     }  Example - Multimodal query expansion:     ```python     {         \"stages\": [             {                 \"stage\": \"query_expand\",                 \"parameters\": {                     \"num_expansions\": 3,                     \"feature_search_config\": {                         \"query\": {\"text\": \"{{INPUT.query}}\", \"image\": \"{{INPUT.image_url}}\"},                         \"feature_extractors\": [                             {\"field_name\": \"content.text\", \"embedding_model\": \"text\"},                             {\"field_name\": \"content.image\", \"embedding_model\": \"multimodal\"}                         ],                         \"top_k\": 15                     },                     \"include_original\": true                 }             }         ]     }  How it works:     1. The original query (from feature_search_config.query.text) is sent to an LLM     2. LLM generates `num_expansions` alternative queries     3. feature_search runs for original query + each expansion     4. Results are fused using RRF: score = sum(1 / (k + rank)) across all queries     5. Documents appearing in multiple result sets get boosted  Why use query expansion:     - Handles vocabulary mismatch (user says \"car\", docs say \"vehicle\")     - Captures related concepts the user might not have thought of     - Improves recall without sacrificing precision (RRF handles fusion)     - Works with any feature_search configuration (text, image, multimodal)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_expansions** | **int** | Number of query variations to generate. More expansions &#x3D; better recall but slower. | [optional] [default to 3]
**expansion_prompt** | **str** | Custom prompt for query expansion. Use {{QUERY}} for the original query and {{NUM_EXPANSIONS}} for the count. If not provided, uses a default prompt. | [optional] [default to 'null']
**expansion_model** | **str** | LLM model to use for generating query expansions. | [optional] [default to 'gpt-4o-mini']
**feature_search_config** | **object** | Full feature_search configuration. This is the same config you would pass to a standalone feature_search stage. The query.text field will be replaced with each expanded query. | 
**include_original** | **bool** | Whether to include the original query in addition to expansions. | [optional] [default to True]
**rrf_k** | **int** | RRF constant k. Higher values give more weight to lower-ranked results. Default of 60 is standard. Use lower (20-40) for precision, higher (80-100) for recall. | [optional] [default to 60]
**fusion_strategy** | **str** | How to fuse results from multiple queries. &#39;rrf&#39; &#x3D; Reciprocal Rank Fusion (recommended), &#39;linear&#39; &#x3D; simple score averaging. | [optional] [default to 'rrf']
**deduplicate** | **bool** | Whether to deduplicate results by document_id before returning. | [optional] [default to True]

## Example

```python
from mixpeek.models.stage_params_query_expand import StageParamsQueryExpand

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsQueryExpand from a JSON string
stage_params_query_expand_instance = StageParamsQueryExpand.from_json(json)
# print the JSON string representation of the object
print(StageParamsQueryExpand.to_json())

# convert the object into a dict
stage_params_query_expand_dict = stage_params_query_expand_instance.to_dict()
# create an instance of StageParamsQueryExpand from a dict
stage_params_query_expand_from_dict = StageParamsQueryExpand.from_dict(stage_params_query_expand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


