# RetrieverStageDefinition

Public definition of a retriever stage available in the system.  Each stage represents a specific operation in a retrieval pipeline (filter, sort, enrich, etc). Use the `/v1/retrievers/stages` endpoint to discover available stages and their parameter schemas before creating retrievers.  Stage Registration:     - Stages are registered in the retriever stage registry     - Each stage has a unique ID, category, and parameter schema     - Parameter schemas are Pydantic models with full validation  Usage Flow:     1. Call GET /v1/retrievers/stages to list all available stages     2. Review parameter_schema for each stage to understand requirements     3. Compose stages into a retrieval pipeline     4. Create retriever via POST /v1/collections/{id}/retrievers  Example Workflow:     ```     # 1. Discover stages     GET /v1/retrievers/stages      # 2. Review attribute_filter schema     {       \"stage_id\": \"attribute_filter\",       \"description\": \"Filter documents by attribute conditions\",       \"category\": \"filter\",       \"parameter_schema\": {         \"type\": \"object\",         \"properties\": {           \"field\": {\"type\": \"string\"},           \"operator\": {\"enum\": [\"eq\", \"ne\", \"gt\", \"gte\", \"lt\", \"lte\", \"in\", \"nin\"]},           \"value\": {}         }       }     }      # 3. Create retriever using discovered stage     POST /v1/collections/col_123/retrievers     {       \"stages\": [         {           \"stage_name\": \"filter_active\",           \"stage_type\": \"filter\",           \"config\": {             \"stage_id\": \"attribute_filter\",             \"parameters\": {               \"field\": \"status\",               \"operator\": \"eq\",               \"value\": \"active\"             }           }         }       ]     }     ```  Requirements:     - stage_id: REQUIRED, unique identifier for the stage     - description: REQUIRED, human-readable description of stage purpose     - category: REQUIRED, transformation category (filter/sort/reduce/apply)     - icon: REQUIRED, UI icon identifier (Lucide React)     - parameter_schema: OPTIONAL, JSON Schema for stage parameters (null if no params)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage_id** | **str** | REQUIRED. Unique identifier for the stage type. Use this ID in the &#39;stage_id&#39; field when configuring stages in a retriever. Common stage IDs: &#39;attribute_filter&#39;, &#39;feature_filter&#39;, &#39;llm_filter&#39;, &#39;sort_relevance&#39;, &#39;document_enrich&#39;, &#39;taxonomy_enrich&#39;. Stage IDs are immutable and versioned separately from implementation. | 
**description** | **str** | REQUIRED. Human-readable description of what the stage does. Explains the stage&#39;s purpose, behavior, and when to use it. Use this to understand stage capabilities before using in pipelines. | 
**category** | [**StageCategory**](StageCategory.md) | REQUIRED. Transformation category defining how the stage processes documents. Categories: &#39;filter&#39; (subset, N→≤N), &#39;sort&#39; (reorder, N→N), &#39;reduce&#39; (aggregate, N→1), &#39;apply&#39; (enrich/expand, N→N or N→N*M). Use category to understand stage&#39;s impact on document flow. | 
**icon** | **str** | REQUIRED. Lucide React icon identifier for UI rendering. Used by frontend clients to display stage icons in pipeline builders. See https://lucide.dev for available icon names. Common icons: &#39;filter&#39; (attribute_filter), &#39;search&#39; (semantic), &#39;brain-circuit&#39; (LLM), &#39;arrow-up-down&#39; (sort). | 
**parameter_schema** | **object** | OPTIONAL. JSON Schema defining the parameters this stage accepts. Contains full Pydantic schema including types, descriptions, examples, and validation rules for all stage parameters. Use this schema to validate stage configurations before submission. Null if stage requires no parameters (rare). Schema includes: field types, required fields, defaults, validation constraints, field descriptions, and usage examples. | [optional] 

## Example

```python
from mixpeek.models.retriever_stage_definition import RetrieverStageDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverStageDefinition from a JSON string
retriever_stage_definition_instance = RetrieverStageDefinition.from_json(json)
# print the JSON string representation of the object
print(RetrieverStageDefinition.to_json())

# convert the object into a dict
retriever_stage_definition_dict = retriever_stage_definition_instance.to_dict()
# create an instance of RetrieverStageDefinition from a dict
retriever_stage_definition_from_dict = RetrieverStageDefinition.from_dict(retriever_stage_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


