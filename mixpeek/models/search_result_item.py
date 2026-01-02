from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.search_result_item_resource_type import SearchResultItemResourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchResultItem")


@_attrs_define
class SearchResultItem:
    """Individual search result representing a matched resource.

    Contains essential metadata about the matched resource including type,
    ID, name, description, and timestamps. Results are sorted by relevance
    (exact matches first) and creation time.

    Use Cases:
        - Display search results in UI
        - Navigate to specific resources by ID
        - Show resource metadata in search results
        - Filter or sort results client-side

    Fields:
        - resource_type: Type of resource (bucket, collection, etc.)
        - resource_id: Unique identifier for the resource
        - resource_name: Human-readable name
        - description: Optional description text
        - created_at: When the resource was created
        - updated_at: When the resource was last updated (if applicable)

        Attributes:
            resource_type (SearchResultItemResourceType): Type of resource this result represents. REQUIRED. One of:
                'bucket', 'collection', 'retriever', 'taxonomy', 'cluster', 'published_retriever', 'namespace'. Used to identify
                which resource type was matched and how to navigate to it. Example: 'bucket' indicates this is a bucket
                resource.
            resource_id (str): Unique identifier for the resource. REQUIRED. Format depends on resource_type: - bucket:
                'bkt_XXXXXXXX' - collection: 'col_XXXXXXXXXX' - retriever: 'ret_XXXXXXXXXXXXXX' - taxonomy: 'tax_XXXXXXXXXXXX' -
                cluster: 'clust_XXXXXXXXXX' - published_retriever: 'pk_XXXXXXXXXX' - namespace: 'ns_XXXXXXXXXX'. Use this ID to
                fetch the full resource or perform operations on it.
            resource_name (str): Human-readable name of the resource. REQUIRED. This is the field that was matched in the
                search. Corresponds to: bucket_name, collection_name, retriever_name, taxonomy_name, cluster_name, or
                public_name. Example: 'Production Videos', 'Product Embeddings', 'Recommendation Engine', 'my-public-search'.
            created_at (datetime.datetime): Timestamp when the resource was created. REQUIRED. ISO 8601 format with UTC
                timezone. Used for sorting results by creation time.
            description (None | str | Unset): Description of the resource if provided. OPTIONAL - May be null if no
                description was set. Provides additional context about the resource's purpose or contents.
            updated_at (datetime.datetime | None | Unset): Timestamp when the resource was last updated. OPTIONAL - May be
                null if resource has never been updated. ISO 8601 format with UTC timezone.
    """

    resource_type: SearchResultItemResourceType
    resource_id: str
    resource_name: str
    created_at: datetime.datetime
    description: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_type = self.resource_type.value

        resource_id = self.resource_id

        resource_name = self.resource_name

        created_at = self.created_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_type": resource_type,
                "resource_id": resource_id,
                "resource_name": resource_name,
                "created_at": created_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_type = SearchResultItemResourceType(d.pop("resource_type"))

        resource_id = d.pop("resource_id")

        resource_name = d.pop("resource_name")

        created_at = isoparse(d.pop("created_at"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        search_result_item = cls(
            resource_type=resource_type,
            resource_id=resource_id,
            resource_name=resource_name,
            created_at=created_at,
            description=description,
            updated_at=updated_at,
        )

        search_result_item.additional_properties = d
        return search_result_item

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
