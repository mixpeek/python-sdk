# SentimentClassifierParams

Parameters for sentiment classifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractor_type** | **str** | Discriminator field for parameter type identification. | [optional] [default to 'sentiment_classifier']
**model_name** | **str** | HuggingFace model name for sentiment classification | [optional] [default to 'distilbert-base-uncased-finetuned-sst-2-english']
**max_length** | **int** | Maximum token length | [optional] [default to 512]
**batch_size** | **int** | Inference batch size | [optional] [default to 32]
**return_all_scores** | **bool** | Return scores for all classes, not just top | [optional] [default to True]
**embed** | **bool** | Generate E5 embeddings for semantic retrieval alongside classification. Uses the internal E5 embedding service for 1024-dimensional vectors. | [optional] [default to False]

## Example

```python
from mixpeek.models.sentiment_classifier_params import SentimentClassifierParams

# TODO update the JSON string below
json = "{}"
# create an instance of SentimentClassifierParams from a JSON string
sentiment_classifier_params_instance = SentimentClassifierParams.from_json(json)
# print the JSON string representation of the object
print(SentimentClassifierParams.to_json())

# convert the object into a dict
sentiment_classifier_params_dict = sentiment_classifier_params_instance.to_dict()
# create an instance of SentimentClassifierParams from a dict
sentiment_classifier_params_from_dict = SentimentClassifierParams.from_dict(sentiment_classifier_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


