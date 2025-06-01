# RetrieverBinding

How a retriever should be used in a taxonomy


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `retriever_id`                                                                       | *str*                                                                                | :heavy_check_mark:                                                                   | ID of the retriever to use                                                           |
| `inputs`                                                                             | Dict[str, *Any*]                                                                     | :heavy_minus_sign:                                                                   | Optional inputs to the retriever. If not provided, will use source collection schema |