# FeatureSearchGroupBy

Database-level grouping for feature search (uses Qdrant query_points_groups).  Enables efficient grouping at the database level rather than in-memory post-processing. Perfect for decompose/recompose patterns where you search chunks but want to return parent documents.  This mirrors the output_mode behavior of the group_by REDUCE stage for API consistency, but executes at the database level for better performance on large result sets.  Stage Category: FILTER (grouping is part of the Qdrant query)  Performance: Database-level grouping is significantly faster than fetching all results and grouping in memory. Qdrant handles the grouping natively.  Use Cases:     - Decompose/recompose: Search 500 text chunks, return top 25 unique documents     - Deduplication: One best result per product_id     - Scene → Video grouping: Search video frames, return parent videos  Examples:     Deduplication (one result per video):         ```json         {\"field\": \"video_id\", \"max_per_group\": 1, \"output_mode\": \"first\"}         ```      Top 3 chunks per document:         ```json         {\"field\": \"source_object_id\", \"max_per_group\": 3, \"output_mode\": \"all\"}         ```      Flatten grouped results:         ```json         {\"field\": \"category\", \"max_per_group\": 5, \"output_mode\": \"flatten\"}         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | REQUIRED. Field path to group documents by using dot notation. Documents with the same field value are grouped together. Common fields: &#39;source_object_id&#39; (parent object from decomposition), &#39;video_id&#39; (media grouping), &#39;product_id&#39; (e-commerce), &#39;metadata.category&#39; (nested categorical field). The field must exist in the document payload. | 
**max_per_group** | **int** | OPTIONAL. Maximum number of documents to keep per group (Qdrant&#39;s group_size). Documents are sorted by score (highest first) before limiting. Default: 1 (deduplication - keeps only highest scoring doc per group). Use 1 for deduplication, 3-5 for preview results, 10+ for comprehensive results. Note: This is a best-effort parameter in Qdrant. | [optional] [default to 1]
**limit** | **int** | OPTIONAL. Maximum number of groups to return. This overrides final_top_k when grouping is enabled. Default: 25 groups. | [optional] [default to 25]
**output_mode** | **str** | OPTIONAL. Controls what documents are returned per group. Mirrors the group_by REDUCE stage for API consistency. &#39;first&#39;: Return only the top document per group (deduplication, fastest).          Use for: unique results per group (e.g., one video per brand). &#39;all&#39;: Return all documents grouped by field (default, shows full context).        Use for: showing chunks within each parent object. &#39;flatten&#39;: Return all documents as flat list (loses group structure).            Use for: need all docs but don&#39;t care about grouping metadata. Default: &#39;all&#39;. | [optional] [default to 'all']

## Example

```python
from mixpeek.models.feature_search_group_by import FeatureSearchGroupBy

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureSearchGroupBy from a JSON string
feature_search_group_by_instance = FeatureSearchGroupBy.from_json(json)
# print the JSON string representation of the object
print(FeatureSearchGroupBy.to_json())

# convert the object into a dict
feature_search_group_by_dict = feature_search_group_by_instance.to_dict()
# create an instance of FeatureSearchGroupBy from a dict
feature_search_group_by_from_dict = FeatureSearchGroupBy.from_dict(feature_search_group_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


