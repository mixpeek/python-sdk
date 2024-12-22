# AssetsModelSearchQuery


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `key`                                                                   | List[*str*]                                                             | :heavy_check_mark:                                                      | Fields to search in. Can be a list of field names or '*' for all fields | [<br/>"title",<br/>"description"<br/>]                                  |
| `value`                                                                 | *str*                                                                   | :heavy_check_mark:                                                      | The search term to look for in the specified fields                     | search term                                                             |