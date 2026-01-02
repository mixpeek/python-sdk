from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.display_config import DisplayConfig


T = TypeVar("T", bound="PatchRetrieverRequest")


@_attrs_define
class PatchRetrieverRequest:
    """Request to update a retriever's metadata.

    **IMPORTANT: Partial Updates with Controlled Mutability**

    This endpoint allows updating ONLY metadata fields. Core retriever logic is immutable
    to ensure consistency for dependent resources (taxonomies, cached results, etc.).

    **✅ Fields You CAN Update (Metadata Only):**
    - `retriever_name`: Rename the retriever
    - `description`: Update documentation
    - `tags`: Update organization tags
    - `display_config`: Update display configuration for publishing

    **❌ Fields You CANNOT Update (Immutable Core Logic):**
    - `input_schema`: Input field definitions (breaks dependent taxonomies)
    - `stages`: Retriever stages and configurations (changes matching behavior)
    - `collection_ids`: Target collections (changes data sources)
    - `budget_limits`: Budget constraints (affects execution behavior)

    **Need to Modify Core Logic?**
    Use POST /retrievers/{retriever_id}/clone instead. Cloning creates a new retriever
    with a new ID, allowing you to:
    - Fix typos in stage names
    - Add or remove stages
    - Change target collections
    - Modify input schema or budget limits

    **Behavior:**
    - All fields are OPTIONAL - provide only what you want to update
    - Version number automatically increments on each update
    - Empty updates (no fields provided) will be rejected with 400 error
    - Original retriever remains unchanged (no destructive operations)

    **Why This Design?**
    - Taxonomies reference retrievers by ID and expect consistent behavior
    - Cached results remain valid after metadata-only changes
    - Version tracking enables auditing and rollback
    - Published retrievers maintain stable behavior for consumers

        Attributes:
            retriever_name (None | str | Unset): Updated retriever name. OPTIONAL - only provide if you want to rename the
                retriever.
            description (None | str | Unset): Updated human-readable description. OPTIONAL - only provide if you want to
                update the description.
            tags (list[str] | None | Unset): Updated tags for organization and filtering. OPTIONAL - replaces existing tags
                if provided.
            display_config (DisplayConfig | None | Unset): Updated display configuration for public retriever UI rendering.
                OPTIONAL - only provide if you want to update the display settings. Defines how the search interface should
                appear when published.
    """

    retriever_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    display_config: DisplayConfig | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.display_config import DisplayConfig

        retriever_name: None | str | Unset
        if isinstance(self.retriever_name, Unset):
            retriever_name = UNSET
        else:
            retriever_name = self.retriever_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        display_config: dict[str, Any] | None | Unset
        if isinstance(self.display_config, Unset):
            display_config = UNSET
        elif isinstance(self.display_config, DisplayConfig):
            display_config = self.display_config.to_dict()
        else:
            display_config = self.display_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retriever_name is not UNSET:
            field_dict["retriever_name"] = retriever_name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if display_config is not UNSET:
            field_dict["display_config"] = display_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.display_config import DisplayConfig

        d = dict(src_dict)

        def _parse_retriever_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retriever_name = _parse_retriever_name(d.pop("retriever_name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_display_config(data: object) -> DisplayConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                display_config_type_0 = DisplayConfig.from_dict(data)

                return display_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DisplayConfig | None | Unset, data)

        display_config = _parse_display_config(d.pop("display_config", UNSET))

        patch_retriever_request = cls(
            retriever_name=retriever_name,
            description=description,
            tags=tags,
            display_config=display_config,
        )

        patch_retriever_request.additional_properties = d
        return patch_retriever_request

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
