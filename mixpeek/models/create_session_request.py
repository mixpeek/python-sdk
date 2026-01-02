from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_config import AgentConfig
    from ..models.create_session_request_metadata import CreateSessionRequestMetadata
    from ..models.create_session_request_user_memory import CreateSessionRequestUserMemory
    from ..models.session_quotas import SessionQuotas


T = TypeVar("T", bound="CreateSessionRequest")


@_attrs_define
class CreateSessionRequest:
    """Request payload for creating a new agent session.

    Attributes:
        agent_config: Agent configuration (model, temperature, tools, etc.)
        quotas: Optional session quotas and rate limits
        user_id: Optional user identifier
        user_memory: Optional initial user memory/preferences
        metadata: Optional session metadata

    Example:
        ```python
        request = CreateSessionRequest(
            agent_config=AgentConfig(
                model="claude-3-5-sonnet-20241022",
                temperature=0.7,
                available_tools=["search_retrievers", "execute_retriever"]
            ),
            quotas=SessionQuotas(
                max_messages=100,
                max_tokens_total=100000
            ),
            user_id="user_123",
            user_memory={"preferences": {"language": "en"}}
        )
        ```

        Attributes:
            agent_config (AgentConfig): Agent configuration for session.

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
            quotas (None | SessionQuotas | Unset): Session quotas and rate limits (OPTIONAL)
            user_id (None | str | Unset): User identifier (OPTIONAL)
            user_memory (CreateSessionRequestUserMemory | Unset): Initial user memory/preferences (OPTIONAL)
            metadata (CreateSessionRequestMetadata | Unset): Session metadata (OPTIONAL)
            enable_memory (bool | Unset): Enable semantic memory for conversation context (OPTIONAL, default: True) Default:
                True.
    """

    agent_config: AgentConfig
    quotas: None | SessionQuotas | Unset = UNSET
    user_id: None | str | Unset = UNSET
    user_memory: CreateSessionRequestUserMemory | Unset = UNSET
    metadata: CreateSessionRequestMetadata | Unset = UNSET
    enable_memory: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_quotas import SessionQuotas

        agent_config = self.agent_config.to_dict()

        quotas: dict[str, Any] | None | Unset
        if isinstance(self.quotas, Unset):
            quotas = UNSET
        elif isinstance(self.quotas, SessionQuotas):
            quotas = self.quotas.to_dict()
        else:
            quotas = self.quotas

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        user_memory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_memory, Unset):
            user_memory = self.user_memory.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        enable_memory = self.enable_memory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_config": agent_config,
            }
        )
        if quotas is not UNSET:
            field_dict["quotas"] = quotas
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_memory is not UNSET:
            field_dict["user_memory"] = user_memory
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if enable_memory is not UNSET:
            field_dict["enable_memory"] = enable_memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_config import AgentConfig
        from ..models.create_session_request_metadata import CreateSessionRequestMetadata
        from ..models.create_session_request_user_memory import CreateSessionRequestUserMemory
        from ..models.session_quotas import SessionQuotas

        d = dict(src_dict)
        agent_config = AgentConfig.from_dict(d.pop("agent_config"))

        def _parse_quotas(data: object) -> None | SessionQuotas | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                quotas_type_0 = SessionQuotas.from_dict(data)

                return quotas_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionQuotas | Unset, data)

        quotas = _parse_quotas(d.pop("quotas", UNSET))

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        _user_memory = d.pop("user_memory", UNSET)
        user_memory: CreateSessionRequestUserMemory | Unset
        if isinstance(_user_memory, Unset):
            user_memory = UNSET
        else:
            user_memory = CreateSessionRequestUserMemory.from_dict(_user_memory)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateSessionRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateSessionRequestMetadata.from_dict(_metadata)

        enable_memory = d.pop("enable_memory", UNSET)

        create_session_request = cls(
            agent_config=agent_config,
            quotas=quotas,
            user_id=user_id,
            user_memory=user_memory,
            metadata=metadata,
            enable_memory=enable_memory,
        )

        create_session_request.additional_properties = d
        return create_session_request

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
