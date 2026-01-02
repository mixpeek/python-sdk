from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentConfig")


@_attrs_define
class AgentConfig:
    """Agent configuration for session.

    This config is immutable after session creation (similar to RetrieverConfig).
    To change agent config, create a new session.

    Attributes:
        model: LLM model identifier. Supported models:
            - claude-3-5-sonnet-20241022 (recommended)
            - claude-3-haiku-20240307 (faster, cheaper)
            - claude-3-opus-20240229 (most capable)
        temperature: Sampling temperature for LLM responses (0.0-2.0)
            - 0.0-0.3: More deterministic, focused responses
            - 0.5-0.7: Balanced creativity and coherence
            - 0.8-2.0: More creative, varied responses
        max_tokens: Maximum tokens per response (1-100000)
        system_prompt: System prompt that defines agent behavior and persona
        available_tools: List of tools the agent can call

    Available Tools:
        RETRIEVER TOOLS:
        - list_retrievers: List available search pipelines
        - get_retriever: Get retriever configuration
        - explain_retriever: Understand how a retriever processes queries
        - execute_retriever: Run a search query
        - search_retrievers: Search for retrievers

        COLLECTION TOOLS:
        - list_collections: List document collections
        - get_collection: Get collection details
        - create_collection: Create new collection
        - update_collection: Update collection
        - delete_collection: Delete collection

        TAXONOMY TOOLS:
        - list_taxonomies: List classification schemas
        - get_taxonomy: Get taxonomy details
        - create_taxonomy: Create new taxonomy
        - update_taxonomy: Update taxonomy
        - delete_taxonomy: Delete taxonomy

        REGISTRY TOOLS:
        - list_stages: List available retriever stage types
        - list_extractors: List available feature extractors

        INGEST TOOLS:
        - ingest_document: Add documents to a collection

    Example:
        ```python
        config = AgentConfig(
            model="claude-3-5-sonnet-20241022",
            temperature=0.7,
            max_tokens=4096,
            system_prompt="You are a helpful video search assistant.",
            available_tools=[
                "list_retrievers",
                "execute_retriever",
                "list_collections"
            ]
        )
        ```

        Attributes:
            model (str | Unset): LLM model identifier. Options: 'gemini-2.0-flash' (fastest, cheapest), 'gemini-2.5-pro'
                (better quality), 'gpt-4o-mini', 'gpt-4o' Default: 'gemini-2.0-flash'.
            temperature (float | Unset): Sampling temperature for LLM responses (0.0-2.0). Lower values (0.0-0.3) are more
                deterministic. Higher values (0.8-2.0) are more creative. Default: 0.7.
            max_tokens (int | Unset): Maximum tokens per response Default: 4096.
            system_prompt (str | Unset): System prompt that defines agent behavior and persona Default: "You are a helpful
                AI assistant with access to Mixpeek's data infrastructure.".
            available_tools (list[str] | Unset): List of tool names the agent can call. Available tools: RETRIEVER:
                list_retrievers, get_retriever, explain_retriever, execute_retriever, search_retrievers. COLLECTION:
                list_collections, get_collection, create_collection, update_collection, delete_collection. TAXONOMY:
                list_taxonomies, get_taxonomy, create_taxonomy, update_taxonomy, delete_taxonomy. REGISTRY: list_stages,
                list_extractors. INGEST: ingest_document. CLUSTER: list_clusters. OBJECT: get_object.
    """

    model: str | Unset = "gemini-2.0-flash"
    temperature: float | Unset = 0.7
    max_tokens: int | Unset = 4096
    system_prompt: str | Unset = "You are a helpful AI assistant with access to Mixpeek's data infrastructure."
    available_tools: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        temperature = self.temperature

        max_tokens = self.max_tokens

        system_prompt = self.system_prompt

        available_tools: list[str] | Unset = UNSET
        if not isinstance(self.available_tools, Unset):
            available_tools = self.available_tools

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model is not UNSET:
            field_dict["model"] = model
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if available_tools is not UNSET:
            field_dict["available_tools"] = available_tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model", UNSET)

        temperature = d.pop("temperature", UNSET)

        max_tokens = d.pop("max_tokens", UNSET)

        system_prompt = d.pop("system_prompt", UNSET)

        available_tools = cast(list[str], d.pop("available_tools", UNSET))

        agent_config = cls(
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            system_prompt=system_prompt,
            available_tools=available_tools,
        )

        agent_config.additional_properties = d
        return agent_config

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
