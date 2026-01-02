from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstantiateScaffoldRequest")


@_attrs_define
class InstantiateScaffoldRequest:
    """Request to instantiate a scaffold template.

    Only namespace_name is required. Other names use scaffold defaults.

    Options:
        include_sample_data: If true, clone from demo namespace with sample data.
                            If false (default), create empty resources.

    Example:
        # Empty scaffold
        {"namespace_name": "my_app"}

        # With sample data
        {"namespace_name": "my_app", "include_sample_data": true}

        Attributes:
            namespace_name (str): Name for the new namespace (required, must be unique)
            namespace_description (None | str | Unset): Optional description for the namespace
            bucket_name (None | str | Unset): Override default bucket name from scaffold
            collection_name (None | str | Unset): Override default collection name from scaffold
            retriever_name (None | str | Unset): Override default retriever name from scaffold
            include_sample_data (bool | Unset): If true, include sample data from demo namespace. If false, create empty
                resources. Default: False.
    """

    namespace_name: str
    namespace_description: None | str | Unset = UNSET
    bucket_name: None | str | Unset = UNSET
    collection_name: None | str | Unset = UNSET
    retriever_name: None | str | Unset = UNSET
    include_sample_data: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace_name = self.namespace_name

        namespace_description: None | str | Unset
        if isinstance(self.namespace_description, Unset):
            namespace_description = UNSET
        else:
            namespace_description = self.namespace_description

        bucket_name: None | str | Unset
        if isinstance(self.bucket_name, Unset):
            bucket_name = UNSET
        else:
            bucket_name = self.bucket_name

        collection_name: None | str | Unset
        if isinstance(self.collection_name, Unset):
            collection_name = UNSET
        else:
            collection_name = self.collection_name

        retriever_name: None | str | Unset
        if isinstance(self.retriever_name, Unset):
            retriever_name = UNSET
        else:
            retriever_name = self.retriever_name

        include_sample_data = self.include_sample_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace_name": namespace_name,
            }
        )
        if namespace_description is not UNSET:
            field_dict["namespace_description"] = namespace_description
        if bucket_name is not UNSET:
            field_dict["bucket_name"] = bucket_name
        if collection_name is not UNSET:
            field_dict["collection_name"] = collection_name
        if retriever_name is not UNSET:
            field_dict["retriever_name"] = retriever_name
        if include_sample_data is not UNSET:
            field_dict["include_sample_data"] = include_sample_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        namespace_name = d.pop("namespace_name")

        def _parse_namespace_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace_description = _parse_namespace_description(d.pop("namespace_description", UNSET))

        def _parse_bucket_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bucket_name = _parse_bucket_name(d.pop("bucket_name", UNSET))

        def _parse_collection_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_name = _parse_collection_name(d.pop("collection_name", UNSET))

        def _parse_retriever_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retriever_name = _parse_retriever_name(d.pop("retriever_name", UNSET))

        include_sample_data = d.pop("include_sample_data", UNSET)

        instantiate_scaffold_request = cls(
            namespace_name=namespace_name,
            namespace_description=namespace_description,
            bucket_name=bucket_name,
            collection_name=collection_name,
            retriever_name=retriever_name,
            include_sample_data=include_sample_data,
        )

        instantiate_scaffold_request.additional_properties = d
        return instantiate_scaffold_request

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
