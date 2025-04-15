"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .assetupdate import AssetUpdate, AssetUpdateTypedDict
from .textsettings import TextSettings, TextSettingsTypedDict
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ProcessTextInputMetadataTypedDict(TypedDict):
    r"""Additional metadata associated with the file. Can include any key-value pairs relevant to the file."""


class ProcessTextInputMetadata(BaseModel):
    r"""Additional metadata associated with the file. Can include any key-value pairs relevant to the file."""


class ProcessTextInputTypedDict(TypedDict):
    collection: str
    r"""Unique identifier for the collection where the processed asset will be stored, can be the collection name or collection ID. If neither exist, the collection will be created."""
    asset_update: NotRequired[Nullable[AssetUpdateTypedDict]]
    r"""Controls how processing results are stored - either creating a new asset or updating an existing one."""
    metadata: NotRequired[ProcessTextInputMetadataTypedDict]
    r"""Additional metadata associated with the file. Can include any key-value pairs relevant to the file."""
    feature_extractors: NotRequired[Nullable[TextSettingsTypedDict]]
    r"""Settings for text processing."""
    skip_duplicate: NotRequired[Nullable[bool]]
    r"""Skips processing when a duplicate hash is found and stores an error by the task_id with the existing asset_id"""


class ProcessTextInput(BaseModel):
    collection: str
    r"""Unique identifier for the collection where the processed asset will be stored, can be the collection name or collection ID. If neither exist, the collection will be created."""

    asset_update: OptionalNullable[AssetUpdate] = UNSET
    r"""Controls how processing results are stored - either creating a new asset or updating an existing one."""

    metadata: Optional[ProcessTextInputMetadata] = None
    r"""Additional metadata associated with the file. Can include any key-value pairs relevant to the file."""

    feature_extractors: OptionalNullable[TextSettings] = UNSET
    r"""Settings for text processing."""

    skip_duplicate: OptionalNullable[bool] = UNSET
    r"""Skips processing when a duplicate hash is found and stores an error by the task_id with the existing asset_id"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "asset_update",
            "metadata",
            "feature_extractors",
            "skip_duplicate",
        ]
        nullable_fields = ["asset_update", "feature_extractors", "skip_duplicate"]
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
