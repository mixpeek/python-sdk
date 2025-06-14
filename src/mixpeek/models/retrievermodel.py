"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .retrievercacheconfig import RetrieverCacheConfig, RetrieverCacheConfigTypedDict
from .retrieverschema_output import (
    RetrieverSchemaOutput,
    RetrieverSchemaOutputTypedDict,
)
from .stageconfig_output import StageConfigOutput, StageConfigOutputTypedDict
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class RetrieverModelTypedDict(TypedDict):
    r"""Definition of a retriever"""

    retriever_name: str
    r"""Name of the retriever"""
    input_schema: RetrieverSchemaOutputTypedDict
    r"""Schema definition for retriever inputs"""
    collection_ids: List[str]
    r"""List of collection IDs to search in"""
    stages: List[StageConfigOutputTypedDict]
    r"""List of stages to execute in order"""
    retriever_id: NotRequired[str]
    r"""Unique identifier for the retriever"""
    description: NotRequired[Nullable[str]]
    r"""Description of the retriever"""
    metadata: NotRequired[Dict[str, Any]]
    cache_config: NotRequired[Nullable[RetrieverCacheConfigTypedDict]]
    r"""Configuration for retriever-level caching"""


class RetrieverModel(BaseModel):
    r"""Definition of a retriever"""

    retriever_name: str
    r"""Name of the retriever"""

    input_schema: RetrieverSchemaOutput
    r"""Schema definition for retriever inputs"""

    collection_ids: List[str]
    r"""List of collection IDs to search in"""

    stages: List[StageConfigOutput]
    r"""List of stages to execute in order"""

    retriever_id: Optional[str] = None
    r"""Unique identifier for the retriever"""

    description: OptionalNullable[str] = UNSET
    r"""Description of the retriever"""

    metadata: Optional[Dict[str, Any]] = None

    cache_config: OptionalNullable[RetrieverCacheConfig] = UNSET
    r"""Configuration for retriever-level caching"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["retriever_id", "description", "metadata", "cache_config"]
        nullable_fields = ["description", "cache_config"]
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
