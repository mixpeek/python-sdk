"""Base resource class with common functionality."""

from __future__ import annotations

from typing import Optional, Tuple, Union

from mixpeek.api_client import ApiClient


class BaseResource:
    """Base class for all resource classes."""

    def __init__(
        self,
        api_client: ApiClient,
        default_namespace: Optional[str] = None,
        default_timeout: Optional[float] = None,
    ) -> None:
        self._api_client = api_client
        self._default_namespace = default_namespace
        self._default_timeout = default_timeout

    def _get_timeout(
        self, timeout: Optional[float] = None
    ) -> Union[None, float, Tuple[float, float]]:
        """Get timeout value, preferring explicit over default."""
        return timeout if timeout is not None else self._default_timeout

    def _get_namespace(self, namespace: Optional[str] = None) -> Optional[str]:
        """Get namespace value, preferring explicit over default."""
        return namespace if namespace is not None else self._default_namespace
