# SingleLineageEntry

Single entry in the lineage chain of a collection.  Each lineage entry represents one processing stage with one feature extractor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_config** | [**SourceConfigOutput**](SourceConfigOutput.md) | Configuration of the source for this lineage entry | 
**feature_extractor** | [**SharedCollectionFeaturesExtractorsModelsFeatureExtractorConfigOutput**](SharedCollectionFeaturesExtractorsModelsFeatureExtractorConfigOutput.md) | Single feature extractor applied at this stage | 
**output_schema** | [**BucketSchemaOutput**](BucketSchemaOutput.md) | Output schema produced by this processing stage | 

## Example

```python
from mixpeek.models.single_lineage_entry import SingleLineageEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SingleLineageEntry from a JSON string
single_lineage_entry_instance = SingleLineageEntry.from_json(json)
# print the JSON string representation of the object
print(SingleLineageEntry.to_json())

# convert the object into a dict
single_lineage_entry_dict = single_lineage_entry_instance.to_dict()
# create an instance of SingleLineageEntry from a dict
single_lineage_entry_from_dict = SingleLineageEntry.from_dict(single_lineage_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


