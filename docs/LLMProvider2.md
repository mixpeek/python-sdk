# LLMProvider2

Supported LLM providers for content generation.  Each provider has different strengths, pricing, and multimodal capabilities. Choose based on your use case, performance requirements, and budget.  Values:     OPENAI: OpenAI GPT models (GPT-4o, GPT-4.1, O3-mini)         - Best for: General purpose, vision tasks, structured outputs         - Multimodal: Text, images         - Performance: Fast (100-500ms), reliable         - Cost: Moderate to high ($0.15-$10 per 1M tokens)         - Use when: Need high-quality generation with vision support      GOOGLE: Google Gemini models (Gemini 1.5 Flash, Gemini 2.5 Flash)         - Best for: Fast generation, video understanding, cost-efficiency         - Multimodal: Text, images, video, audio, PDFs         - Performance: Very fast (50-200ms)         - Cost: Low to moderate ($0.075-$0.40 per 1M tokens)         - Use when: Need video/audio/PDF support or cost-efficiency      ANTHROPIC: Anthropic Claude models (Claude 3.5 Sonnet, Claude 3.5 Haiku)         - Best for: Long context, complex reasoning, safety         - Multimodal: Text, images         - Performance: Moderate (200-800ms)         - Cost: Moderate to high ($0.25-$15 per 1M tokens)         - Use when: Need long context or complex reasoning  Examples:     - Use OPENAI for production with structured JSON outputs     - Use GOOGLE for video summarization and cost-sensitive workloads     - Use ANTHROPIC for complex reasoning with long documents

## Enum

* `OPENAI` (value: `'openai'`)

* `GOOGLE` (value: `'google'`)

* `ANTHROPIC` (value: `'anthropic'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


