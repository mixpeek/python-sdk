"""Resource managers for the high-level Mixpeek client."""

from __future__ import annotations

import json
from typing import Any, Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from mixpeek._client.client import Mixpeek


class _Resource:
    """Base resource with access to the parent client's HTTP helper."""

    def __init__(self, client: Mixpeek) -> None:
        self._client = client
        self._request = client._request


class Namespaces(_Resource):
    """Manage namespaces (Qdrant collections)."""

    def list(self) -> List[Dict[str, Any]]:
        return self._request("GET", "/namespaces")

    def get(self, namespace_id: str) -> Dict[str, Any]:
        return self._request("GET", f"/namespaces/{namespace_id}")

    def create(
        self,
        *,
        name: str,
        feature_extractors: Optional[List[Dict[str, Any]]] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        body: Dict[str, Any] = {"name": name, **kwargs}
        if feature_extractors is not None:
            body["feature_extractors"] = feature_extractors
        return self._request("POST", "/namespaces", body=body)

    def delete(self, namespace_id: str) -> Dict[str, Any]:
        return self._request("DELETE", f"/namespaces/{namespace_id}")


class Buckets(_Resource):
    """Manage buckets and object uploads."""

    def list(self) -> List[Dict[str, Any]]:
        return self._request("POST", "/buckets/list")

    def get(self, bucket_id: str) -> Dict[str, Any]:
        return self._request("GET", f"/buckets/{bucket_id}")

    def create(self, *, name: str, **kwargs: Any) -> Dict[str, Any]:
        return self._request("POST", "/buckets", body={"name": name, **kwargs})

    def delete(self, bucket_id: str) -> Dict[str, Any]:
        return self._request("DELETE", f"/buckets/{bucket_id}")

    def upload(
        self,
        bucket_id: str,
        *,
        url: Optional[str] = None,
        data: Optional[Any] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        body: Dict[str, Any] = {**kwargs}
        if url is not None:
            body["blob"] = {"url": url}
        elif data is not None:
            body["blob"] = {"data": data}
        if metadata is not None:
            body["metadata"] = metadata
        return self._request(
            "POST", f"/buckets/{bucket_id}/objects", body=body
        )

    def list_objects(
        self,
        bucket_id: str,
        *,
        cursor: Optional[str] = None,
        page_size: int = 100,
    ) -> Dict[str, Any]:
        body: Dict[str, Any] = {"page_size": page_size}
        if cursor is not None:
            body["cursor"] = cursor
        return self._request(
            "POST", f"/buckets/{bucket_id}/objects/list", body=body
        )


class Collections(_Resource):
    """Manage collections (processing pipelines)."""

    def list(self) -> List[Dict[str, Any]]:
        return self._request("POST", "/collections/list")

    def get(self, collection_id: str) -> Dict[str, Any]:
        return self._request("GET", f"/collections/{collection_id}")

    def create(
        self,
        *,
        name: str,
        feature_extractor: Optional[Dict[str, Any]] = None,
        source: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        body: Dict[str, Any] = {"name": name, **kwargs}
        if feature_extractor is not None:
            body["feature_extractor"] = feature_extractor
        if source is not None:
            body["source"] = source
        return self._request("POST", "/collections", body=body)

    def delete(self, collection_id: str) -> Dict[str, Any]:
        return self._request("DELETE", f"/collections/{collection_id}")

    def trigger(self, collection_id: str, **kwargs: Any) -> Dict[str, Any]:
        return self._request(
            "POST", f"/collections/{collection_id}/trigger", body=kwargs or None
        )


class Retrievers(_Resource):
    """Manage and execute retrievers."""

    def list(self) -> List[Dict[str, Any]]:
        return self._request("POST", "/retrievers/list")

    def get(self, retriever_id: str) -> Dict[str, Any]:
        return self._request("GET", f"/retrievers/{retriever_id}")

    def create(
        self,
        *,
        name: str,
        stages: List[Dict[str, Any]],
        **kwargs: Any,
    ) -> Dict[str, Any]:
        return self._request(
            "POST", "/retrievers", body={"name": name, "stages": stages, **kwargs}
        )

    def delete(self, retriever_id: str) -> Dict[str, Any]:
        return self._request("DELETE", f"/retrievers/{retriever_id}")

    def execute(
        self,
        retriever_id: str,
        *,
        inputs: Dict[str, Any],
        settings: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        body: Dict[str, Any] = {"inputs": inputs, **kwargs}
        if settings is not None:
            body["settings"] = settings
        return self._request(
            "POST", f"/retrievers/{retriever_id}/execute", body=body
        )


class Documents(_Resource):
    """Query and manage documents."""

    def list(
        self,
        collection_id: str,
        *,
        cursor: Optional[str] = None,
        page_size: int = 100,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        body: Dict[str, Any] = {"page_size": page_size, **kwargs}
        if cursor is not None:
            body["cursor"] = cursor
        return self._request(
            "POST", f"/collections/{collection_id}/documents/list", body=body
        )

    def get(self, collection_id: str, document_id: str) -> Dict[str, Any]:
        return self._request(
            "GET", f"/collections/{collection_id}/documents/{document_id}"
        )

    def delete(self, collection_id: str, document_id: str) -> Dict[str, Any]:
        return self._request(
            "DELETE", f"/collections/{collection_id}/documents/{document_id}"
        )

    def update(
        self,
        collection_id: str,
        document_id: str,
        *,
        update_data: Dict[str, Any],
    ) -> Dict[str, Any]:
        return self._request(
            "PATCH",
            f"/collections/{collection_id}/documents/{document_id}",
            body=update_data,
        )

    def batch_update(
        self,
        collection_id: str,
        *,
        updates: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        return self._request(
            "POST",
            f"/collections/{collection_id}/documents/batch",
            body={"updates": updates},
        )

    def search(
        self,
        *,
        collection_ids: Optional[List[str]] = None,
        query: Optional[str] = None,
        page_size: int = 10,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        body: Dict[str, Any] = {"page_size": page_size, **kwargs}
        if collection_ids is not None:
            body["collection_ids"] = collection_ids
        if query is not None:
            body["query"] = query
        return self._request("POST", "/documents/search", body=body)
