"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .attributebasedconfig import AttributeBasedConfig, AttributeBasedConfigTypedDict
from .automaticnaming import AutomaticNaming, AutomaticNamingTypedDict
from .clustertype import ClusterType
from .vectorbasedconfig import VectorBasedConfig, VectorBasedConfigTypedDict
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CreateClusterRequestTypedDict(TypedDict):
    collection_id: str
    r"""ID of the collection to cluster"""
    cluster_name: NotRequired[Nullable[str]]
    r"""Name for the cluster (auto-generated if empty)"""
    cluster_type: NotRequired[ClusterType]
    vector_config: NotRequired[Nullable[VectorBasedConfigTypedDict]]
    attribute_config: NotRequired[Nullable[AttributeBasedConfigTypedDict]]
    automatic_naming: NotRequired[AutomaticNamingTypedDict]


class CreateClusterRequest(BaseModel):
    collection_id: str
    r"""ID of the collection to cluster"""

    cluster_name: OptionalNullable[str] = UNSET
    r"""Name for the cluster (auto-generated if empty)"""

    cluster_type: Optional[ClusterType] = None

    vector_config: OptionalNullable[VectorBasedConfig] = UNSET

    attribute_config: OptionalNullable[AttributeBasedConfig] = UNSET

    automatic_naming: Optional[AutomaticNaming] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "cluster_name",
            "cluster_type",
            "vector_config",
            "attribute_config",
            "automatic_naming",
        ]
        nullable_fields = ["cluster_name", "vector_config", "attribute_config"]
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
