"""Taxonomies resource."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from mixpeek.api.taxonomies_api import TaxonomiesApi
from mixpeek.models.create_taxonomy_request import CreateTaxonomyRequest
from mixpeek.models.execute_taxonomy_request import ExecuteTaxonomyRequest
from mixpeek.models.taxonomy_model import TaxonomyModel
from mixpeek.models.taxonomy_response import TaxonomyResponse
from mixpeek.models.list_taxonomies_response import ListTaxonomiesResponse
from mixpeek._client.resources.base import BaseResource


class Taxonomies(BaseResource):
    """
    Taxonomies resource for classification and categorization.

    Example:
        >>> client.taxonomies.list()
        >>> client.taxonomies.create(alias="categories", config={...})
    """

    def __init__(self, api_client, default_namespace=None, default_timeout=None):
        super().__init__(api_client, default_namespace, default_timeout)
        self._api = TaxonomiesApi(api_client)

    def list(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> ListTaxonomiesResponse:
        """
        List all taxonomies.

        Args:
            offset: Number of items to skip for pagination.
            limit: Maximum number of items to return.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            ListTaxonomiesResponse with taxonomies list.

        Example:
            >>> taxonomies = client.taxonomies.list()
        """
        from mixpeek.models.list_taxonomies_request import ListTaxonomiesRequest

        request = ListTaxonomiesRequest(
            offset=offset,
            limit=limit,
        )
        return self._api.list_taxonomies(
            list_taxonomies_request=request,
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
    ) -> TaxonomyModel:
        """
        Create a new taxonomy.

        Args:
            alias: Unique identifier for the taxonomy.
            description: Human-readable description.
            config: Taxonomy configuration.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.
            **kwargs: Additional taxonomy options.

        Returns:
            TaxonomyModel with the created taxonomy details.

        Example:
            >>> taxonomy = client.taxonomies.create(
            ...     alias="product_categories",
            ...     config={"type": "hierarchical", ...}
            ... )
        """
        request = CreateTaxonomyRequest(
            alias=alias,
            description=description,
            config=config,
            **kwargs,
        )
        return self._api.create_taxonomy(
            create_taxonomy_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def get(
        self,
        taxonomy: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> TaxonomyModel:
        """
        Get a taxonomy by ID or alias.

        Args:
            taxonomy: Taxonomy ID or alias.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            TaxonomyModel with taxonomy details.

        Example:
            >>> taxonomy = client.taxonomies.get("product_categories")
        """
        return self._api.get_taxonomy(
            taxonomy_identifier=taxonomy,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def delete(
        self,
        taxonomy: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        """
        Delete a taxonomy.

        Args:
            taxonomy: Taxonomy ID or alias.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Example:
            >>> client.taxonomies.delete("product_categories")
        """
        return self._api.delete_taxonomy(
            taxonomy_identifier=taxonomy,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def execute(
        self,
        taxonomy: str,
        *,
        input_data: Optional[Dict[str, Any]] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> TaxonomyResponse:
        """
        Execute taxonomy classification.

        Args:
            taxonomy: Taxonomy ID or alias.
            input_data: Data to classify.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.
            **kwargs: Additional options.

        Returns:
            TaxonomyResponse with classification results.

        Example:
            >>> result = client.taxonomies.execute(
            ...     taxonomy="product_categories",
            ...     input_data={"text": "red leather shoes"}
            ... )
        """
        request = ExecuteTaxonomyRequest(
            input=input_data,
            **kwargs,
        )
        return self._api.execute_taxonomy(
            taxonomy_identifier=taxonomy,
            execute_taxonomy_request=request,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )
