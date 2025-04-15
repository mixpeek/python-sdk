"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .assets_model_searchquery import (
    AssetsModelSearchQuery,
    AssetsModelSearchQueryTypedDict,
)
from .logicaloperator import LogicalOperator, LogicalOperatorTypedDict
from .sortoption import SortOption, SortOptionTypedDict
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List
from typing_extensions import NotRequired, TypedDict


class SearchAssetsRequestTypedDict(TypedDict):
    collections: List[str]
    r"""List of Collection IDs or Names to search within, required"""
    query: NotRequired[Nullable[AssetsModelSearchQueryTypedDict]]
    r"""Structured query object specifying which fields to search in and what to search for"""
    filters: NotRequired[Nullable[LogicalOperatorTypedDict]]
    r"""Complex nested query filters"""
    sort: NotRequired[Nullable[SortOptionTypedDict]]
    r"""List of fields to sort by"""
    select: NotRequired[Nullable[List[str]]]
    r"""List of fields to return in results"""
    return_url: NotRequired[Nullable[bool]]
    r"""Return the presigned URL for the asset and preview asset, this will introduce additional latency"""


class SearchAssetsRequest(BaseModel):
    collections: List[str]
    r"""List of Collection IDs or Names to search within, required"""

    query: OptionalNullable[AssetsModelSearchQuery] = UNSET
    r"""Structured query object specifying which fields to search in and what to search for"""

    filters: OptionalNullable[LogicalOperator] = UNSET
    r"""Complex nested query filters"""

    sort: OptionalNullable[SortOption] = UNSET
    r"""List of fields to sort by"""

    select: OptionalNullable[List[str]] = UNSET
    r"""List of fields to return in results"""

    return_url: OptionalNullable[bool] = UNSET
    r"""Return the presigned URL for the asset and preview asset, this will introduce additional latency"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["query", "filters", "sort", "select", "return_url"]
        nullable_fields = ["query", "filters", "sort", "select", "return_url"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
