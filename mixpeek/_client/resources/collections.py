"""Collections resource."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from mixpeek.api.collections_api import CollectionsApi
from mixpeek.models.create_collection_request import CreateCollectionRequest
from mixpeek.models.collection_response import CollectionResponse
from mixpeek.models.list_collections_response import ListCollectionsResponse
from mixpeek.models.describe_collection_features_response import DescribeCollectionFeaturesResponse
from mixpeek._client.resources.base import BaseResource


class Collections(BaseResource):
    """
    Collections resource for managing document collections.

    Example:
        >>> client.collections.list()
        >>> client.collections.create(alias="my_collection", description="My data")
        >>> client.collections.get("my_collection")
        >>> client.collections.delete("my_collection")
    """

    def __init__(self, api_client, default_namespace=None, default_timeout=None):
        super().__init__(api_client, default_namespace, default_timeout)
        self._api = CollectionsApi(api_client)

    def list(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> ListCollectionsResponse:
        """
        List all collections.

        Args:
            offset: Number of items to skip for pagination.
            limit: Maximum number of items to return.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            ListCollectionsResponse with collections list and pagination info.

        Example:
            >>> collections = client.collections.list()
            >>> for collection in collections.collections:
            ...     print(collection.alias)
        """
        from mixpeek.models.list_collections_request import ListCollectionsRequest

        request = ListCollectionsRequest(
            offset=offset,
            limit=limit,
        )
        return self._api.list_collections(
            list_collections_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def create(
        self,
        alias: str,
        *,
        description: Optional[str] = None,
        payload_index: Optional[Dict[str, Any]] = None,
        vector_index: Optional[Dict[str, Any]] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> CollectionResponse:
        """
        Create a new collection.

        Args:
            alias: Unique identifier for the collection.
            description: Human-readable description.
            payload_index: Payload index configuration.
            vector_index: Vector index configuration.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            CollectionResponse with the created collection details.

        Example:
            >>> collection = client.collections.create(
            ...     alias="products",
            ...     description="Product catalog"
            ... )
        """
        request = CreateCollectionRequest(
            alias=alias,
            description=description,
            payload_index=payload_index,
            vector_index=vector_index,
        )
        return self._api.create_collection(
            create_collection_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def get(
        self,
        collection: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> CollectionResponse:
        """
        Get a collection by ID or alias.

        Args:
            collection: Collection ID or alias.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            CollectionResponse with collection details.

        Example:
            >>> collection = client.collections.get("products")
        """
        return self._api.get_collection(
            collection_identifier=collection,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def delete(
        self,
        collection: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        """
        Delete a collection.

        Args:
            collection: Collection ID or alias.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Example:
            >>> client.collections.delete("products")
        """
        return self._api.delete_collection(
            collection_identifier=collection,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def describe_features(
        self,
        collection: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> DescribeCollectionFeaturesResponse:
        """
        Get feature descriptors for a collection.

        Args:
            collection: Collection ID or alias.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            DescribeCollectionFeaturesResponse with feature information.
        """
        return self._api.describe_collection_features(
            collection_identifier=collection,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )
