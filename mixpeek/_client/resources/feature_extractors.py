"""Feature Extractors resource."""

from __future__ import annotations

from typing import Any, Dict, Optional

from mixpeek.api.feature_extractors_api import FeatureExtractorsApi
from mixpeek.models.feature_extractor_response_model import FeatureExtractorResponseModel
from mixpeek._client.resources.base import BaseResource


class FeatureExtractors(BaseResource):
    """
    Feature Extractors resource for managing embedding and feature extraction models.

    Example:
        >>> client.feature_extractors.list()
        >>> extractor = client.feature_extractors.get("text-embedding")
    """

    def __init__(self, api_client, default_namespace=None, default_timeout=None):
        super().__init__(api_client, default_namespace, default_timeout)
        self._api = FeatureExtractorsApi(api_client)

    def list(
        self,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        """
        List all available feature extractors.

        Args:
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            List of available feature extractors.

        Example:
            >>> extractors = client.feature_extractors.list()
            >>> for e in extractors:
            ...     print(e.alias)
        """
        return self._api.list_feature_extractors(
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def get(
        self,
        extractor: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> FeatureExtractorResponseModel:
        """
        Get a feature extractor by ID or alias.

        Args:
            extractor: Feature extractor ID or alias.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            FeatureExtractorResponseModel with extractor details.

        Example:
            >>> extractor = client.feature_extractors.get("text-embedding")
        """
        return self._api.get_feature_extractor(
            feature_extractor_identifier=extractor,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )
