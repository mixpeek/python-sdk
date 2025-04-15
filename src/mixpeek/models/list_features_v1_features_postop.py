"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .listfeaturesrequest import ListFeaturesRequest, ListFeaturesRequestTypedDict
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from mixpeek.utils import (
    FieldMetadata,
    HeaderMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListFeaturesV1FeaturesPostRequestTypedDict(TypedDict):
    list_features_request: ListFeaturesRequestTypedDict
    offset_feature_id: NotRequired[Nullable[str]]
    r"""The offset id to start returning results from. Used for pagination"""
    page_size: NotRequired[int]
    x_namespace: NotRequired[Nullable[str]]
    r"""Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint."""


class ListFeaturesV1FeaturesPostRequest(BaseModel):
    list_features_request: Annotated[
        ListFeaturesRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    offset_feature_id: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""The offset id to start returning results from. Used for pagination"""

    page_size: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 10

    x_namespace: Annotated[
        OptionalNullable[str],
        pydantic.Field(alias="X-Namespace"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = UNSET
    r"""Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["offset_feature_id", "page_size", "X-Namespace"]
        nullable_fields = ["offset_feature_id", "X-Namespace"]
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
