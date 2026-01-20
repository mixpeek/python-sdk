# WebScraperExtractorParams

Parameters for the web scraper extractor.  The web scraper extractor crawls websites and extracts content with three types of embeddings for comprehensive multimodal search:  **Embedding Types:** - Text (E5-Large): 1024D embeddings for page content - Code (Jina Code): 768D embeddings for code blocks - Images (SigLIP): 768D embeddings for figures/screenshots  **Crawl Modes:** - DETERMINISTIC: BFS following all links (default, predictable) - SEMANTIC: LLM-guided, prioritizes pages matching crawl_goal  **Rendering Strategies:** - STATIC: Fast HTTP fetch (default, works for most sites) - JAVASCRIPT: Playwright browser for SPAs (React/Vue/Angular) - AUTO: Tries static, falls back to JS if content too short  **Use Cases:** - Documentation freshness: Crawl docs, compare against course content - Job board ingestion: Extract job listings with structured data - Knowledge base building: Convert websites to searchable collections - Code example indexing: Find API usage patterns across docs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractor_type** | **str** | Discriminator field for parameter type identification. | [optional] [default to 'web_scraper']
**max_depth** | **int** | Maximum link depth to crawl. 0&#x3D;seed page only, 1&#x3D;seed+direct links, etc. Default: 2. Increase for comprehensive crawls, decrease for targeted extraction. | [optional] [default to 2]
**max_pages** | **int** | Maximum pages to crawl. Default: 50. Set higher (1000+) for large documentation sites. Max: 1,000,000. | [optional] [default to 50]
**crawl_timeout** | **int** | Maximum total time for crawling in seconds. Default: 300 (5 minutes). Increase for large sites with many pages. Max: 3600 (1 hour). | [optional] [default to 300]
**crawl_mode** | [**CrawlMode**](CrawlMode.md) | Crawl strategy. DETERMINISTIC: BFS all links (predictable). SEMANTIC: LLM-guided, prioritizes relevant pages (requires crawl_goal). | [optional] 
**crawl_goal** | **str** | Goal for semantic crawling. Only used when crawl_mode&#x3D;SEMANTIC. Example: &#39;Find all S3 API documentation and examples&#39; | [optional] 
**render_strategy** | [**RenderStrategy**](RenderStrategy.md) | How to render pages. AUTO (default): tries static, falls back to JS. STATIC: fast HTTP fetch. JAVASCRIPT: Playwright browser for SPAs. | [optional] 
**include_patterns** | **List[str]** | Regex patterns for URLs to include. Example: [&#39;/docs/&#39;, &#39;/api/&#39;] | [optional] 
**exclude_patterns** | **List[str]** | Regex patterns for URLs to exclude. Example: [&#39;/blog/&#39;, &#39;\\.pdf$&#39;] | [optional] 
**chunk_strategy** | [**ChunkStrategy**](ChunkStrategy.md) | How to split page content. NONE: one chunk per page. SENTENCES/PARAGRAPHS: semantic boundaries. WORDS/CHARACTERS: fixed size chunks. | [optional] 
**chunk_size** | **int** | Target size for each chunk (in units of chunk_strategy). | [optional] [default to 500]
**chunk_overlap** | **int** | Overlap between chunks to preserve context. | [optional] [default to 50]
**document_id_strategy** | [**DocumentIdStrategy**](DocumentIdStrategy.md) | How to generate document IDs. URL (default): stable across re-crawls. POSITION: order-based. CONTENT: deduplicates identical content. | [optional] 
**generate_text_embeddings** | **bool** | Generate E5 embeddings for text content. | [optional] [default to True]
**generate_code_embeddings** | **bool** | Generate Jina code embeddings for code blocks. | [optional] [default to True]
**generate_image_embeddings** | **bool** | Generate SigLIP embeddings for images/figures. | [optional] [default to True]
**response_shape** | [**ResponseShape3**](ResponseShape3.md) |  | [optional] 
**llm_provider** | **str** | LLM provider for structured extraction: openai, google, anthropic | [optional] 
**llm_model** | **str** | LLM model for structured extraction. | [optional] 
**llm_api_key** | **str** | API key for LLM operations (BYOK - Bring Your Own Key). Supports: - Direct key: &#39;sk-proj-abc123...&#39; - Secret reference: &#39;{{SECRET.openai_api_key}}&#39;  When using secret reference, the key is loaded from your organization&#39;s secrets vault at runtime. Store secrets via POST /v1/organizations/secrets.  If not provided, uses Mixpeek&#39;s default API keys. | [optional] 
**max_retries** | **int** | Maximum retry attempts for failed HTTP requests. Uses exponential backoff with jitter. Default: 3. | [optional] [default to 3]
**retry_base_delay** | **float** | Base delay in seconds for retry backoff. Actual delay &#x3D; base * 2^attempt + jitter. Default: 1.0. | [optional] [default to 1.0]
**retry_max_delay** | **float** | Maximum delay in seconds between retries. Default: 30. | [optional] [default to 30.0]
**respect_retry_after** | **bool** | Respect Retry-After header from 429/503 responses. If False, uses exponential backoff instead. Default: True. | [optional] [default to True]
**proxies** | **List[str]** | List of proxy URLs for rotation. Supports formats: &#39;http://host:port&#39;, &#39;http://user:pass@host:port&#39;, &#39;socks5://host:port&#39;. Proxies rotate on errors or every N requests. | [optional] 
**rotate_proxy_on_error** | **bool** | Rotate to next proxy when request fails. Default: True. | [optional] [default to True]
**rotate_proxy_every_n_requests** | **int** | Rotate proxy every N requests (0 &#x3D; disabled). Useful for avoiding IP-based rate limits. Default: 0 (disabled). | [optional] [default to 0]
**captcha_service_provider** | **str** | Captcha solving service provider: &#39;2captcha&#39;, &#39;anti-captcha&#39;, &#39;capsolver&#39;. If not set, captcha pages are skipped gracefully. | [optional] 
**captcha_service_api_key** | **str** | API key for captcha solving service. Supports secret reference: &#39;{{SECRET.captcha_api_key}}&#39;. Required if captcha_service_provider is set. | [optional] 
**detect_captcha** | **bool** | Detect captcha challenges (Cloudflare, reCAPTCHA, hCaptcha). If detected and no solver configured, page is skipped. Default: True. | [optional] [default to True]
**persist_cookies** | **bool** | Persist cookies across requests within a crawl session. Useful for sites requiring authentication. Default: True. | [optional] [default to True]
**custom_headers** | **Dict[str, str]** | Custom HTTP headers to include in all requests. Example: {&#39;Authorization&#39;: &#39;Bearer token&#39;, &#39;X-Custom&#39;: &#39;value&#39;} | [optional] 
**delay_between_requests** | **float** | Delay in seconds between consecutive requests. Useful for polite crawling and avoiding rate limits. Default: 0 (no delay). | [optional] [default to 0.0]

## Example

```python
from mixpeek.models.web_scraper_extractor_params import WebScraperExtractorParams

# TODO update the JSON string below
json = "{}"
# create an instance of WebScraperExtractorParams from a JSON string
web_scraper_extractor_params_instance = WebScraperExtractorParams.from_json(json)
# print the JSON string representation of the object
print(WebScraperExtractorParams.to_json())

# convert the object into a dict
web_scraper_extractor_params_dict = web_scraper_extractor_params_instance.to_dict()
# create an instance of WebScraperExtractorParams from a dict
web_scraper_extractor_params_from_dict = WebScraperExtractorParams.from_dict(web_scraper_extractor_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


