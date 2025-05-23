"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mixpeek.types import BaseModel
from typing_extensions import TypedDict


class ResourceTotalsTypedDict(TypedDict):
    r"""Resource totals for the organization"""

    storage_gb: float
    r"""Total storage in GB"""
    api_calls_per_month: int
    r"""Total API calls per month"""
    documents: int
    r"""Total number of documents"""
    collections: int
    r"""Total number of collections"""
    namespaces: int
    r"""Total number of namespaces"""


class ResourceTotals(BaseModel):
    r"""Resource totals for the organization"""

    storage_gb: float
    r"""Total storage in GB"""

    api_calls_per_month: int
    r"""Total API calls per month"""

    documents: int
    r"""Total number of documents"""

    collections: int
    r"""Total number of collections"""

    namespaces: int
    r"""Total number of namespaces"""
