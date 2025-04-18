"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bucketschema_input import BucketSchemaInput, BucketSchemaInputTypedDict
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class BucketCreateRequestMetadataTypedDict(TypedDict):
    r"""Additional metadata for the bucket"""


class BucketCreateRequestMetadata(BaseModel):
    r"""Additional metadata for the bucket"""


class BucketCreateRequestTypedDict(TypedDict):
    r"""Request model for creating a new bucket"""

    bucket_name: str
    r"""Human-readable name for the bucket"""
    bucket_schema: BucketSchemaInputTypedDict
    r"""Schema definition for bucket objects"""
    description: NotRequired[Nullable[str]]
    r"""Description of the bucket"""
    metadata: NotRequired[BucketCreateRequestMetadataTypedDict]
    r"""Additional metadata for the bucket"""


class BucketCreateRequest(BaseModel):
    r"""Request model for creating a new bucket"""

    bucket_name: str
    r"""Human-readable name for the bucket"""

    bucket_schema: BucketSchemaInput
    r"""Schema definition for bucket objects"""

    description: OptionalNullable[str] = UNSET
    r"""Description of the bucket"""

    metadata: Optional[BucketCreateRequestMetadata] = None
    r"""Additional metadata for the bucket"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description", "metadata"]
        nullable_fields = ["description"]
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
