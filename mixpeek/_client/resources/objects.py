"""Objects resource."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from mixpeek.api.bucket_objects_api import BucketObjectsApi
from mixpeek.models.create_object_request import CreateObjectRequest
from mixpeek.models.update_object_request import UpdateObjectRequest
from mixpeek.models.object_response import ObjectResponse
from mixpeek.models.list_objects_response import ListObjectsResponse
from mixpeek._client.resources.base import BaseResource


class Objects(BaseResource):
    """
    Objects resource for managing objects within buckets.

    Example:
        >>> client.objects.list(bucket="my_bucket")
        >>> client.objects.create(bucket="my_bucket", key="file.txt", ...)
    """

    def __init__(self, api_client, default_namespace=None, default_timeout=None):
        super().__init__(api_client, default_namespace, default_timeout)
        self._api = BucketObjectsApi(api_client)

    def list(
        self,
        bucket: str,
        *,
        prefix: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> ListObjectsResponse:
        """
        List objects in a bucket.

        Args:
            bucket: Bucket ID or alias.
            prefix: Filter objects by key prefix.
            offset: Number of items to skip for pagination.
            limit: Maximum number of items to return.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            ListObjectsResponse with objects list.

        Example:
            >>> objects = client.objects.list("media_files", prefix="images/")
        """
        return self._api.list_objects(
            bucket_identifier=bucket,
            prefix=prefix,
            offset=offset,
            limit=limit,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def create(
        self,
        bucket: str,
        *,
        key: Optional[str] = None,
        url: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> ObjectResponse:
        """
        Create a new object in a bucket.

        Args:
            bucket: Bucket ID or alias.
            key: Object key/path.
            url: URL to fetch the object content from.
            metadata: Object metadata.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.
            **kwargs: Additional object options.

        Returns:
            ObjectResponse with the created object details.

        Example:
            >>> obj = client.objects.create(
            ...     bucket="media_files",
            ...     url="https://example.com/image.jpg",
            ...     metadata={"type": "image"}
            ... )
        """
        request = CreateObjectRequest(
            key=key,
            url=url,
            metadata=metadata,
            **kwargs,
        )
        return self._api.create_object(
            bucket_identifier=bucket,
            create_object_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def get(
        self,
        bucket: str,
        object_id: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> ObjectResponse:
        """
        Get an object by ID.

        Args:
            bucket: Bucket ID or alias.
            object_id: Object ID.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            ObjectResponse with object details.

        Example:
            >>> obj = client.objects.get("media_files", "obj_123")
        """
        return self._api.get_object(
            bucket_identifier=bucket,
            object_identifier=object_id,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def update(
        self,
        bucket: str,
        object_id: str,
        *,
        metadata: Optional[Dict[str, Any]] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> ObjectResponse:
        """
        Update an object.

        Args:
            bucket: Bucket ID or alias.
            object_id: Object ID.
            metadata: Updated metadata.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.
            **kwargs: Additional options.

        Returns:
            ObjectResponse with updated object details.
        """
        request = UpdateObjectRequest(
            metadata=metadata,
            **kwargs,
        )
        return self._api.update_object(
            bucket_identifier=bucket,
            object_identifier=object_id,
            update_object_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def delete(
        self,
        bucket: str,
        object_id: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        """
        Delete an object.

        Args:
            bucket: Bucket ID or alias.
            object_id: Object ID.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Example:
            >>> client.objects.delete("media_files", "obj_123")
        """
        return self._api.delete_object(
            bucket_identifier=bucket,
            object_identifier=object_id,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )
