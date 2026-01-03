# DurationStats

Statistical distribution of durations for successful step transitions.  Provides comprehensive percentile analysis to understand timing patterns.  Attributes:     mean: Average duration (seconds)     median: Middle value (50th percentile)     p50: 50th percentile (same as median, included for consistency)     p90: 90th percentile (90% complete faster)     p95: 95th percentile (95% complete faster)     std_dev: Standard deviation (measure of spread)     min: Fastest observed duration     max: Slowest observed duration  Example:     ```python     DurationStats(         mean=432000.0,     # 5 days average         median=345600.0,   # 4 days median         p50=345600.0,         p90=691200.0,      # 8 days (90th percentile)         p95=864000.0,      # 10 days (95th percentile)         std_dev=172800.0,  # 2 days std dev         min=86400.0,       # 1 day minimum         max=1209600.0      # 14 days maximum     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mean** | **float** | Average duration in seconds | 
**median** | **float** | Median duration in seconds | 
**p50** | **float** | 50th percentile (same as median) | 
**p90** | **float** | 90th percentile duration in seconds | 
**p95** | **float** | 95th percentile duration in seconds | 
**std_dev** | **float** | Standard deviation in seconds | 
**min** | **float** | Minimum duration observed in seconds | 
**max** | **float** | Maximum duration observed in seconds | 

## Example

```python
from mixpeek.models.duration_stats import DurationStats

# TODO update the JSON string below
json = "{}"
# create an instance of DurationStats from a JSON string
duration_stats_instance = DurationStats.from_json(json)
# print the JSON string representation of the object
print(DurationStats.to_json())

# convert the object into a dict
duration_stats_dict = duration_stats_instance.to_dict()
# create an instance of DurationStats from a dict
duration_stats_from_dict = DurationStats.from_dict(duration_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


