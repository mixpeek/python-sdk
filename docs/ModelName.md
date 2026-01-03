# ModelName

REQUIRED when enabled=True. Specific LLM model to use for cluster labeling. All models are defined as enums for type safety.  OpenAI Models (provider='openai'): - gpt-4o-2024-08-06: Highest quality, best for production ($2.50/$10 per 1M tokens) - gpt-4o-mini-2024-07-18: Cost-effective, recommended for most use cases ($0.15/$0.60 per 1M tokens) - gpt-4.1-2025-04-14: Latest model, future-proofed - gpt-4.1-mini-2025-04-14: Latest cost-optimized model - o3-mini-2025-01-31: Advanced reasoning, best for complex clustering  Google Models (provider='google'): - gemini-2.0-flash: Fastest, latest multimodal model, recommended ($0.075/$0.30 per 1M tokens) - gemini-2.0-flash-exp: Experimental version with latest features ($0.075/$0.30 per 1M tokens)  Anthropic Models (provider='anthropic'): - claude-3-5-sonnet-20241022: Best reasoning, 200K context ($3/$15 per 1M tokens) - claude-3-5-haiku-20241022: Fast, cost-effective ($0.25/$1.25 per 1M tokens)  Recommendation: - Use gemini-2.0-flash (DEFAULT) - cheapest option with multimodal support - Use gpt-4o-mini-2024-07-18 for OpenAI compatibility - Use gpt-4o-2024-08-06 for highest quality when cost is not a concern

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from mixpeek.models.model_name import ModelName

# TODO update the JSON string below
json = "{}"
# create an instance of ModelName from a JSON string
model_name_instance = ModelName.from_json(json)
# print the JSON string representation of the object
print(ModelName.to_json())

# convert the object into a dict
model_name_dict = model_name_instance.to_dict()
# create an instance of ModelName from a dict
model_name_from_dict = ModelName.from_dict(model_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


