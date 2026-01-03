# OrganizationPublishStatsResponse

Response for organization publish quota stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_count** | **int** | Number of currently published retrievers | 
**max_allowed** | **int** | Maximum number of allowed published retrievers | 
**remaining** | **int** | Number of remaining publish slots | 
**at_limit** | **bool** | Whether the organization has reached the publish limit | 

## Example

```python
from mixpeek.models.organization_publish_stats_response import OrganizationPublishStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationPublishStatsResponse from a JSON string
organization_publish_stats_response_instance = OrganizationPublishStatsResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationPublishStatsResponse.to_json())

# convert the object into a dict
organization_publish_stats_response_dict = organization_publish_stats_response_instance.to_dict()
# create an instance of OrganizationPublishStatsResponse from a dict
organization_publish_stats_response_from_dict = OrganizationPublishStatsResponse.from_dict(organization_publish_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


