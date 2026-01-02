from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseRateLimits")


@_attrs_define
class BaseRateLimits:
    """Rate limits by operation type (requests per minute).

    The rate limiting system uses 5 categories aligned with actual resource consumption:

    Categories:
        metadata: Infrastructure and configuration operations (namespaces, collections,
                 retrievers, taxonomies, clusters CRUD). Zero-credit operations with
                 highest rate limits.

        data: Data operations (objects, documents CRUD). Low-credit operations with
              high rate limits.

        search: Search and retrieval operations (retriever/taxonomy execution).
                Medium-credit operations with moderate rate limits.

        upload: File upload operations (credit-intensive: 1 credit/MB). Variable-credit
                operations with lower rate limits.

        compute: Compute operations (cluster execution, batch processing). High-credit
                 operations (10 credits/min video) with lowest rate limits.

    Rate Limit Strategy:
        Higher limits for low-cost operations (metadata, data)
        Lower limits for high-cost operations (upload, compute)
        This aligns API throttling with actual infrastructure costs

    Examples:
        - Creating a namespace: Uses 'metadata' category (fast, cheap)
        - Uploading a file: Uses 'upload' category (slow, expensive per MB)
        - Executing a retriever: Uses 'search' category (moderate cost)
        - Running batch processing: Uses 'compute' category (very expensive)

        Attributes:
            metadata (int | Unset): REQUIRED. Rate limit for infrastructure and configuration operations (namespaces,
                collections, retrievers, taxonomies, clusters CRUD). These are zero-credit operations with highest rate limits
                since they're cheap to execute. Examples: creating collections, updating retrievers, listing namespaces.
                Default: 10.
            data (int | Unset): REQUIRED. Rate limit for data operations (objects, documents CRUD). Low-credit operations
                with high rate limits. Examples: creating documents, updating objects, batch document updates. Default: 10.
            search (int | Unset): REQUIRED. Rate limit for search and retrieval operations (retriever/taxonomy execution).
                Medium-credit operations with moderate rate limits. Examples: executing retrievers, running taxonomy matching.
                Default: 10.
            upload (int | Unset): REQUIRED. Rate limit for file upload operations. Credit-intensive (1 credit/MB) with lower
                rate limits to prevent excessive resource consumption. Examples: uploading files, generating presigned URLs.
                Default: 10.
            compute (int | Unset): REQUIRED. Rate limit for compute operations (cluster execution, batch processing). High-
                credit operations (10 credits/min video) with lowest rate limits. Examples: submitting batches, executing
                clusters, triggering syncs. Default: 10.
    """

    metadata: int | Unset = 10
    data: int | Unset = 10
    search: int | Unset = 10
    upload: int | Unset = 10
    compute: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata

        data = self.data

        search = self.search

        upload = self.upload

        compute = self.compute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if data is not UNSET:
            field_dict["data"] = data
        if search is not UNSET:
            field_dict["search"] = search
        if upload is not UNSET:
            field_dict["upload"] = upload
        if compute is not UNSET:
            field_dict["compute"] = compute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metadata = d.pop("metadata", UNSET)

        data = d.pop("data", UNSET)

        search = d.pop("search", UNSET)

        upload = d.pop("upload", UNSET)

        compute = d.pop("compute", UNSET)

        base_rate_limits = cls(
            metadata=metadata,
            data=data,
            search=search,
            upload=upload,
            compute=compute,
        )

        base_rate_limits.additional_properties = d
        return base_rate_limits

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
