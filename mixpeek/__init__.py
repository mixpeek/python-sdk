"""A client library for accessing Mixpeek API"""

from .client import AuthenticatedClient, Client
from .resources import Collections, Buckets, Retrievers, Namespaces

__all__ = (
    "AuthenticatedClient",
    "Client",
    "Collections",
    "Buckets",
    "Retrievers",
    "Namespaces",
)
