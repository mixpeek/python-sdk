"""Clusters resource."""

from __future__ import annotations

from typing import Any, Dict, Optional

from mixpeek.api.clusters_api import ClustersApi
from mixpeek.models.create_cluster_request import CreateClusterRequest
from mixpeek.models.execute_cluster_request import ExecuteClusterRequest
from mixpeek.models.cluster_model import ClusterModel
from mixpeek.models.execute_cluster_response import ExecuteClusterResponse
from mixpeek.models.list_clusters_response import ListClustersResponse
from mixpeek._client.resources.base import BaseResource


class Clusters(BaseResource):
    """
    Clusters resource for data clustering operations.

    Example:
        >>> client.clusters.list()
        >>> client.clusters.create(alias="my_cluster", config={...})
    """

    def __init__(self, api_client, default_namespace=None, default_timeout=None):
        super().__init__(api_client, default_namespace, default_timeout)
        self._api = ClustersApi(api_client)

    def list(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> ListClustersResponse:
        """
        List all clusters.

        Args:
            offset: Number of items to skip for pagination.
            limit: Maximum number of items to return.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            ListClustersResponse with clusters list.

        Example:
            >>> clusters = client.clusters.list()
        """
        from mixpeek.models.list_clusters_request import ListClustersRequest

        request = ListClustersRequest(
            offset=offset,
            limit=limit,
        )
        return self._api.list_clusters(
            list_clusters_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def create(
        self,
        alias: str,
        *,
        description: Optional[str] = None,
        config: Optional[Dict[str, Any]] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> ClusterModel:
        """
        Create a new cluster configuration.

        Args:
            alias: Unique identifier for the cluster.
            description: Human-readable description.
            config: Clustering configuration (algorithm, parameters, etc.).
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.
            **kwargs: Additional cluster options.

        Returns:
            ClusterModel with the created cluster details.

        Example:
            >>> cluster = client.clusters.create(
            ...     alias="user_segments",
            ...     config={"algorithm": "kmeans", "k": 5}
            ... )
        """
        request = CreateClusterRequest(
            alias=alias,
            description=description,
            config=config,
            **kwargs,
        )
        return self._api.create_cluster(
            create_cluster_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def get(
        self,
        cluster: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> ClusterModel:
        """
        Get a cluster by ID or alias.

        Args:
            cluster: Cluster ID or alias.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            ClusterModel with cluster details.

        Example:
            >>> cluster = client.clusters.get("user_segments")
        """
        return self._api.get_cluster(
            cluster_identifier=cluster,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def delete(
        self,
        cluster: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        """
        Delete a cluster.

        Args:
            cluster: Cluster ID or alias.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Example:
            >>> client.clusters.delete("user_segments")
        """
        return self._api.delete_cluster(
            cluster_identifier=cluster,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def execute(
        self,
        cluster: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> ExecuteClusterResponse:
        """
        Execute clustering.

        Args:
            cluster: Cluster ID or alias.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.
            **kwargs: Additional execution options.

        Returns:
            ExecuteClusterResponse with clustering results.

        Example:
            >>> result = client.clusters.execute("user_segments")
        """
        request = ExecuteClusterRequest(**kwargs)
        return self._api.execute_cluster(
            cluster_identifier=cluster,
            execute_cluster_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )
