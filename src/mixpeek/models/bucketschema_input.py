"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bucketschemafield_input import (
    BucketSchemaFieldInput,
    BucketSchemaFieldInputTypedDict,
)
from mixpeek.types import BaseModel
import pydantic
from pydantic import ConfigDict
from typing import Any, Dict
from typing_extensions import TypedDict


class BucketSchemaInputTypedDict(TypedDict):
    r"""Schema definition for bucket objects"""

    properties: Dict[str, BucketSchemaFieldInputTypedDict]


class BucketSchemaInput(BaseModel):
    r"""Schema definition for bucket objects"""

    model_config = ConfigDict(
        populate_by_name=True, arbitrary_types_allowed=True, extra="allow"
    )
    __pydantic_extra__: Dict[str, Any] = pydantic.Field(init=False)

    properties: Dict[str, BucketSchemaFieldInput]

    @property
    def additional_properties(self):
        return self.__pydantic_extra__

    @additional_properties.setter
    def additional_properties(self, value):
        self.__pydantic_extra__ = value  # pyright: ignore[reportIncompatibleVariableOverride]
