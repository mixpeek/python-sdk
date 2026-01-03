# RangeBucket

Configuration for range-based bucketing.  Groups numeric values into ranges/buckets for histogram-style analysis.  Requirements:     - field: REQUIRED, numeric field to bucket     - boundaries: REQUIRED, list of boundary values defining buckets     - default_bucket: OPTIONAL, name for values outside boundaries  Examples:     - Video duration buckets: [0, 60, 300, 600] creates: 0-60s, 60-300s, 300-600s, 600+s     - View count buckets: [0, 100, 1000, 10000] creates: 0-100, 100-1K, 1K-10K, 10K+ views

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Numeric field to create buckets for. REQUIRED, must be a numeric field. Supports dot notation for nested fields. Values will be grouped into ranges defined by boundaries. | 
**boundaries** | [**List[RangeBucketBoundariesInner]**](RangeBucketBoundariesInner.md) | List of boundary values defining bucket ranges. REQUIRED, must be sorted in ascending order. Creates N+1 buckets for N boundaries: [0, 10, 20] creates: &lt;0, 0-10, 10-20, &gt;20. Values on boundaries go into the lower bucket. | 
**default_bucket** | **str** | Name for values outside defined boundaries. OPTIONAL, defaults to &#39;other&#39;. Used for values below min or above max boundary. | [optional] 

## Example

```python
from mixpeek.models.range_bucket import RangeBucket

# TODO update the JSON string below
json = "{}"
# create an instance of RangeBucket from a JSON string
range_bucket_instance = RangeBucket.from_json(json)
# print the JSON string representation of the object
print(RangeBucket.to_json())

# convert the object into a dict
range_bucket_dict = range_bucket_instance.to_dict()
# create an instance of RangeBucket from a dict
range_bucket_from_dict = RangeBucket.from_dict(range_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


