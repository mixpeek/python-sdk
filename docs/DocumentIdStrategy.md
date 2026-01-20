# DocumentIdStrategy

Strategy for generating deterministic document IDs.  Values:     URL: hash(page_url + chunk_index) - stable across re-crawls     POSITION: hash(seed_url + page_index + chunk_index) - order-based     CONTENT: hash(content) - deduplicates identical content

## Enum

* `URL` (value: `'url'`)

* `POSITION` (value: `'position'`)

* `CONTENT` (value: `'content'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


