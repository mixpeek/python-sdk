# TextSplitStrategy

Strategy for splitting text into chunks.  Defines how long text documents are decomposed into smaller chunks for processing. Different strategies are optimal for different types of content and use cases.  Values:     CHARACTERS: Split by fixed character count, fastest but may break mid-word     WORDS: Split by word boundaries, preserves words but may break mid-sentence     SENTENCES: Split by sentence boundaries, preserves semantic units     PARAGRAPHS: Split by paragraph boundaries (double newlines), best for structured documents     PAGES: Split by page breaks (form feed character), best for paginated documents     NONE: No splitting, process entire text as one document (default)  Examples:     - Use CHARACTERS for uniform chunk sizes regardless of content structure     - Use WORDS for better readability than character-level splitting     - Use SENTENCES for semantic coherence in each chunk     - Use PARAGRAPHS for long-form articles, blog posts, documentation     - Use PAGES for PDFs or documents with explicit page structure     - Use NONE for short texts that fit within context window

## Enum

* `CHARACTERS` (value: `'characters'`)

* `WORDS` (value: `'words'`)

* `SENTENCES` (value: `'sentences'`)

* `PARAGRAPHS` (value: `'paragraphs'`)

* `PAGES` (value: `'pages'`)

* `NONE` (value: `'none'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


