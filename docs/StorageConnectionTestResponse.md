# StorageConnectionTestResponse

Response payload for connection test endpoint.  Returns the result of testing connection credentials against the external provider. Used to validate credentials before saving or to diagnose issues.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the connection test succeeded. True: Credentials are valid and connection is accessible. False: Authentication failed, network error, or permissions denied. | 
**message** | **str** | Human-readable message describing the test result. Success: &#39;Connection test succeeded&#39; or similar. Failure: Error message explaining what went wrong. | 
**details** | **Dict[str, object]** | OPTIONAL. Additional diagnostic information about the test result. May include error details, provider-specific information, or success metadata. Format varies by provider. | [optional] 

## Example

```python
from mixpeek.models.storage_connection_test_response import StorageConnectionTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StorageConnectionTestResponse from a JSON string
storage_connection_test_response_instance = StorageConnectionTestResponse.from_json(json)
# print the JSON string representation of the object
print(StorageConnectionTestResponse.to_json())

# convert the object into a dict
storage_connection_test_response_dict = storage_connection_test_response_instance.to_dict()
# create an instance of StorageConnectionTestResponse from a dict
storage_connection_test_response_from_dict = StorageConnectionTestResponse.from_dict(storage_connection_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


