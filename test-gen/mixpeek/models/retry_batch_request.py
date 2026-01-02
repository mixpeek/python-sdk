from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.retry_batch_request_retry_mode import RetryBatchRequestRetryMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="RetryBatchRequest")


@_attrs_define
class RetryBatchRequest:
    """Request to retry failed documents in a batch.

    Allows selective retry of failed documents with intelligent filtering by error type
    and tier. Retries use exponential backoff and respect max retry limits.

    Use Cases:
        - Retry only transient errors after resolving temporary infrastructure issues
        - Retry specific processing tiers that failed
        - Retry all failed documents regardless of error type (force retry)

    Requirements:
        - retry_mode: REQUIRED. Determines which documents to retry
        - tier_nums: OPTIONAL. Only retry failures from specific tiers (empty = all tiers)
        - max_retry_count: OPTIONAL. Skip documents that have been retried this many times

    Behavior:
        - 'transient_only': Retries only transient errors (network, timeout, rate limit)
        - 'all': Retries both transient and permanent errors
        - Documents beyond max_retry_count are excluded from retry
        - Each retry increments the document's retry_count

        Attributes:
            retry_mode (RetryBatchRequestRetryMode | Unset): Determines which types of failed documents to retry.
                'transient_only': Only retry documents that failed with transient errors (network issues, timeouts, rate
                limits). This is the recommended default as it avoids retrying documents with permanent failures (invalid data,
                missing fields, incompatible formats). 'all': Retry all failed documents regardless of error type. Use this for
                force retries after fixing data issues or updating extraction logic. Default:
                RetryBatchRequestRetryMode.TRANSIENT_ONLY.
            tier_nums (list[int] | None | Unset): List of specific tier numbers to retry failures from. OPTIONAL - If not
                provided or empty list, retries failures from all tiers. Use this to selectively retry a specific processing
                stage. Example: [2] would only retry failures from tier 2 (the third processing stage). Tier numbering starts at
                0 (bucket → collection), tier 1+ are collection → collection.
            max_retry_count (int | Unset): Maximum number of times a document can be retried. Documents that have been
                retried this many times already are excluded. Prevents infinite retry loops for documents with persistent
                issues. Default is 3 retries per document. Set to higher value for more aggressive retries. Default: 3.
    """

    retry_mode: RetryBatchRequestRetryMode | Unset = RetryBatchRequestRetryMode.TRANSIENT_ONLY
    tier_nums: list[int] | None | Unset = UNSET
    max_retry_count: int | Unset = 3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retry_mode: str | Unset = UNSET
        if not isinstance(self.retry_mode, Unset):
            retry_mode = self.retry_mode.value

        tier_nums: list[int] | None | Unset
        if isinstance(self.tier_nums, Unset):
            tier_nums = UNSET
        elif isinstance(self.tier_nums, list):
            tier_nums = self.tier_nums

        else:
            tier_nums = self.tier_nums

        max_retry_count = self.max_retry_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retry_mode is not UNSET:
            field_dict["retry_mode"] = retry_mode
        if tier_nums is not UNSET:
            field_dict["tier_nums"] = tier_nums
        if max_retry_count is not UNSET:
            field_dict["max_retry_count"] = max_retry_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _retry_mode = d.pop("retry_mode", UNSET)
        retry_mode: RetryBatchRequestRetryMode | Unset
        if isinstance(_retry_mode, Unset):
            retry_mode = UNSET
        else:
            retry_mode = RetryBatchRequestRetryMode(_retry_mode)

        def _parse_tier_nums(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tier_nums_type_0 = cast(list[int], data)

                return tier_nums_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        tier_nums = _parse_tier_nums(d.pop("tier_nums", UNSET))

        max_retry_count = d.pop("max_retry_count", UNSET)

        retry_batch_request = cls(
            retry_mode=retry_mode,
            tier_nums=tier_nums,
            max_retry_count=max_retry_count,
        )

        retry_batch_request.additional_properties = d
        return retry_batch_request

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
