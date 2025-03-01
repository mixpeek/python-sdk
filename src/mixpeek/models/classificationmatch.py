"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .taxonomynode import TaxonomyNode, TaxonomyNodeTypedDict
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List
from typing_extensions import NotRequired, TypedDict


class ClassificationMatchTypedDict(TypedDict):
    r"""Individual node match with score"""

    taxonomy_id: str
    r"""ID of the matched taxonomy"""
    node_id: str
    r"""ID of the matched taxonomy node"""
    score: float
    r"""Confidence score of the match"""
    depth: int
    r"""Depth of the node in the taxonomy"""
    order: List[int]
    r"""Order of the node in the taxonomy"""
    node: NotRequired[Nullable[TaxonomyNodeTypedDict]]
    r"""Full node object if requested"""


class ClassificationMatch(BaseModel):
    r"""Individual node match with score"""

    taxonomy_id: str
    r"""ID of the matched taxonomy"""

    node_id: str
    r"""ID of the matched taxonomy node"""

    score: float
    r"""Confidence score of the match"""

    depth: int
    r"""Depth of the node in the taxonomy"""

    order: List[int]
    r"""Order of the node in the taxonomy"""

    node: OptionalNullable[TaxonomyNode] = UNSET
    r"""Full node object if requested"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["node"]
        nullable_fields = ["node"]
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
