"""Tasks resource."""

from __future__ import annotations

from typing import Optional

from mixpeek.api.tasks_api import TasksApi
from mixpeek.models.task_response import TaskResponse
from mixpeek.models.list_tasks_response import ListTasksResponse
from mixpeek._client.resources.base import BaseResource


class Tasks(BaseResource):
    """
    Tasks resource for monitoring async operations.

    Example:
        >>> client.tasks.list()
        >>> client.tasks.get("task_123")
    """

    def __init__(self, api_client, default_namespace=None, default_timeout=None):
        super().__init__(api_client, default_namespace, default_timeout)
        self._api = TasksApi(api_client)

    def list(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> ListTasksResponse:
        """
        List all tasks.

        Args:
            offset: Number of items to skip for pagination.
            limit: Maximum number of items to return.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            ListTasksResponse with tasks list.

        Example:
            >>> tasks = client.tasks.list()
            >>> for task in tasks.tasks:
            ...     print(task.task_id, task.status)
        """
        return self._api.list_tasks(
            offset=offset,
            limit=limit,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def get(
        self,
        task_id: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> TaskResponse:
        """
        Get a task by ID.

        Args:
            task_id: Task ID.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Returns:
            TaskResponse with task details.

        Example:
            >>> task = client.tasks.get("task_123")
            >>> print(task.status)
        """
        return self._api.get_task(
            task_id=task_id,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )

    def delete(
        self,
        task_id: str,
        *,
        namespace: Optional[str] = None,
        timeout: Optional[float] = None,
    ):
        """
        Delete/cancel a task.

        Args:
            task_id: Task ID.
            namespace: Optional namespace override.
            timeout: Request timeout in seconds.

        Example:
            >>> client.tasks.delete("task_123")
        """
        return self._api.delete_task(
            task_id=task_id,
            x_namespace=self._get_namespace(namespace),
            _request_timeout=self._get_timeout(timeout),
        )
