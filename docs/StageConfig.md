# StageConfig

Configuration for a single stage within a retriever.  Stages support dynamic configuration through template expressions using Jinja2 syntax.  IMPORTANT - Template Syntax:     - Use DOUBLE curly braces: {{INPUT.query}} (correct)     - Single curly braces will NOT work: {INPUT.query} (wrong - not substituted)     - Namespace names are CASE-INSENSITIVE: {{INPUT.query}}, {{inputs.query}}, {{input.query}}       all work identically  Template Namespaces (case-insensitive):     - INPUT / inputs / input: User-provided query parameters and inputs     - DOC / doc: Current document fields (for per-document logic)     - CONTEXT / context: Execution state (budget, timing, retriever metadata)     - STAGE / stage: Previous stage outputs (for cascading logic)  Examples:     Correct: {{INPUT.query_text}}, {{inputs.query}}, {{DOC.content_type}}     Correct: {{CONTEXT.budget_remaining}}, {{context.budget_remaining}}     Wrong:   {INPUT.query} - single braces won't be substituted

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage_name** | **str** | Human-readable stage instance name (REQUIRED). | 
**stage_type** | [**StageType**](StageType.md) | Functional category of the stage. Optional for creation requests; auto-inferred from &#x60;stage_id&#x60; when omitted. | [optional] 
**config** | **object** | Stage implementation parameters (REQUIRED). Must include &#x60;stage_id&#x60; key referencing a registered retriever stage. Supports template expressions using Jinja2 syntax resolved at execution time. Template namespaces support both uppercase and lowercase formats: {{INPUT.field}} or {{inputs.field}}, {{DOC.field}} or {{doc.field}}, {{CONTEXT.field}} or {{context.field}}, {{STAGE.field}} or {{stage.field}}. All formats work identically. Provide stage-specific configuration under &#x60;parameters&#x60;. | 
**batch_size** | **str** | Optional templated batch size expression evaluated per execution. Supports template variables: {{INPUT.page_size}}, {{inputs.page_size}}, {{CONTEXT.budget_remaining}}, etc. Both uppercase and lowercase namespace names are supported (e.g., INPUT/inputs, DOC/doc, CONTEXT/context, STAGE/stage). Defaults to stage-specific value when omitted. | [optional] 
**description** | **str** | User-facing description of the stage (OPTIONAL). | [optional] 

## Example

```python
from mixpeek.models.stage_config import StageConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StageConfig from a JSON string
stage_config_instance = StageConfig.from_json(json)
# print the JSON string representation of the object
print(StageConfig.to_json())

# convert the object into a dict
stage_config_dict = stage_config_instance.to_dict()
# create an instance of StageConfig from a dict
stage_config_from_dict = StageConfig.from_dict(stage_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


