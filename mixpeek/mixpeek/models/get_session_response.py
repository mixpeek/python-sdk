from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.session_status import SessionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_config import AgentConfig
    from ..models.get_session_response_user_memory import GetSessionResponseUserMemory
    from ..models.session_stats import SessionStats


T = TypeVar("T", bound="GetSessionResponse")


@_attrs_define
class GetSessionResponse:
    """Response for retrieving session metadata.

    Attributes:
        session_id: Session identifier
        namespace_id: Namespace identifier
        internal_id: Organization internal ID
        user_id: Optional user identifier
        session_name: Auto-generated session name (null until first message)
        agent_config: Agent configuration
        user_memory: User memory/preferences
        status: Session status
        message_count: Total messages in session
        stats: Session statistics
        created_at: Creation timestamp
        updated_at: Last update timestamp
        last_activity_at: Last activity timestamp
        expires_at: Expiration timestamp

    Example:
        ```python
        response = GetSessionResponse(
            session_id="ses_abc123",
            namespace_id="ns_xyz789",
            internal_id="int_abc123",
            session_name="Video search for ML tutorials",
            agent_config=AgentConfig(...),
            status="active",
            message_count=10,
            stats=SessionStats(...)
        )
        ```

        Attributes:
            session_id (str): Session identifier
            namespace_id (str): Namespace identifier
            internal_id (str): Organization internal ID
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
            status (SessionStatus): Session lifecycle states.

                Attributes:
                    ACTIVE: Session is actively processing messages
                    IDLE: Session exists but no recent activity
                    ARCHIVED: Session archived (read-only)
                    TERMINATED: Session permanently closed
            message_count (int): Total messages in session
            stats (SessionStats): Session usage statistics.

                Tracked in MongoDB session document, updated on each message.
                Use this to display usage metrics in your UI.

                Attributes:
                    total_messages: Total messages sent in session
                    total_tokens: Cumulative tokens used (for cost tracking)
                    total_tool_calls: Total tool invocations
                    avg_latency_ms: Average message latency in milliseconds

                Example:
                    ```python
                    # Display in UI
                    stats = session_response.stats
                    print(f"Messages: {stats.total_messages}")
                    print(f"Tokens used: {stats.total_tokens}")
                    print(f"Tool calls: {stats.total_tool_calls}")
                    print(f"Avg latency: {stats.avg_latency_ms:.0f}ms")
                    ```
            created_at (datetime.datetime): Creation timestamp
            updated_at (datetime.datetime): Last update timestamp
            last_activity_at (datetime.datetime): Last activity timestamp
            expires_at (datetime.datetime): Expiration timestamp
            user_id (None | str | Unset): User identifier
            session_name (None | str | Unset): Auto-generated session name based on first conversation
            user_memory (GetSessionResponseUserMemory | Unset): User memory/preferences
    """

    session_id: str
    namespace_id: str
    internal_id: str
    agent_config: AgentConfig
    status: SessionStatus
    message_count: int
    stats: SessionStats
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_activity_at: datetime.datetime
    expires_at: datetime.datetime
    user_id: None | str | Unset = UNSET
    session_name: None | str | Unset = UNSET
    user_memory: GetSessionResponseUserMemory | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        namespace_id = self.namespace_id

        internal_id = self.internal_id

        agent_config = self.agent_config.to_dict()

        status = self.status.value

        message_count = self.message_count

        stats = self.stats.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        last_activity_at = self.last_activity_at.isoformat()

        expires_at = self.expires_at.isoformat()

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        session_name: None | str | Unset
        if isinstance(self.session_name, Unset):
            session_name = UNSET
        else:
            session_name = self.session_name

        user_memory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_memory, Unset):
            user_memory = self.user_memory.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_id": session_id,
                "namespace_id": namespace_id,
                "internal_id": internal_id,
                "agent_config": agent_config,
                "status": status,
                "message_count": message_count,
                "stats": stats,
                "created_at": created_at,
                "updated_at": updated_at,
                "last_activity_at": last_activity_at,
                "expires_at": expires_at,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if session_name is not UNSET:
            field_dict["session_name"] = session_name
        if user_memory is not UNSET:
            field_dict["user_memory"] = user_memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_config import AgentConfig
        from ..models.get_session_response_user_memory import GetSessionResponseUserMemory
        from ..models.session_stats import SessionStats

        d = dict(src_dict)
        session_id = d.pop("session_id")

        namespace_id = d.pop("namespace_id")

        internal_id = d.pop("internal_id")

        agent_config = AgentConfig.from_dict(d.pop("agent_config"))

        status = SessionStatus(d.pop("status"))

        message_count = d.pop("message_count")

        stats = SessionStats.from_dict(d.pop("stats"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        last_activity_at = isoparse(d.pop("last_activity_at"))

        expires_at = isoparse(d.pop("expires_at"))

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_session_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_name = _parse_session_name(d.pop("session_name", UNSET))

        _user_memory = d.pop("user_memory", UNSET)
        user_memory: GetSessionResponseUserMemory | Unset
        if isinstance(_user_memory, Unset):
            user_memory = UNSET
        else:
            user_memory = GetSessionResponseUserMemory.from_dict(_user_memory)

        get_session_response = cls(
            session_id=session_id,
            namespace_id=namespace_id,
            internal_id=internal_id,
            agent_config=agent_config,
            status=status,
            message_count=message_count,
            stats=stats,
            created_at=created_at,
            updated_at=updated_at,
            last_activity_at=last_activity_at,
            expires_at=expires_at,
            user_id=user_id,
            session_name=session_name,
            user_memory=user_memory,
        )

        get_session_response.additional_properties = d
        return get_session_response

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
