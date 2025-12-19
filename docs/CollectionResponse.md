# CollectionResponse

Response model for collection endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | Unique collection identifier | [optional] 
**collection_name** | **str** | Collection name | 
**description** | **str** | Collection description | [optional] 
**var_schema** | **Dict[str, object]** | Collection schema | [optional] 
**input_schema** | [**BucketSchemaOutput**](BucketSchemaOutput.md) | Input schema for the collection | [optional] 
**output_schema** | [**BucketSchemaOutput**](BucketSchemaOutput.md) | Output schema after feature extraction | [optional] 
**feature_extractors** | [**List[FeatureExtractorConfigOutput]**](FeatureExtractorConfigOutput.md) | Feature extractors applied to this collection | [optional] 
**source** | [**SourceConfig**](SourceConfig.md) | Primary source configuration for this collection | 
**source_lineage** | [**List[SingleLineageEntry]**](SingleLineageEntry.md) | Lineage chain showing the processing history | [optional] 
**vector_indexes** | **List[object]** | Vector indexes for this collection | [optional] 
**payload_indexes** | **List[object]** | Payload indexes for this collection | [optional] 
**enabled** | **bool** | Whether the collection is enabled | [optional] [default to True]
**metadata** | **Dict[str, object]** | Additional metadata for the collection | [optional] 
**taxonomy_applications** | [**List[TaxonomyApplicationConfig]**](TaxonomyApplicationConfig.md) | List of taxonomies applied to this collection | [optional] 
**document_count** | **int** | Number of documents in the collection | [optional] 

## Example

```python
from mixpeek.models.collection_response import CollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionResponse from a JSON string
collection_response_instance = CollectionResponse.from_json(json)
# print the JSON string representation of the object
print(CollectionResponse.to_json())

# convert the object into a dict
collection_response_dict = collection_response_instance.to_dict()
# create an instance of CollectionResponse from a dict
collection_response_from_dict = CollectionResponse.from_dict(collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


