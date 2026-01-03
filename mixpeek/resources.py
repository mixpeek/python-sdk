"""
Simplified resource interfaces for common Mixpeek operations.

This module provides a cleaner, more intuitive API on top of the auto-generated SDK.
"""

from typing import Optional, Any
from .client import AuthenticatedClient, Client


class Collections:
    """Collections resource with simplified methods."""

    def __init__(self, client: AuthenticatedClient | Client):
        self.client = client

    def list(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        cursor: Optional[str] = None,
    ) -> Any:
        """List all collections.

        Args:
            limit: Maximum number of results to return
            offset: Number of results to skip
            cursor: Pagination cursor

        Returns:
            Response object with collections data
        """
        from .api.collections.list_collections_v1_collections_list_post import sync_detailed
        return sync_detailed(
            client=self.client,
            limit=limit,
            offset=offset,
            cursor=cursor,
        )

    def get(self, collection_id: str) -> Any:
        """Get a specific collection.

        Args:
            collection_id: The collection identifier

        Returns:
            Response object with collection data
        """
        from .api.collections.get_collection_v1_collections_collection_identifier_get import sync_detailed
        return sync_detailed(
            collection_identifier=collection_id,
            client=self.client,
        )


class Buckets:
    """Buckets resource with simplified methods."""

    def __init__(self, client: AuthenticatedClient | Client):
        self.client = client

    def list(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Any:
        """List all buckets.

        Args:
            limit: Maximum number of results to return
            offset: Number of results to skip

        Returns:
            Response object with buckets data
        """
        from .api.buckets.list_buckets_v1_buckets_list_post import sync_detailed
        return sync_detailed(
            client=self.client,
            limit=limit,
            offset=offset,
        )

    def get(self, bucket_id: str) -> Any:
        """Get a specific bucket.

        Args:
            bucket_id: The bucket identifier

        Returns:
            Response object with bucket data
        """
        from .api.buckets.get_bucket_v1_buckets_bucket_identifier_get import sync_detailed
        return sync_detailed(
            bucket_identifier=bucket_id,
            client=self.client,
        )


class Retrievers:
    """Retrievers resource with simplified methods."""

    def __init__(self, client: AuthenticatedClient | Client):
        self.client = client

    def list(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Any:
        """List all retrievers.

        Args:
            limit: Maximum number of results to return
            offset: Number of results to skip

        Returns:
            Response object with retrievers data
        """
        from .api.retrievers.list_retrievers_v1_retrievers_list_post import sync_detailed
        return sync_detailed(
            client=self.client,
            limit=limit,
            offset=offset,
        )

    def get(self, retriever_id: str) -> Any:
        """Get a specific retriever.

        Args:
            retriever_id: The retriever identifier

        Returns:
            Response object with retriever data
        """
        from .api.retrievers.get_retriever_v1_retrievers_retriever_id_get import sync_detailed
        return sync_detailed(
            retriever_id=retriever_id,
            client=self.client,
        )


class Namespaces:
    """Namespaces resource with simplified methods."""

    def __init__(self, client: AuthenticatedClient | Client):
        self.client = client

    def list(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Any:
        """List all namespaces.

        Args:
            limit: Maximum number of results to return
            offset: Number of results to skip

        Returns:
            Response object with namespaces data
        """
        from .api.namespaces.list_namespaces_v1_namespaces_list_post import sync_detailed
        return sync_detailed(
            client=self.client,
            limit=limit,
            offset=offset,
        )

    def get(self, namespace_id: str) -> Any:
        """Get a specific namespace.

        Args:
            namespace_id: The namespace identifier

        Returns:
            Response object with namespace data
        """
        from .api.namespaces.get_namespace_v1_namespaces_namespace_identifier_get import sync_detailed
        return sync_detailed(
            namespace_identifier=namespace_id,
            client=self.client,
        )
