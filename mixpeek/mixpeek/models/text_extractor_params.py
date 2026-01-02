from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_split_strategy import TextSplitStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_extractor_params_response_shape_type_1 import TextExtractorParamsResponseShapeType1


T = TypeVar("T", bound="TextExtractorParams")


@_attrs_define
class TextExtractorParams:
    """Parameters for the text extractor.

    The text extractor generates dense vector embeddings optimized for semantic similarity search.
    It uses the E5-Large multilingual model to convert text into 1024-dimensional vectors that
    capture semantic meaning, enabling accurate retrieval of conceptually related documents.

    **Text Chunking & Decomposition**:
        The extractor supports splitting long texts into multiple documents using various strategies.
        This is essential for RAG applications where you need granular retrieval of specific passages.

        - split_by: Strategy for splitting text (characters, words, sentences, paragraphs, pages, none)
        - chunk_size: Target size for each chunk (interpretation depends on split_by strategy)
        - chunk_overlap: Number of units to overlap between chunks (helps preserve context)

        **Strategy Guide**:
        - CHARACTERS: Fastest, uniform sizes, may break words. Good for quick testing.
        - WORDS: Better readability, may break sentences. Good for general text.
        - SENTENCES: Preserves semantic units. Best for Q&A and precise retrieval.
        - PARAGRAPHS: Natural document structure. Best for articles and documentation.
        - PAGES: Explicit page boundaries. Best for PDFs and paginated content.
        - NONE: No splitting. Use for short texts (<400 words).

    **LLM Structured Extraction (NEW)**:
        The extractor now supports LLM-powered structured extraction using `response_shape`.
        Instead of just generating embeddings, you can extract custom structured data from text.

        - response_shape: Natural language prompt OR explicit JSON schema
        - llm_provider: LLM provider to use (openai, google, anthropic)
        - llm_model: Specific model for extraction

        **When to Use**:
        - Extract entities, relationships, sentiment from text
        - Generate structured summaries with custom fields
        - Classify text into custom taxonomies
        - Extract domain-specific metadata

    **When to Use**:
        - General semantic search (documents, articles, knowledge bases, FAQs)
        - RAG (Retrieval Augmented Generation) applications requiring fast context retrieval
        - Q&A systems matching questions to answers semantically
        - Content recommendation based on similarity
        - Chatbots finding relevant information from documentation
        - Multi-language search (supports 100+ languages)
        - Real-time search requiring low latency (<10ms per query)
        - Structured extraction from text using LLMs (NEW)

    **When NOT to Use**:
        - Very short texts (1-5 words) where keyword matching might be sufficient
        - When exact keyword/phrase matching is more important than semantic similarity

    **Model Details**:
        - Embedding Model: E5-Large (intfloat/multilingual-e5-large-instruct)
        - Dimensions: 1024
        - Context Length: 512 tokens (~400 words)
        - Languages: 100+ (trained on multilingual data)
        - Distance Metric: Cosine similarity
        - Normalization: L2 normalized vectors

    **Performance Characteristics**:
        - Embedding Generation: 5ms per document (batched: 2ms/doc)
        - Index Build: ~1 hour per 10M documents
        - Query Time: 5-10ms for top-100 results
        - Memory: ~4GB per 1M documents
        - Scales linearly with document count

    **Use Case Examples**:
        1. **E-commerce Product Search**: Search 1M products by description, find semantically similar items
        2. **Customer Support**: Match user questions to 10K FAQ articles with 85%+ accuracy
        3. **Document RAG**: Retrieve relevant context chunks from 100K documents for LLM prompts
        4. **News Article Discovery**: Find related articles across 1M news items
        5. **Research Paper Search**: Semantic search over academic papers and abstracts
        6. **Structured Extraction**: Extract entities, sentiment, topics from documents using LLMs (NEW)

    **Limitations**:
        - Cannot match exact phrases or technical terms reliably
        - May miss documents that use different terminology for same concept
        - Struggles with very domain-specific jargon or acronyms
        - 512 token limit means long documents must be chunked
        - Less effective for keyword-heavy queries (e.g., "iPhone 15 Pro Max 256GB")
        - LLM extraction adds latency (only use when needed)

    Requirements:
        - text field: REQUIRED (string or text type)
        - All chunking parameters are OPTIONAL
        - LLM parameters are OPTIONAL (only for structured extraction)

        Attributes:
            extractor_type (Literal['text_extractor'] | Unset): Discriminator field for parameter type identification. Must
                be 'text_extractor'. Default: 'text_extractor'.
            split_by (TextSplitStrategy | Unset): Strategy for splitting text into chunks.

                Defines how long text documents are decomposed into smaller chunks for processing.
                Different strategies are optimal for different types of content and use cases.

                Values:
                    CHARACTERS: Split by fixed character count, fastest but may break mid-word
                    WORDS: Split by word boundaries, preserves words but may break mid-sentence
                    SENTENCES: Split by sentence boundaries, preserves semantic units
                    PARAGRAPHS: Split by paragraph boundaries (double newlines), best for structured documents
                    PAGES: Split by page breaks (form feed character), best for paginated documents
                    NONE: No splitting, process entire text as one document (default)

                Examples:
                    - Use CHARACTERS for uniform chunk sizes regardless of content structure
                    - Use WORDS for better readability than character-level splitting
                    - Use SENTENCES for semantic coherence in each chunk
                    - Use PARAGRAPHS for long-form articles, blog posts, documentation
                    - Use PAGES for PDFs or documents with explicit page structure
                    - Use NONE for short texts that fit within context window
            chunk_size (int | Unset): OPTIONAL. Target size for each chunk. Interpretation depends on split_by strategy: -
                characters: Number of characters per chunk (e.g., 1000 chars). - words: Number of words per chunk (e.g., 200
                words). - sentences: Number of sentences per chunk (e.g., 5 sentences). - paragraphs: Number of paragraphs per
                chunk (e.g., 2 paragraphs). - pages: Number of pages per chunk (e.g., 1 page). - none: Ignored (entire text
                processed as one document). Default: 1000. Recommended ranges: characters (500-2000), words (100-400), sentences
                (3-10). Default: 1000.
            chunk_overlap (int | Unset): OPTIONAL. Number of units to overlap between consecutive chunks. Helps preserve
                context across chunk boundaries. Units match split_by strategy (characters, words, sentences, etc.). Example:
                With chunk_size=1000 and chunk_overlap=100, chunks will be: [0-1000], [900-1900], [1800-2800], etc. Default: 0
                (no overlap). Recommended: 10-20% of chunk_size (e.g., 100-200 for chunk_size=1000). Higher overlap improves
                context but increases storage and processing time. Default: 0.
            response_shape (None | str | TextExtractorParamsResponseShapeType1 | Unset): OPTIONAL. Define custom structured
                output using LLM extraction. NOT REQUIRED - by default, only embeddings are generated. When provided, LLM will
                extract structured data matching this schema.

                Two modes supported:
                1. Natural language prompt (string): Describe desired output in plain English
                   - Service automatically infers JSON schema from your description
                   - Example: 'Extract key entities, sentiment (positive/negative/neutral), and main topics'
                   - Auto-generates schema with appropriate types (string, array, etc.)

                2. Explicit JSON schema (dict): Provide complete JSON schema for output structure
                   - Full control over output structure, types, and constraints
                   - Example: {'type': 'object', 'properties': {'entities': {'type': 'array', ...}}}


                Use when:
                  - Need to extract entities, relationships, sentiment from text
                  - Want structured summaries with custom fields
                  - Require classification into custom taxonomies
                  - Have domain-specific extraction requirements


                Output fields are automatically added to collection schema and stored in document metadata.
                Note: Adds LLM latency - only use when structured extraction is needed.
            llm_provider (None | str | Unset): OPTIONAL. LLM provider to use for structured extraction. Only required if
                response_shape is provided. Supported providers: 'openai', 'google', 'anthropic'. Default: 'openai' if not
                specified.
            llm_model (None | str | Unset): OPTIONAL. Specific LLM model for structured extraction. Only required if
                response_shape is provided. Examples:
                - OpenAI: 'gpt-4o-mini-2024-07-18' (efficient), 'gpt-4o-2024-08-06' (best quality)
                - Google: 'gemini-2.0-flash' (fastest, recommended)
                - Anthropic: 'claude-3-5-haiku-20241022' (fast), 'claude-3-5-sonnet-20241022' (best reasoning)
                Default: Uses provider's recommended model if not specified.
    """

    extractor_type: Literal["text_extractor"] | Unset = "text_extractor"
    split_by: TextSplitStrategy | Unset = UNSET
    chunk_size: int | Unset = 1000
    chunk_overlap: int | Unset = 0
    response_shape: None | str | TextExtractorParamsResponseShapeType1 | Unset = UNSET
    llm_provider: None | str | Unset = UNSET
    llm_model: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_extractor_params_response_shape_type_1 import TextExtractorParamsResponseShapeType1

        extractor_type = self.extractor_type

        split_by: str | Unset = UNSET
        if not isinstance(self.split_by, Unset):
            split_by = self.split_by.value

        chunk_size = self.chunk_size

        chunk_overlap = self.chunk_overlap

        response_shape: dict[str, Any] | None | str | Unset
        if isinstance(self.response_shape, Unset):
            response_shape = UNSET
        elif isinstance(self.response_shape, TextExtractorParamsResponseShapeType1):
            response_shape = self.response_shape.to_dict()
        else:
            response_shape = self.response_shape

        llm_provider: None | str | Unset
        if isinstance(self.llm_provider, Unset):
            llm_provider = UNSET
        else:
            llm_provider = self.llm_provider

        llm_model: None | str | Unset
        if isinstance(self.llm_model, Unset):
            llm_model = UNSET
        else:
            llm_model = self.llm_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extractor_type is not UNSET:
            field_dict["extractor_type"] = extractor_type
        if split_by is not UNSET:
            field_dict["split_by"] = split_by
        if chunk_size is not UNSET:
            field_dict["chunk_size"] = chunk_size
        if chunk_overlap is not UNSET:
            field_dict["chunk_overlap"] = chunk_overlap
        if response_shape is not UNSET:
            field_dict["response_shape"] = response_shape
        if llm_provider is not UNSET:
            field_dict["llm_provider"] = llm_provider
        if llm_model is not UNSET:
            field_dict["llm_model"] = llm_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_extractor_params_response_shape_type_1 import TextExtractorParamsResponseShapeType1

        d = dict(src_dict)
        extractor_type = cast(Literal["text_extractor"] | Unset, d.pop("extractor_type", UNSET))
        if extractor_type != "text_extractor" and not isinstance(extractor_type, Unset):
            raise ValueError(f"extractor_type must match const 'text_extractor', got '{extractor_type}'")

        _split_by = d.pop("split_by", UNSET)
        split_by: TextSplitStrategy | Unset
        if isinstance(_split_by, Unset):
            split_by = UNSET
        else:
            split_by = TextSplitStrategy(_split_by)

        chunk_size = d.pop("chunk_size", UNSET)

        chunk_overlap = d.pop("chunk_overlap", UNSET)

        def _parse_response_shape(data: object) -> None | str | TextExtractorParamsResponseShapeType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_shape_type_1 = TextExtractorParamsResponseShapeType1.from_dict(data)

                return response_shape_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | TextExtractorParamsResponseShapeType1 | Unset, data)

        response_shape = _parse_response_shape(d.pop("response_shape", UNSET))

        def _parse_llm_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        llm_provider = _parse_llm_provider(d.pop("llm_provider", UNSET))

        def _parse_llm_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        llm_model = _parse_llm_model(d.pop("llm_model", UNSET))

        text_extractor_params = cls(
            extractor_type=extractor_type,
            split_by=split_by,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            response_shape=response_shape,
            llm_provider=llm_provider,
            llm_model=llm_model,
        )

        text_extractor_params.additional_properties = d
        return text_extractor_params

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
