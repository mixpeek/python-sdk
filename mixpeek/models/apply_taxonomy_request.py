from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.apply_taxonomy_request_scroll_filters_type_0 import ApplyTaxonomyRequestScrollFiltersType0


T = TypeVar("T", bound="ApplyTaxonomyRequest")


@_attrs_define
class ApplyTaxonomyRequest:
    """Request to apply a taxonomy to an existing collection.

    This endpoint triggers retroactive taxonomy materialization on
    all documents in a collection using distributed Ray processing.

    Use Cases:
        - Apply taxonomy to documents that were ingested before the taxonomy was created
        - Re-apply taxonomy after taxonomy configuration changes
        - Backfill enrichment data for existing collections

    Requirements:
        - taxonomy_id: REQUIRED - Must be an existing, valid taxonomy
        - The taxonomy must already be attached to the collection via taxonomy_applications
        - Documents must exist in the collection

        Attributes:
            taxonomy_id (str): ID of the taxonomy to apply. REQUIRED. Must be an existing taxonomy (tax_*). The taxonomy
                must already be in the collection's taxonomy_applications list.
            scroll_filters (ApplyTaxonomyRequestScrollFiltersType0 | None | Unset): Optional Qdrant filters to limit which
                documents are enriched. NOT REQUIRED. If not provided, all documents in the collection will be enriched. Use to
                process specific subsets (e.g., documents missing enrichment).
            batch_size (int | Unset): Number of documents to process in each parallel batch. NOT REQUIRED. Defaults to 1000.
                Larger batches = fewer Ray tasks but more memory per task. Smaller batches = more Ray tasks but lower memory per
                task. Default: 1000.
            parallelism (int | Unset): Number of parallel Ray workers to use for processing. NOT REQUIRED. Defaults to 4.
                Higher parallelism = faster processing but more cluster resources. Set based on available Ray cluster capacity.
                Default: 4.
    """

    taxonomy_id: str
    scroll_filters: ApplyTaxonomyRequestScrollFiltersType0 | None | Unset = UNSET
    batch_size: int | Unset = 1000
    parallelism: int | Unset = 4
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.apply_taxonomy_request_scroll_filters_type_0 import ApplyTaxonomyRequestScrollFiltersType0

        taxonomy_id = self.taxonomy_id

        scroll_filters: dict[str, Any] | None | Unset
        if isinstance(self.scroll_filters, Unset):
            scroll_filters = UNSET
        elif isinstance(self.scroll_filters, ApplyTaxonomyRequestScrollFiltersType0):
            scroll_filters = self.scroll_filters.to_dict()
        else:
            scroll_filters = self.scroll_filters

        batch_size = self.batch_size

        parallelism = self.parallelism

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taxonomy_id": taxonomy_id,
            }
        )
        if scroll_filters is not UNSET:
            field_dict["scroll_filters"] = scroll_filters
        if batch_size is not UNSET:
            field_dict["batch_size"] = batch_size
        if parallelism is not UNSET:
            field_dict["parallelism"] = parallelism

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.apply_taxonomy_request_scroll_filters_type_0 import ApplyTaxonomyRequestScrollFiltersType0

        d = dict(src_dict)
        taxonomy_id = d.pop("taxonomy_id")

        def _parse_scroll_filters(data: object) -> ApplyTaxonomyRequestScrollFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scroll_filters_type_0 = ApplyTaxonomyRequestScrollFiltersType0.from_dict(data)

                return scroll_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApplyTaxonomyRequestScrollFiltersType0 | None | Unset, data)

        scroll_filters = _parse_scroll_filters(d.pop("scroll_filters", UNSET))

        batch_size = d.pop("batch_size", UNSET)

        parallelism = d.pop("parallelism", UNSET)

        apply_taxonomy_request = cls(
            taxonomy_id=taxonomy_id,
            scroll_filters=scroll_filters,
            batch_size=batch_size,
            parallelism=parallelism,
        )

        apply_taxonomy_request.additional_properties = d
        return apply_taxonomy_request

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
