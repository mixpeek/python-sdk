# InstantiateTemplateRequest

Request to create a new namespace from a template.  Instantiation clones all data from the template's source namespace including: - Namespace configuration (feature extractors, indexes) - Qdrant vectors and payloads (pre-computed embeddings) - MongoDB metadata (collections, documents)  The process is fast (<5 seconds) because data is cloned, not reprocessed.  Use Cases:     - First-time user onboarding with working examples     - Creating demo environments for sales/trials     - Spinning up test environments with known data     - Providing industry-specific starting points  Requirements:     - namespace_name: REQUIRED, must be unique within organization     - description: OPTIONAL, defaults to template description if not provided  Validation:     - Checks namespace name uniqueness before creation     - Validates template exists and is active     - Ensures source namespace is accessible

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_name** | **str** | Name for the new namespace. REQUIRED. Must be unique within your organization. Used as identifier and display name. Format: 3-50 characters, alphanumeric with underscores/hyphens, lowercase recommended. Cannot match existing namespace names. | 
**description** | **str** | Optional description for the namespace. NOT REQUIRED. If not provided, uses the template&#39;s description. Useful for adding context about your specific use case. Format: 0-500 characters, plain text. | [optional] 

## Example

```python
from mixpeek.models.instantiate_template_request import InstantiateTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstantiateTemplateRequest from a JSON string
instantiate_template_request_instance = InstantiateTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(InstantiateTemplateRequest.to_json())

# convert the object into a dict
instantiate_template_request_dict = instantiate_template_request_instance.to_dict()
# create an instance of InstantiateTemplateRequest from a dict
instantiate_template_request_from_dict = InstantiateTemplateRequest.from_dict(instantiate_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


