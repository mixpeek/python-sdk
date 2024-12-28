"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .assetupdate import AssetUpdate, AssetUpdateTypedDict
from .videosettings import VideoSettings, VideoSettingsTypedDict
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ProcessVideoURLInputMetadataTypedDict(TypedDict):
    r"""Additional metadata associated with the asset. Can include any key-value pairs relevant to the asset."""


class ProcessVideoURLInputMetadata(BaseModel):
    r"""Additional metadata associated with the asset. Can include any key-value pairs relevant to the asset."""


class ProcessVideoURLInputTypedDict(TypedDict):
    url: str
    r"""The URL of the asset to be processed. Must be a valid HTTP or HTTPS URL."""
    collection: str
    r"""Unique identifier for the collection where the processed asset will be stored, can be the collection name or collection ID. If neither exist, the collection will be created."""
    asset_update: NotRequired[Nullable[AssetUpdateTypedDict]]
    r"""Controls how processing results are stored - either creating a new asset or updating an existing one."""
    metadata: NotRequired[ProcessVideoURLInputMetadataTypedDict]
    r"""Additional metadata associated with the asset. Can include any key-value pairs relevant to the asset."""
    skip_duplicate: NotRequired[Nullable[bool]]
    r"""Makes feature extraction idempotent. When True and a duplicate file hash is found, copies features from the existing asset instead of reprocessing. This allows the same file to be used multiple times with different metadata while avoiding redundant processing."""
    feature_extractors: NotRequired[Nullable[List[VideoSettingsTypedDict]]]
    r"""Settings for video processing. Only applicable if the URL points to a video file."""


class ProcessVideoURLInput(BaseModel):
    url: str
    r"""The URL of the asset to be processed. Must be a valid HTTP or HTTPS URL."""

    collection: str
    r"""Unique identifier for the collection where the processed asset will be stored, can be the collection name or collection ID. If neither exist, the collection will be created."""

    asset_update: OptionalNullable[AssetUpdate] = UNSET
    r"""Controls how processing results are stored - either creating a new asset or updating an existing one."""

    metadata: Optional[ProcessVideoURLInputMetadata] = None
    r"""Additional metadata associated with the asset. Can include any key-value pairs relevant to the asset."""

    skip_duplicate: OptionalNullable[bool] = UNSET
    r"""Makes feature extraction idempotent. When True and a duplicate file hash is found, copies features from the existing asset instead of reprocessing. This allows the same file to be used multiple times with different metadata while avoiding redundant processing."""

    feature_extractors: OptionalNullable[List[VideoSettings]] = UNSET
    r"""Settings for video processing. Only applicable if the URL points to a video file."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "asset_update",
            "metadata",
            "skip_duplicate",
            "feature_extractors",
        ]
        nullable_fields = ["asset_update", "skip_duplicate", "feature_extractors"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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
