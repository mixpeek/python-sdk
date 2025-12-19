"""Namespaces resource."""

from __future__ import annotations

from typing import Any, Dict, Optional

from mixpeek.api.namespaces_api import NamespacesApi
from mixpeek.models.create_namespace_request import CreateNamespaceRequest
from mixpeek.models.update_namespace_request import UpdateNamespaceRequest
from mixpeek.models.namespace_model import NamespaceModel
from mixpeek.models.list_namespaces_response import ListNamespacesResponse
from mixpeek._client.resources.base import BaseResource


class Namespaces(BaseResource):
    """
    Namespaces resource for managing data isolation namespaces.

    Example:
        >>> client.namespaces.list()
        >>> client.namespaces.create(alias="production")
    """

    def __init__(self, api_client, default_namespace=None, default_timeout=None):
        super().__init__(api_client, default_namespace, default_timeout)
        self._api = NamespacesApi(api_client)

    def list(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[float] = None,
    ) -> ListNamespacesResponse:
        """
        List all namespaces.

        Args:
            offset: Number of items to skip for pagination.
            limit: Maximum number of items to return.
            timeout: Request timeout in seconds.

        Returns:
            ListNamespacesResponse with namespaces list.

        Example:
            >>> namespaces = client.namespaces.list()
            >>> for ns in namespaces.namespaces:
            ...     print(ns.alias)
        """
        from mixpeek.models.list_namespaces_request import ListNamespacesRequest

        request = ListNamespacesRequest(
            offset=offset,
            limit=limit,
        )
        return self._api.list_namespaces(
            list_namespaces_request=request,
            _request_timeout=self._get_timeout(timeout),
        )

    def create(
        self,
        alias: str,
        *,
        description: Optional[str] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> NamespaceModel:
        """
        Create a new namespace.

        Args:
            alias: Unique identifier for the namespace.
            description: Human-readable description.
            timeout: Request timeout in seconds.
            **kwargs: Additional namespace options.

        Returns:
            NamespaceModel with the created namespace details.

        Example:
            >>> ns = client.namespaces.create(
            ...     alias="production",
            ...     description="Production environment"
            ... )
        """
        request = CreateNamespaceRequest(
            alias=alias,
            description=description,
            **kwargs,
        )
        return self._api.create_namespace(
            create_namespace_request=request,
            _request_timeout=self._get_timeout(timeout),
        )

    def get(
        self,
        namespace_id: str,
        *,
        timeout: Optional[float] = None,
    ) -> NamespaceModel:
        """
        Get a namespace by ID.

        Args:
            namespace_id: Namespace ID.
            timeout: Request timeout in seconds.

        Returns:
            NamespaceModel with namespace details.

        Example:
            >>> ns = client.namespaces.get("ns_123")
        """
        return self._api.get_namespace(
            namespace_id=namespace_id,
            _request_timeout=self._get_timeout(timeout),
        )

    def update(
        self,
        namespace_id: str,
        *,
        alias: Optional[str] = None,
        description: Optional[str] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> NamespaceModel:
        """
        Update a namespace.

        Args:
            namespace_id: Namespace ID.
            alias: Updated alias.
            description: Updated description.
            timeout: Request timeout in seconds.
            **kwargs: Additional options.

        Returns:
            NamespaceModel with updated namespace details.
        """
        request = UpdateNamespaceRequest(
            alias=alias,
            description=description,
            **kwargs,
        )
        return self._api.update_namespace(
            namespace_id=namespace_id,
            update_namespace_request=request,
            _request_timeout=self._get_timeout(timeout),
        )

    def delete(
        self,
        namespace_id: str,
        *,
        timeout: Optional[float] = None,
    ):
        """
        Delete a namespace.

        Args:
            namespace_id: Namespace ID.
            timeout: Request timeout in seconds.

        Example:
            >>> client.namespaces.delete("ns_123")
        """
        return self._api.delete_namespace(
            namespace_id=namespace_id,
            _request_timeout=self._get_timeout(timeout),
        )
