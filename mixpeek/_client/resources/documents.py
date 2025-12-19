"""Documents resource."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from mixpeek.api.collection_documents_api import CollectionDocumentsApi
from mixpeek.models.document_create_request import DocumentCreateRequest
from mixpeek.models.document_update_request import DocumentUpdateRequest
from mixpeek.models.document_response import DocumentResponse
from mixpeek.models.list_documents_response import ListDocumentsResponse
from mixpeek._client.resources.base import BaseResource


class Documents(BaseResource):
    """
    Documents resource for managing documents within collections.

    Example:
        >>> client.documents.list(collection="my_collection")
        >>> client.documents.create(collection="my_collection", metadata={...})
        >>> client.documents.get(collection="my_collection", document_id="doc_123")
    """

    def __init__(self, api_client, default_namespace=None, default_timeout=None):
        super().__init__(api_client, default_namespace, default_timeout)
        self._api = CollectionDocumentsApi(api_client)

    def list(
        self,
        collection: str,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        filters: Optional[Dict[str, Any]] = None,
        sort: Optional[Dict[str, Any]] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> ListDocumentsResponse:
        """
        List documents in a collection.

        Args:
            collection: Collection ID or alias.
            offset: Number of items to skip for pagination.
            limit: Maximum number of items to return.
            filters: Filter conditions.
            sort: Sort options.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            ListDocumentsResponse with documents list and pagination info.

        Example:
            >>> docs = client.documents.list("products", limit=100)
            >>> for doc in docs.documents:
            ...     print(doc.document_id)
        """
        from mixpeek.models.list_documents_request import ListDocumentsRequest

        request = ListDocumentsRequest(
            offset=offset,
            limit=limit,
            filters=filters,
            sort=sort,
        )
        return self._api.list_documents(
            collection_identifier=collection,
            list_documents_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def create(
        self,
        collection: str,
        *,
        metadata: Dict[str, Any],
        document_id: Optional[str] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> DocumentResponse:
        """
        Create a new document in a collection.

        Args:
            collection: Collection ID or alias.
            metadata: Document metadata/payload.
            document_id: Optional custom document ID.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            DocumentResponse with the created document details.

        Example:
            >>> doc = client.documents.create(
            ...     collection="products",
            ...     metadata={"name": "Widget", "price": 9.99}
            ... )
        """
        request = DocumentCreateRequest(
            metadata=metadata,
            document_id=document_id,
        )
        return self._api.create_document(
            collection_identifier=collection,
            document_create_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def get(
        self,
        collection: str,
        document_id: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> DocumentResponse:
        """
        Get a document by ID.

        Args:
            collection: Collection ID or alias.
            document_id: Document ID.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            DocumentResponse with document details.

        Example:
            >>> doc = client.documents.get("products", "doc_123")
        """
        return self._api.get_document(
            collection_identifier=collection,
            document_identifier=document_id,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def update(
        self,
        collection: str,
        document_id: str,
        *,
        metadata: Dict[str, Any],
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> DocumentResponse:
        """
        Update a document.

        Args:
            collection: Collection ID or alias.
            document_id: Document ID.
            metadata: Updated metadata.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            DocumentResponse with updated document details.

        Example:
            >>> doc = client.documents.update(
            ...     collection="products",
            ...     document_id="doc_123",
            ...     metadata={"price": 12.99}
            ... )
        """
        request = DocumentUpdateRequest(metadata=metadata)
        return self._api.update_document(
            collection_identifier=collection,
            document_identifier=document_id,
            document_update_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def delete(
        self,
        collection: str,
        document_id: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        """
        Delete a document.

        Args:
            collection: Collection ID or alias.
            document_id: Document ID.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Example:
            >>> client.documents.delete("products", "doc_123")
        """
        return self._api.delete_document(
            collection_identifier=collection,
            document_identifier=document_id,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )
