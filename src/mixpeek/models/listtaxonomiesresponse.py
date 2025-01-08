"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .db_model_paginationresponse import (
    DbModelPaginationResponse,
    DbModelPaginationResponseTypedDict,
)
from .taxonomymodel import TaxonomyModel, TaxonomyModelTypedDict
from mixpeek.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ListTaxonomiesResponseTypedDict(TypedDict):
    results: List[TaxonomyModelTypedDict]
    r"""List of fully populated taxonomies with nodes"""
    pagination: DbModelPaginationResponseTypedDict


class ListTaxonomiesResponse(BaseModel):
    results: List[TaxonomyModel]
    r"""List of fully populated taxonomies with nodes"""

    pagination: DbModelPaginationResponse
