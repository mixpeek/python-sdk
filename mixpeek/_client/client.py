"""High-level Mixpeek client — ergonomic wrapper around the generated SDK."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional

import urllib3


class Mixpeek:
    """One-liner client for the Mixpeek API.

    Usage::

        from mixpeek import Mixpeek

        mp = Mixpeek("sk_xxx", namespace="ns_xxx")
        results = mp.search("red car", collection="products")
    """

    DEFAULT_BASE_URL = "https://api.mixpeek.com/v1"

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        namespace: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self.api_key = api_key or os.environ.get("MIXPEEK_API_KEY", "")
        if not self.api_key:
            raise ValueError(
                "An API key is required. Pass api_key= or set MIXPEEK_API_KEY."
            )
        self.namespace = namespace or os.environ.get("MIXPEEK_NAMESPACE")
        self.base_url = (base_url or self.DEFAULT_BASE_URL).rstrip("/")
        self.timeout = timeout
        self._http = urllib3.PoolManager(
            timeout=urllib3.Timeout(connect=5.0, read=timeout),
            retries=urllib3.Retry(total=2, backoff_factor=0.3),
        )

        # Resource managers (lazy-style but immediate for discoverability)
        from mixpeek._client.resources import (
            Buckets,
            Collections,
            Documents,
            Namespaces,
            Retrievers,
        )

        self.namespaces = Namespaces(self)
        self.buckets = Buckets(self)
        self.collections = Collections(self)
        self.retrievers = Retrievers(self)
        self.documents = Documents(self)

    # ---- Convenience shortcuts ------------------------------------------------

    def search(
        self,
        query: str,
        *,
        collection: Optional[str] = None,
        filters: Optional[Dict[str, Any]] = None,
        limit: int = 10,
        namespace: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Zero-setup semantic search using an adhoc retriever.

        Constructs a ``feature_search`` stage on the fly and executes it
        via ``POST /v1/retrievers/execute`` (adhoc mode).
        """
        ns = namespace or self.namespace
        stages: List[Dict[str, Any]] = [
            {
                "type": "feature_search",
                "feature_extractor": {"type": "text"},
                "query": query,
                "collection_ids": [collection] if collection else [],
                "limit": limit,
            }
        ]
        if filters:
            stages.insert(
                0,
                {
                    "type": "attribute_filter",
                    "conditions": filters,
                },
            )
        body: Dict[str, Any] = {
            "stages": stages,
            "inputs": {"query": query},
        }
        return self._request(
            "POST", "/retrievers/execute", body=body, namespace=ns
        )

    def index(
        self,
        source: str,
        *,
        collection: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        namespace: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Upload a file URL to a bucket and optionally trigger a collection.

        ``source`` can be an S3/GCS URI or any public URL.
        If ``collection`` is provided the collection is triggered after upload.
        """
        ns = namespace or self.namespace

        # Find or pick the first bucket in the namespace
        buckets = self._request("POST", "/buckets/list", namespace=ns)
        if not buckets:
            raise ValueError("No buckets found in the target namespace.")
        bucket_id = buckets[0]["bucket_id"] if isinstance(buckets, list) else buckets["results"][0]["bucket_id"]

        upload_body: Dict[str, Any] = {"blob": {"url": source}}
        if metadata:
            upload_body["metadata"] = metadata

        result = self._request(
            "POST", f"/buckets/{bucket_id}/objects", body=upload_body, namespace=ns
        )

        if collection:
            self._request(
                "POST", f"/collections/{collection}/trigger", namespace=ns
            )

        return result

    # ---- HTTP helper ----------------------------------------------------------

    def _request(
        self,
        method: str,
        path: str,
        *,
        body: Optional[Any] = None,
        namespace: Optional[str] = None,
    ) -> Any:
        url = f"{self.base_url}{path}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        ns = namespace or self.namespace
        if ns:
            headers["X-Namespace"] = ns

        encoded_body = json.dumps(body).encode("utf-8") if body is not None else None

        resp = self._http.request(
            method,
            url,
            body=encoded_body,
            headers=headers,
        )

        if resp.status >= 400:
            try:
                detail = json.loads(resp.data.decode("utf-8"))
            except Exception:
                detail = resp.data.decode("utf-8", errors="replace")
            raise MixpeekAPIError(resp.status, detail)

        if not resp.data:
            return None

        return json.loads(resp.data.decode("utf-8"))


class MixpeekAPIError(Exception):
    """Raised when the Mixpeek API returns an error response."""

    def __init__(self, status: int, detail: Any) -> None:
        self.status = status
        self.detail = detail
        super().__init__(f"Mixpeek API error {status}: {detail}")
