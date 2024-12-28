"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .vectormodel import VectorModel
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class VideoTranscriptionSettingsJSONOutputTypedDict(TypedDict):
    r"""JSON format for the response"""


class VideoTranscriptionSettingsJSONOutput(BaseModel):
    r"""JSON format for the response"""


class VideoTranscriptionSettingsTypedDict(TypedDict):
    enabled: NotRequired[bool]
    r"""Enable video transcription"""
    prompt: NotRequired[Nullable[str]]
    json_output: NotRequired[VideoTranscriptionSettingsJSONOutputTypedDict]
    r"""JSON format for the response"""
    embedding_model: NotRequired[Nullable[VectorModel]]
    r"""Name of the vector model to use for embedding the text output. If embedding_model is duplicated, the vector will be overwritten."""


class VideoTranscriptionSettings(BaseModel):
    enabled: Optional[bool] = True
    r"""Enable video transcription"""

    prompt: OptionalNullable[str] = UNSET

    json_output: Optional[VideoTranscriptionSettingsJSONOutput] = None
    r"""JSON format for the response"""

    embedding_model: OptionalNullable[VectorModel] = UNSET
    r"""Name of the vector model to use for embedding the text output. If embedding_model is duplicated, the vector will be overwritten."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["enabled", "prompt", "json_output", "embedding_model"]
        nullable_fields = ["prompt", "embedding_model"]
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
