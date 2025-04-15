"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class CreateCollectionRequestMetadataTypedDict(TypedDict):
    pass


class CreateCollectionRequestMetadata(BaseModel):
    pass


class CreateCollectionRequestTypedDict(TypedDict):
    collection_name: str
    r"""Name for the collection"""
    metadata: NotRequired[Nullable[CreateCollectionRequestMetadataTypedDict]]
    r"""Optional metadata for the collection"""


class CreateCollectionRequest(BaseModel):
    collection_name: str
    r"""Name for the collection"""

    metadata: OptionalNullable[CreateCollectionRequestMetadata] = UNSET
    r"""Optional metadata for the collection"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["metadata"]
        nullable_fields = ["metadata"]
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
