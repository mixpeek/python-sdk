"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mixpeek.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class UUIDIndexParamsTypedDict(TypedDict):
    r"""Configuration for UUID index"""

    type: NotRequired[str]
    is_tenant: NotRequired[bool]


class UUIDIndexParams(BaseModel):
    r"""Configuration for UUID index"""

    type: Optional[str] = "uuid"

    is_tenant: Optional[bool] = False
