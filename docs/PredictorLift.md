# PredictorLift

Lift calculation for a specific covariate value.  Lift measures how much a specific value increases/decreases conversion likelihood compared to the baseline. Lift > 1.0 means the value helps conversion.  Attributes:     field: Name of the covariate (e.g., \"Sender Domain\", \"Word Count Q3\")     value: Specific value or bin (e.g., \"gmail.com\", \"Q3\")     count: Number of sequences with this value     conversion_rate: Conversion rate for this value (0.0 to 1.0)     lift: Conversion rate / baseline rate (1.0 = no effect, >1.0 = positive, <1.0 = negative)  Example:     ```python     # Sender domain \"enterprise.com\" has 2.5x baseline conversion     PredictorLift(         field=\"Sender Domain\",         value=\"enterprise.com\",         count=150,         conversion_rate=0.75,  # 75% conversion         lift=2.5  # 2.5x the baseline rate     )     ```  Interpretation:     - lift = 1.5: This value increases conversion by 50%     - lift = 1.0: No effect on conversion     - lift = 0.5: This value decreases conversion by 50%

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Covariate field name | 
**value** | **str** | Specific value or bin label | 
**count** | **int** | Number of sequences with this value | 
**conversion_rate** | **float** | Conversion rate for this value | 
**lift** | **float** | Lift relative to baseline (&gt;1.0 &#x3D; positive, &lt;1.0 &#x3D; negative) | 

## Example

```python
from mixpeek.models.predictor_lift import PredictorLift

# TODO update the JSON string below
json = "{}"
# create an instance of PredictorLift from a JSON string
predictor_lift_instance = PredictorLift.from_json(json)
# print the JSON string representation of the object
print(PredictorLift.to_json())

# convert the object into a dict
predictor_lift_dict = predictor_lift_instance.to_dict()
# create an instance of PredictorLift from a dict
predictor_lift_from_dict = PredictorLift.from_dict(predictor_lift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


