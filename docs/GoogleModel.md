# GoogleModel

Google Gemini model identifiers for LLM generation.  Gemini models excel at multimodal understanding with best-in-class video support. All models support text, images, video, audio, and PDFs.  Values:     GEMINI_2_0_FLASH: Latest Gemini 2.0 Flash model (recommended)         - Use for: Fastest generation, highest quality multimodal         - Context: 1M tokens         - Multimodal: Text, images, video (up to 2hr), audio, PDFs         - Cost: $0.075/1M input, $0.30/1M output         - Performance: 50-200ms per request (fastest multimodal model)         - When to use: Default choice for all Gemini use cases      GEMINI_2_0_FLASH_EXP: Experimental Gemini 2.0 Flash model         - Use for: Testing latest features before stable release         - Same capabilities as GEMINI_2_0_FLASH  Note: Gemini 1.5 models (gemini-1.5-flash, gemini-1.5-pro) were retired by Google in April 2025. Use GEMINI_2_0_FLASH instead.  Examples:     - Use GEMINI_2_0_FLASH for video scene understanding (best video support)     - Use GEMINI_2_0_FLASH for cost-effective PDF extraction (best price/performance)

## Enum

* `GEMINI_MINUS_2_DOT_0_MINUS_FLASH` (value: `'gemini-2.0-flash'`)

* `GEMINI_MINUS_2_DOT_0_MINUS_FLASH_MINUS_EXP` (value: `'gemini-2.0-flash-exp'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


