# LLMLabeling

Configuration for LLM-based cluster labeling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether to generate labels for clusters using LLM | [optional] [default to False]
**provider** | **str** | LLM provider to use for labeling. Supported: &#39;openai&#39;, &#39;google&#39; | [optional] 
**model_name** | **str** | LLM model identifier. For OpenAI defaults to &#39;gpt-4o-mini&#39;. For Google defaults to &#39;gemini-2.5-flash&#39;. | [optional] 
**include_summary** | **bool** | Whether to generate cluster summaries | [optional] [default to True]
**include_keywords** | **bool** | Whether to extract keywords for clusters | [optional] [default to True]
**max_samples_per_cluster** | **int** | Maximum samples to send to LLM per cluster | [optional] [default to 10]
**custom_prompt** | **str** | Custom prompt template for labeling | [optional] 
**parameters** | **Dict[str, object]** | Provider-specific parameters forwarded to the LLM service. For OpenAI: temperature, max_tokens, top_p, json_output, etc. For Google: temperature, top_k, max_output_tokens, json_output, etc. | [optional] 

## Example

```python
from mixpeek.models.llm_labeling import LLMLabeling

# TODO update the JSON string below
json = "{}"
# create an instance of LLMLabeling from a JSON string
llm_labeling_instance = LLMLabeling.from_json(json)
# print the JSON string representation of the object
print(LLMLabeling.to_json())

# convert the object into a dict
llm_labeling_dict = llm_labeling_instance.to_dict()
# create an instance of LLMLabeling from a dict
llm_labeling_from_dict = LLMLabeling.from_dict(llm_labeling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


