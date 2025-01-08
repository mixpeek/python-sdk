"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mixpeek.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class FeatureOptionsTypedDict(TypedDict):
    r"""Controls what feature data to include in classification responses"""

    return_payload: NotRequired[bool]
    r"""Whether to include the full feature payload in the response"""
    return_url: NotRequired[bool]
    r"""Whether to include feature URLs in the response"""


class FeatureOptions(BaseModel):
    r"""Controls what feature data to include in classification responses"""

    return_payload: Optional[bool] = False
    r"""Whether to include the full feature payload in the response"""

    return_url: Optional[bool] = False
    r"""Whether to include feature URLs in the response"""
