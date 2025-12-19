"""Retrievers resource."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from mixpeek.api.retrievers_api import RetrieversApi
from mixpeek.models.create_retriever_request import CreateRetrieverRequest
from mixpeek.models.retriever_query_request import RetrieverQueryRequest
from mixpeek.models.retriever_model_output import RetrieverModelOutput
from mixpeek.models.retriever_response import RetrieverResponse
from mixpeek.models.list_retrievers_response import ListRetrieversResponse
from mixpeek._client.resources.base import BaseResource


class Retrievers(BaseResource):
    """
    Retrievers resource for search and retrieval operations.

    Example:
        >>> client.retrievers.list()
        >>> results = client.retrievers.query(retriever="my_retriever", query="search text")
    """

    def __init__(self, api_client, default_namespace=None, default_timeout=None):
        super().__init__(api_client, default_namespace, default_timeout)
        self._api = RetrieversApi(api_client)

    def list(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> ListRetrieversResponse:
        """
        List all retrievers.

        Args:
            offset: Number of items to skip for pagination.
            limit: Maximum number of items to return.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            ListRetrieversResponse with retrievers list.

        Example:
            >>> retrievers = client.retrievers.list()
            >>> for r in retrievers.retrievers:
            ...     print(r.alias)
        """
        from mixpeek.models.list_retrievers_request import ListRetrieversRequest

        request = ListRetrieversRequest(
            offset=offset,
            limit=limit,
        )
        return self._api.list_retrievers(
            list_retrievers_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def create(
        self,
        alias: str,
        *,
        description: Optional[str] = None,
        schema: Optional[Dict[str, Any]] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> RetrieverModelOutput:
        """
        Create a new retriever.

        Args:
            alias: Unique identifier for the retriever.
            description: Human-readable description.
            schema: Retriever schema configuration.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.
            **kwargs: Additional retriever configuration options.

        Returns:
            RetrieverModelOutput with the created retriever details.

        Example:
            >>> retriever = client.retrievers.create(
            ...     alias="product_search",
            ...     description="Search products"
            ... )
        """
        request = CreateRetrieverRequest(
            alias=alias,
            description=description,
            schema=schema,
            **kwargs,
        )
        return self._api.create_retriever(
            create_retriever_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def get(
        self,
        retriever: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> RetrieverModelOutput:
        """
        Get a retriever by ID or alias.

        Args:
            retriever: Retriever ID or alias.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            RetrieverModelOutput with retriever details.

        Example:
            >>> retriever = client.retrievers.get("product_search")
        """
        return self._api.get_retriever(
            retriever_identifier=retriever,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def delete(
        self,
        retriever: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        """
        Delete a retriever.

        Args:
            retriever: Retriever ID or alias.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Example:
            >>> client.retrievers.delete("product_search")
        """
        return self._api.delete_retriever(
            retriever_identifier=retriever,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def query(
        self,
        retriever: str,
        *,
        query: Optional[str] = None,
        queries: Optional[List[Dict[str, Any]]] = None,
        filters: Optional[Dict[str, Any]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        debug: bool = False,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> RetrieverResponse:
        """
        Execute a search query using a retriever.

        Args:
            retriever: Retriever ID or alias.
            query: Search query text (for simple queries).
            queries: List of query configurations (for complex queries).
            filters: Filter conditions.
            limit: Maximum number of results.
            offset: Number of results to skip.
            debug: Whether to include debug information.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.
            **kwargs: Additional query options.

        Returns:
            RetrieverResponse with search results.

        Example:
            >>> results = client.retrievers.query(
            ...     retriever="product_search",
            ...     query="red shoes",
            ...     limit=10
            ... )
            >>> for result in results.results:
            ...     print(result.document_id, result.score)
        """
        request = RetrieverQueryRequest(
            queries=queries,
            filters=filters,
            limit=limit,
            offset=offset,
            **kwargs,
        )
        return self._api.query_retriever(
            retriever_identifier=retriever,
            retriever_query_request=request,
            debug=debug,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )
