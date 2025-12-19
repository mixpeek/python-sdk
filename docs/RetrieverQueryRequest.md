# RetrieverQueryRequest

Query parameters for executing a retriever pipeline.  This model defines all the parameters that can be provided when running a search using a predefined retriever pipeline. It allows for customizing the query inputs, filtering, sorting, pagination, and result formatting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_id** | **str** | Identifier of the retriever to execute. If omitted, the execution context must provide it. | [optional] 
**inputs** | **Dict[str, object]** | Input values for the retriever query. These map to the required inputs defined in the retriever&#39;s first stage. | 
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Logical operations for filtering results. Can include AND, OR, NOT conditions with field comparisons. | [optional] 
**sorts** | [**List[SortOption]**](SortOption.md) | Controls the ordering of results. Can sort by score (default) or any other document field. This sorts the results from the last stage. | [optional] 
**limit** | **int** | Maximum number of results to return. Overrides the default pagination limit in the retriever definition. | [optional] [default to 10]
**offset** | **int** | Number of results to skip. Use with limit for pagination. For large offsets, consider using session_id for cursor-based pagination. | [optional] [default to 0]
**select** | **List[str]** | Specific fields to include in the response. If not specified, returns all fields. | [optional] 
**session_id** | **str** | Session identifier for interaction tracking. | [optional] 
**return_urls** | **bool** | When true, generates pre-signed URLs for any media assets in the results. May increase response time slightly. | [optional] [default to False]
**group_by** | [**GroupByOption**](GroupByOption.md) | Options for grouping results by a specific field. | [optional] 

## Example

```python
from mixpeek.models.retriever_query_request import RetrieverQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverQueryRequest from a JSON string
retriever_query_request_instance = RetrieverQueryRequest.from_json(json)
# print the JSON string representation of the object
print(RetrieverQueryRequest.to_json())

# convert the object into a dict
retriever_query_request_dict = retriever_query_request_instance.to_dict()
# create an instance of RetrieverQueryRequest from a dict
retriever_query_request_from_dict = RetrieverQueryRequest.from_dict(retriever_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


