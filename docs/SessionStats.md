# SessionStats

Session usage statistics.  Tracked in MongoDB session document, updated on each message. Use this to display usage metrics in your UI.  Attributes:     total_messages: Total messages sent in session     total_tokens: Cumulative tokens used (for cost tracking)     total_tool_calls: Total tool invocations     avg_latency_ms: Average message latency in milliseconds  Example:     ```python     # Display in UI     stats = session_response.stats     print(f\"Messages: {stats.total_messages}\")     print(f\"Tokens used: {stats.total_tokens}\")     print(f\"Tool calls: {stats.total_tool_calls}\")     print(f\"Avg latency: {stats.avg_latency_ms:.0f}ms\")     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_messages** | **int** | Total messages sent in session | [optional] [default to 0]
**total_tokens** | **int** | Cumulative tokens used (for cost tracking) | [optional] [default to 0]
**total_tool_calls** | **int** | Total tool invocations | [optional] [default to 0]
**avg_latency_ms** | **float** | Average message latency in milliseconds | [optional] [default to 0.0]

## Example

```python
from mixpeek.models.session_stats import SessionStats

# TODO update the JSON string below
json = "{}"
# create an instance of SessionStats from a JSON string
session_stats_instance = SessionStats.from_json(json)
# print the JSON string representation of the object
print(SessionStats.to_json())

# convert the object into a dict
session_stats_dict = session_stats_instance.to_dict()
# create an instance of SessionStats from a dict
session_stats_from_dict = SessionStats.from_dict(session_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


