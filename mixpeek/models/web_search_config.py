from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebSearchConfig")


@_attrs_define
class WebSearchConfig:
    """Configuration for web search enrichment using Exa AI-native search.

    **Stage Category**: APPLY (Document Enrichment - enriches existing documents)

    **Transformation**: N documents → N documents (each enriched with web search results)

    **Purpose**: Enriches each document in the pipeline by adding AI-native web search
    results from Exa's neural ranking system to the document's metadata. The query can
    be templated per-document using {{DOC.*}}, {{INPUT.*}}, etc., enabling dynamic
    searches based on document content. Results are automatically cached by query to
    minimize redundant API calls.

    **When to Use**:
        - Enrich documents with real-time web context
        - Add related articles/research to each document
        - Augment internal data with external web sources
        - Find competitive intelligence per product/company in documents
        - Add news/updates related to document entities
        - Research and discovery based on document content
        - Context augmentation for RAG pipelines

    **When NOT to Use**:
        - Searching within your own collections (use feature_search instead)
        - Need full web page content (use web_scrape stage for that)
        - Want to create NEW documents from web search (this enriches existing ones)
        - No existing documents to enrich (pipeline must have documents first)

    **Operational Behavior**:
        - ENRICHES existing documents (N → N operation, preserves all docs)
        - Each document gets web search results added to metadata.web_search
        - Query is templated per-document with {{DOC.*}} support
        - Smart caching: identical queries share results (only 1 API call)
        - Preserves all original document data (ID, collection, score, etc.)
        - Makes external HTTP request to Exa API (cached per unique query)
        - Fast operation: 100-500ms per unique query (not per document)

    **Common Pipeline Position**:
        - feature_search → web_search (enrich search results with web context)
        - feature_search → web_search → llm_filter (search, enrich, then filter)
        - feature_search → web_search → web_scrape (enrich with URLs, then scrape)

    **Cost & Performance**:
        - Moderate Cost: Exa API charges per unique query (caching reduces costs)
        - Fast: 100-500ms per unique query, cached queries are instant
        - Network dependent: requires external API call
        - Static queries: 1 API call for all documents (highly efficient)
        - Dynamic queries: 1 API call per unique rendered query

    **Output Schema**: Adds to each DocumentResult:
        - metadata.web_search.query: Rendered query used for this document
        - metadata.web_search.results: Array of web search results
        - metadata.web_search.results[].url: Web page URL
        - metadata.web_search.results[].title: Page title
        - metadata.web_search.results[].text: Text snippet (if include_text=True)
        - metadata.web_search.results[].published_date: Publication date
        - metadata.web_search.results[].author: Author name
        - metadata.web_search.results[].score: Exa relevance score
        - metadata.web_search.results[].position: Result position (0-indexed)
        - metadata.web_search.num_results: Count of results
        - metadata.web_search.autoprompt_used: Whether autoprompt was enabled

    Requirements:
        - query: REQUIRED, search query text (supports templates like {INPUT.query})
        - num_results: OPTIONAL, number of results (default 10, max 100)
        - use_autoprompt: OPTIONAL, use Exa's query enhancement (default True)
        - start_published_date: OPTIONAL, filter by publication date
        - category: OPTIONAL, filter by content type
        - include_text: OPTIONAL, include text snippets (default True)

    Use Cases:
        - RAG enhancement: Enrich documents with current web context before LLM
        - Product research: Add competitor info to each product document
        - News enrichment: Add latest news to company/entity documents
        - Academic research: Add related papers to each research document
        - Documentation augmentation: Add official docs/guides to each result
        - Competitive intelligence: Enrich results with competitor mentions
        - Fact verification: Add source citations from web to each claim

    Examples:
        Static query enrichment (all documents get same web results):
            ```json
            {
                "query": "latest AI developments 2024",
                "num_results": 10,
                "include_text": true
            }
            ```
            Result: 1 API call total, all documents enriched with same 10 web results

        Dynamic per-document enrichment (query varies by document):
            ```json
            {
                "query": "{{DOC.metadata.product_name}} reviews and comparisons",
                "num_results": 5,
                "include_text": true
            }
            ```
            Result: 1 API call per unique product name (automatically cached)

        Hybrid query (combines input + document fields):
            ```json
            {
                "query": "{{INPUT.topic}} {{DOC.metadata.category}}",
                "num_results": 3,
                "start_published_date": "2024-01-01"
            }
            ```
            Result: Caching optimizes for documents with same topic+category combo

        News enrichment with date filter:
            ```json
            {
                "query": "{{DOC.metadata.company_name}} latest news",
                "num_results": 5,
                "category": "news",
                "start_published_date": "2024-11-01"
            }
            ```
            Result: Recent news added to each company document's metadata

        Attributes:
            query (str | Unset): Search query text for Exa AI search. Supports template variables: {{INPUT.field}} for query
                inputs, {{DOC.field}} for document fields in enrichment context. Exa uses neural ranking for semantic search, so
                natural language queries work well. Examples: 'machine learning tutorials', 'latest AI developments',
                '{{INPUT.user_query}}', 'news about {{DOC.metadata.company_name}}' Default: '{{INPUT.query}}'.
            num_results (int | Unset): OPTIONAL. Number of search results to return. Must be between 1 and 100. Default is
                10. More results = higher API costs. Consider using lower values for faster responses and cost control. Default:
                10.
            use_autoprompt (bool | Unset): OPTIONAL. Enable Exa's autoprompt feature for query enhancement. When True, Exa
                optimizes the query for better search results. Default is True. Recommended for most use cases. Disable if you
                want exact query matching without enhancement. Default: True.
            start_published_date (None | str | Unset): OPTIONAL. Filter results to content published after this date.
                Format: YYYY-MM-DD (e.g., '2024-01-01'). When NOT specified, returns results from all dates. Useful for finding
                recent content, news, or time-sensitive information.
            category (None | str | Unset): OPTIONAL. Filter results by content category. When NOT specified, searches across
                all categories. Common categories: 'research paper', 'news', 'github', 'tweet', 'company', 'pdf', 'personal
                site', 'blog'. Case-insensitive. Use for focused domain search.
            include_text (bool | Unset): OPTIONAL. Include text snippets in search results. When True, each result includes
                a text preview (~200 words). Default is True. Disable to reduce API costs and response size. Text snippets are
                stored in metadata.text field of DocumentResult. Default: True.
    """

    query: str | Unset = "{{INPUT.query}}"
    num_results: int | Unset = 10
    use_autoprompt: bool | Unset = True
    start_published_date: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    include_text: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        num_results = self.num_results

        use_autoprompt = self.use_autoprompt

        start_published_date: None | str | Unset
        if isinstance(self.start_published_date, Unset):
            start_published_date = UNSET
        else:
            start_published_date = self.start_published_date

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        include_text = self.include_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if num_results is not UNSET:
            field_dict["num_results"] = num_results
        if use_autoprompt is not UNSET:
            field_dict["use_autoprompt"] = use_autoprompt
        if start_published_date is not UNSET:
            field_dict["start_published_date"] = start_published_date
        if category is not UNSET:
            field_dict["category"] = category
        if include_text is not UNSET:
            field_dict["include_text"] = include_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query", UNSET)

        num_results = d.pop("num_results", UNSET)

        use_autoprompt = d.pop("use_autoprompt", UNSET)

        def _parse_start_published_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_published_date = _parse_start_published_date(d.pop("start_published_date", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        include_text = d.pop("include_text", UNSET)

        web_search_config = cls(
            query=query,
            num_results=num_results,
            use_autoprompt=use_autoprompt,
            start_published_date=start_published_date,
            category=category,
            include_text=include_text,
        )

        web_search_config.additional_properties = d
        return web_search_config

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
