"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from mixpeek.types import BaseModel
from typing_extensions import TypedDict


class TimeseriesDataPointTypedDict(TypedDict):
    r"""Single data point for timeseries data"""

    timestamp: datetime
    r"""Timestamp of the data point"""
    value: float
    r"""Value of the metric"""


class TimeseriesDataPoint(BaseModel):
    r"""Single data point for timeseries data"""

    timestamp: datetime
    r"""Timestamp of the data point"""

    value: float
    r"""Value of the metric"""
