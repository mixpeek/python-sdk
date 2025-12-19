"""
Mixpeek Python SDK - Modern Client Interface

Usage:
    from mixpeek import Mixpeek

    client = Mixpeek(api_key="your_api_key")

    # Collections
    client.collections.list()
    client.collections.create(alias="my_collection", description="...")
    client.collections.get("my_collection")
    client.collections.delete("my_collection")

    # Documents
    client.documents.create(collection="my_collection", metadata={...})
    client.documents.list(collection="my_collection")

    # Retrievers
    client.retrievers.query(retriever="my_retriever", query="search text")
"""

from __future__ import annotations

import os
from typing import Optional

from mixpeek.api_client import ApiClient
from mixpeek.configuration import Configuration
from mixpeek._client.resources import (
    Collections,
    Documents,
    Retrievers,
    Buckets,
    Objects,
    Namespaces,
    Tasks,
    Taxonomies,
    Clusters,
    FeatureExtractors,
)


class Mixpeek:
    """
    Modern interface for the Mixpeek API.

    Example:
        >>> from mixpeek import Mixpeek
        >>> client = Mixpeek(api_key="your_api_key")
        >>> collections = client.collections.list()
        >>> client.collections.create(alias="demo", description="My collection")
    """

    collections: Collections
    documents: Documents
    retrievers: Retrievers
    buckets: Buckets
    objects: Objects
    namespaces: Namespaces
    tasks: Tasks
    taxonomies: Taxonomies
    clusters: Clusters
    feature_extractors: FeatureExtractors

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.mixpeek.com",
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> None:
        """
        Initialize the Mixpeek client.

        Args:
            api_key: Your Mixpeek API key. If not provided, reads from MIXPEEK_API_KEY env var.
            base_url: API base URL. Defaults to https://api.mixpeek.com
            namespace: Default namespace for all requests. Can be overridden per-request.
            timeout: Default request timeout in seconds.

        Example:
            >>> client = Mixpeek(api_key="sk_...")
            >>> # Or use environment variable
            >>> client = Mixpeek()  # reads MIXPEEK_API_KEY
        """
        self._api_key = api_key or os.environ.get("MIXPEEK_API_KEY")
        if not self._api_key:
            raise ValueError(
                "API key is required. Pass api_key parameter or set MIXPEEK_API_KEY environment variable."
            )

        self._base_url = base_url
        self._namespace = namespace
        self._timeout = timeout

        # Configure the underlying API client
        self._configuration = Configuration(
            host=base_url,
            api_key={"ApiKeyAuth": self._api_key}
        )

        self._api_client = ApiClient(self._configuration)

        # Initialize resource accessors
        self.collections = Collections(self._api_client, self._namespace, self._timeout)
        self.documents = Documents(self._api_client, self._namespace, self._timeout)
        self.retrievers = Retrievers(self._api_client, self._namespace, self._timeout)
        self.buckets = Buckets(self._api_client, self._namespace, self._timeout)
        self.objects = Objects(self._api_client, self._namespace, self._timeout)
        self.namespaces = Namespaces(self._api_client, self._namespace, self._timeout)
        self.tasks = Tasks(self._api_client, self._namespace, self._timeout)
        self.taxonomies = Taxonomies(self._api_client, self._namespace, self._timeout)
        self.clusters = Clusters(self._api_client, self._namespace, self._timeout)
        self.feature_extractors = FeatureExtractors(self._api_client, self._namespace, self._timeout)

    def __enter__(self) -> "Mixpeek":
        """Support context manager usage."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Clean up on context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the underlying API client and release resources."""
        if self._api_client:
            self._api_client.close()
