# PublicRetrieverTemplateResponse

Response containing public retriever configuration as a reusable template.  This returns the retriever's configuration in a format that can be directly used in a CreateRetrieverRequest. Users can copy this config, modify it for their needs (e.g., change collection_identifiers), and create their own retriever.  Use Case:     1. Browse public retrievers to find patterns you like     2. GET /public/retrievers/{public_name}/template to get the config     3. Modify collection_identifiers and other fields as needed     4. POST /retrievers to create your own retriever with this config     5. Optionally POST /retrievers/{id}/publish to publish it similarly

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_name** | **str** | Original retriever name (you&#39;ll change this when creating your own). Provided as reference. | 
**description** | **str** | Original retriever description (you can use or modify this). Provides context about what this retriever does. | [optional] 
**collection_identifiers** | **List[str]** | IMPORTANT: These are the original collections. You MUST replace these with your own collection identifiers when creating a retriever from this template. | 
**stages** | **List[object]** | Pipeline stages configuration. You can use as-is or modify for your needs. This is the core retrieval logic. | 
**input_schema** | [**Dict[str, RetrieverInputSchemaFieldOutput]**](RetrieverInputSchemaFieldOutput.md) | Input schema defining expected inputs. If you change the input field names, make sure to update references in stages (e.g., {{inputs.query}}). | 
**budget_limits** | **object** | Budget limits for execution. You can adjust these based on your needs. | 
**tags** | **List[str]** | Original tags (optional, for reference) | [optional] 
**display_config** | [**DisplayConfigOutput**](DisplayConfigOutput.md) | OPTIONAL: Display configuration used for the public interface. Include this if you plan to publish your retriever and want to use a similar UI design. Otherwise, you can omit it. | [optional] 
**source_public_name** | **str** | Public name of the source retriever (for reference) | 
**source_public_url** | **str** | Public URL of the source retriever (to view it in action) | 
**feature_extractors** | **List[object]** | Feature extractors from all collections used by this retriever. Each extractor includes: feature_extractor_name, version, params, input_mappings, collection_id, and collection_name for reference. Shows how each collection processes data into searchable features. | [optional] 

## Example

```python
from mixpeek.models.public_retriever_template_response import PublicRetrieverTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicRetrieverTemplateResponse from a JSON string
public_retriever_template_response_instance = PublicRetrieverTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(PublicRetrieverTemplateResponse.to_json())

# convert the object into a dict
public_retriever_template_response_dict = public_retriever_template_response_instance.to_dict()
# create an instance of PublicRetrieverTemplateResponse from a dict
public_retriever_template_response_from_dict = PublicRetrieverTemplateResponse.from_dict(public_retriever_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


