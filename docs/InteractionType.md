# InteractionType

Types of user interactions with search results.  These interaction types are used to track user behavior and improve retrieval quality through Learning to Rank (LTR), collaborative filtering, and embedding fine-tuning.  Values:     VIEW: User viewed a search result     CLICK: User clicked on a search result     POSITIVE_FEEDBACK: User explicitly marked result as relevant/helpful     NEGATIVE_FEEDBACK: User explicitly marked result as not relevant     PURCHASE: User purchased the item (high-value conversion signal)     ADD_TO_CART: User added item to cart (mid-funnel signal)     WISHLIST: User saved item for later (engagement signal)     LONG_VIEW: User spent significant time viewing (dwell time)     SHARE: User shared the result (strong engagement signal)     BOOKMARK: User bookmarked the result     QUERY_REFINEMENT: User modified their search query     ZERO_RESULTS: Query yielded no results (helps identify gaps)     FILTER_TOGGLE: User modified filters (helps understand intent)     SKIP: User skipped over result to click something lower (negative signal)     RETURN_TO_RESULTS: User quickly returned to results (negative signal)  Usage in Retrieval Optimization:     - LTR (Learning to Rank): Train models to predict click-through rates     - Collaborative Filtering: Find similar users/items based on interactions     - Embedding Fine-tuning: Adjust embeddings based on what users actually click     - Query Understanding: Analyze refinements and zero-result queries     - Result Quality: Identify poorly-performing results via skip/return patterns

## Enum

* `VIEW` (value: `'view'`)

* `CLICK` (value: `'click'`)

* `POSITIVE_FEEDBACK` (value: `'positive_feedback'`)

* `NEGATIVE_FEEDBACK` (value: `'negative_feedback'`)

* `PURCHASE` (value: `'purchase'`)

* `ADD_TO_CART` (value: `'add_to_cart'`)

* `WISHLIST` (value: `'wishlist'`)

* `LONG_VIEW` (value: `'long_view'`)

* `SHARE` (value: `'share'`)

* `BOOKMARK` (value: `'bookmark'`)

* `QUERY_REFINEMENT` (value: `'query_refinement'`)

* `ZERO_RESULTS` (value: `'zero_results'`)

* `FILTER_TOGGLE` (value: `'filter_toggle'`)

* `SKIP` (value: `'skip'`)

* `RETURN_TO_RESULTS` (value: `'return_to_results'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


