"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .filtercondition import FilterCondition, FilterConditionTypedDict
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class LogicalOperatorTypedDict(TypedDict):
    case_sensitive: NotRequired[Nullable[bool]]
    r"""Whether to perform case-sensitive matching"""
    and_: NotRequired[Nullable[List[AndTypedDict]]]
    r"""Logical AND operation"""
    or_: NotRequired[Nullable[List[OrTypedDict]]]
    r"""Logical OR operation"""
    nor: NotRequired[Nullable[List[NorTypedDict]]]
    r"""Logical NOR operation"""


class LogicalOperator(BaseModel):
    case_sensitive: OptionalNullable[bool] = UNSET
    r"""Whether to perform case-sensitive matching"""

    and_: Annotated[OptionalNullable[List[And]], pydantic.Field(alias="AND")] = UNSET
    r"""Logical AND operation"""

    or_: Annotated[OptionalNullable[List[Or]], pydantic.Field(alias="OR")] = UNSET
    r"""Logical OR operation"""

    nor: Annotated[OptionalNullable[List[Nor]], pydantic.Field(alias="NOR")] = UNSET
    r"""Logical NOR operation"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["case_sensitive", "AND", "OR", "NOR"]
        nullable_fields = ["case_sensitive", "AND", "OR", "NOR"]
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


AndTypedDict = TypeAliasType(
    "AndTypedDict", Union[FilterConditionTypedDict, "LogicalOperatorTypedDict"]
)


And = TypeAliasType("And", Union[FilterCondition, "LogicalOperator"])


OrTypedDict = TypeAliasType(
    "OrTypedDict", Union[FilterConditionTypedDict, "LogicalOperatorTypedDict"]
)


Or = TypeAliasType("Or", Union[FilterCondition, "LogicalOperator"])


NorTypedDict = TypeAliasType(
    "NorTypedDict", Union[FilterConditionTypedDict, "LogicalOperatorTypedDict"]
)


Nor = TypeAliasType("Nor", Union[FilterCondition, "LogicalOperator"])
