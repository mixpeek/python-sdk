"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .embeddingconfig import EmbeddingConfig, EmbeddingConfigTypedDict
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class TaxonomyNodeTypedDict(TypedDict):
    taxonomy_id: str
    r"""ID of the taxonomy this node belongs to"""
    node_name: str
    r"""Name of the taxonomy node (must be lowercase without spaces)"""
    embedding_configs: List[EmbeddingConfigTypedDict]
    r"""List of embedding configurations defining how this node should be vectorized"""
    node_id: NotRequired[str]
    r"""Unique identifier for the taxonomy node"""
    parent_node_id: NotRequired[Nullable[str]]
    r"""ID of the parent node (None if root node)"""
    node_description: NotRequired[Nullable[str]]
    r"""Optional description of what this node represents"""
    children: NotRequired[Nullable[List[TaxonomyNodeTypedDict]]]
    r"""List of child nodes under this node"""
    path_tokens: NotRequired[List[str]]
    r"""List of node names representing the path from root to this node"""
    order: NotRequired[List[int]]
    r"""Order of the node in the taxonomy"""
    depth: NotRequired[int]
    r"""Depth of the node in the taxonomy"""


class TaxonomyNode(BaseModel):
    taxonomy_id: str
    r"""ID of the taxonomy this node belongs to"""

    node_name: str
    r"""Name of the taxonomy node (must be lowercase without spaces)"""

    embedding_configs: List[EmbeddingConfig]
    r"""List of embedding configurations defining how this node should be vectorized"""

    node_id: Optional[str] = None
    r"""Unique identifier for the taxonomy node"""

    parent_node_id: OptionalNullable[str] = UNSET
    r"""ID of the parent node (None if root node)"""

    node_description: OptionalNullable[str] = UNSET
    r"""Optional description of what this node represents"""

    children: OptionalNullable[List[TaxonomyNode]] = UNSET
    r"""List of child nodes under this node"""

    path_tokens: Optional[List[str]] = None
    r"""List of node names representing the path from root to this node"""

    order: Optional[List[int]] = None
    r"""Order of the node in the taxonomy"""

    depth: Optional[int] = 0
    r"""Depth of the node in the taxonomy"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "node_id",
            "parent_node_id",
            "node_description",
            "children",
            "path_tokens",
            "order",
            "depth",
        ]
        nullable_fields = ["parent_node_id", "node_description", "children"]
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
