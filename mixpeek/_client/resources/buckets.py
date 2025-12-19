"""Buckets resource."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from mixpeek.api.buckets_api import BucketsApi
from mixpeek.models.bucket_create_request import BucketCreateRequest
from mixpeek.models.bucket_update_request import BucketUpdateRequest
from mixpeek.models.bucket_response import BucketResponse
from mixpeek.models.list_buckets_response import ListBucketsResponse
from mixpeek._client.resources.base import BaseResource


class Buckets(BaseResource):
    """
    Buckets resource for managing storage buckets.

    Example:
        >>> client.buckets.list()
        >>> client.buckets.create(alias="my_bucket")
        >>> client.buckets.get("my_bucket")
    """

    def __init__(self, api_client, default_namespace=None, default_timeout=None):
        super().__init__(api_client, default_namespace, default_timeout)
        self._api = BucketsApi(api_client)

    def list(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> ListBucketsResponse:
        """
        List all buckets.

        Args:
            offset: Number of items to skip for pagination.
            limit: Maximum number of items to return.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            ListBucketsResponse with buckets list.

        Example:
            >>> buckets = client.buckets.list()
            >>> for bucket in buckets.buckets:
            ...     print(bucket.alias)
        """
        from mixpeek.models.list_buckets_request import ListBucketsRequest

        request = ListBucketsRequest(
            offset=offset,
            limit=limit,
        )
        return self._api.list_buckets(
            list_buckets_request=request,
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
    ) -> BucketResponse:
        """
        Create a new bucket.

        Args:
            alias: Unique identifier for the bucket.
            description: Human-readable description.
            schema: Bucket schema configuration.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.
            **kwargs: Additional bucket configuration options.

        Returns:
            BucketResponse with the created bucket details.

        Example:
            >>> bucket = client.buckets.create(
            ...     alias="media_files",
            ...     description="Media storage bucket"
            ... )
        """
        request = BucketCreateRequest(
            alias=alias,
            description=description,
            schema=schema,
            **kwargs,
        )
        return self._api.create_bucket(
            bucket_create_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def get(
        self,
        bucket: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> BucketResponse:
        """
        Get a bucket by ID or alias.

        Args:
            bucket: Bucket ID or alias.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            BucketResponse with bucket details.

        Example:
            >>> bucket = client.buckets.get("media_files")
        """
        return self._api.get_bucket(
            bucket_identifier=bucket,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def update(
        self,
        bucket: str,
        *,
        description: Optional[str] = None,
        schema: Optional[Dict[str, Any]] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> BucketResponse:
        """
        Update a bucket.

        Args:
            bucket: Bucket ID or alias.
            description: Updated description.
            schema: Updated schema configuration.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.
            **kwargs: Additional options.

        Returns:
            BucketResponse with updated bucket details.
        """
        request = BucketUpdateRequest(
            description=description,
            schema=schema,
            **kwargs,
        )
        return self._api.update_bucket(
            bucket_identifier=bucket,
            bucket_update_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def delete(
        self,
        bucket: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        """
        Delete a bucket.

        Args:
            bucket: Bucket ID or alias.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Example:
            >>> client.buckets.delete("media_files")
        """
        return self._api.delete_bucket(
            bucket_identifier=bucket,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )
