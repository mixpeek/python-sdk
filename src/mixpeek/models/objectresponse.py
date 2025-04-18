"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .blobmodel import BlobModel, BlobModelTypedDict
from .taskstatus import TaskStatus
from datetime import datetime
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List
from typing_extensions import NotRequired, TypedDict


class ObjectResponseMetadataTypedDict(TypedDict):
    r"""Additional metadata for the object, appended to downstream documents of connected collections"""


class ObjectResponseMetadata(BaseModel):
    r"""Additional metadata for the object, appended to downstream documents of connected collections"""


class ObjectResponseTypedDict(TypedDict):
    r"""Response model for bucket objects"""

    object_id: str
    r"""Unique identifier for the object"""
    bucket_id: str
    r"""ID of the bucket this object belongs to"""
    blobs: List[BlobModelTypedDict]
    r"""List of blobs contained in this object"""
    status: TaskStatus
    metadata: ObjectResponseMetadataTypedDict
    r"""Additional metadata for the object, appended to downstream documents of connected collections"""
    task_id: NotRequired[Nullable[str]]
    r"""ID of the task that created this object, used to track the object creation progress and status"""
    key: NotRequired[Nullable[str]]
    r"""Storage key/path of the object, used to retrieve the object from storage"""
    created_by: NotRequired[Nullable[str]]
    r"""Identifier of the entity that created this object"""
    error: NotRequired[Nullable[str]]
    r"""Error message if the object processing failed"""
    created_at: NotRequired[Nullable[datetime]]
    r"""Timestamp when the object was created"""
    updated_at: NotRequired[Nullable[datetime]]
    r"""Timestamp when the object was last updated"""


class ObjectResponse(BaseModel):
    r"""Response model for bucket objects"""

    object_id: str
    r"""Unique identifier for the object"""

    bucket_id: str
    r"""ID of the bucket this object belongs to"""

    blobs: List[BlobModel]
    r"""List of blobs contained in this object"""

    status: TaskStatus

    metadata: ObjectResponseMetadata
    r"""Additional metadata for the object, appended to downstream documents of connected collections"""

    task_id: OptionalNullable[str] = UNSET
    r"""ID of the task that created this object, used to track the object creation progress and status"""

    key: OptionalNullable[str] = UNSET
    r"""Storage key/path of the object, used to retrieve the object from storage"""

    created_by: OptionalNullable[str] = UNSET
    r"""Identifier of the entity that created this object"""

    error: OptionalNullable[str] = UNSET
    r"""Error message if the object processing failed"""

    created_at: OptionalNullable[datetime] = UNSET
    r"""Timestamp when the object was created"""

    updated_at: OptionalNullable[datetime] = UNSET
    r"""Timestamp when the object was last updated"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "task_id",
            "key",
            "created_by",
            "error",
            "created_at",
            "updated_at",
        ]
        nullable_fields = [
            "task_id",
            "key",
            "created_by",
            "error",
            "created_at",
            "updated_at",
        ]
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
