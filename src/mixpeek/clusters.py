"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from mixpeek import models, utils
from mixpeek._hooks import HookContext
from mixpeek.types import OptionalNullable, UNSET
from mixpeek.utils import get_security_from_env
from typing import Any, Mapping, Optional, Union


class Clusters(BaseSDK):
    def create_cluster_v1_clusters_post(
        self,
        *,
        collection_id: str,
        x_namespace: OptionalNullable[str] = UNSET,
        cluster_name: OptionalNullable[str] = UNSET,
        cluster_type: Optional[models.ClusterType] = None,
        vector_config: OptionalNullable[
            Union[models.VectorBasedConfig, models.VectorBasedConfigTypedDict]
        ] = UNSET,
        attribute_config: OptionalNullable[
            Union[models.AttributeBasedConfig, models.AttributeBasedConfigTypedDict]
        ] = UNSET,
        automatic_naming: Optional[
            Union[models.AutomaticNaming, models.AutomaticNamingTypedDict]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TaskResponse:
        r"""Create Cluster

        :param collection_id: ID of the collection to cluster
        :param x_namespace: Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint.
        :param cluster_name: Name for the cluster (auto-generated if empty)
        :param cluster_type:
        :param vector_config:
        :param attribute_config:
        :param automatic_naming:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.CreateClusterV1ClustersPostRequest(
            x_namespace=x_namespace,
            create_cluster_request=models.CreateClusterRequest(
                cluster_name=cluster_name,
                collection_id=collection_id,
                cluster_type=cluster_type,
                vector_config=utils.get_pydantic_model(
                    vector_config, OptionalNullable[models.VectorBasedConfig]
                ),
                attribute_config=utils.get_pydantic_model(
                    attribute_config, OptionalNullable[models.AttributeBasedConfig]
                ),
                automatic_naming=utils.get_pydantic_model(
                    automatic_naming, Optional[models.AutomaticNaming]
                ),
            ),
        )

        req = self._build_request(
            method="POST",
            path="/v1/clusters",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.create_cluster_request,
                False,
                False,
                "json",
                models.CreateClusterRequest,
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="create_cluster_v1_clusters_post",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "422", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.TaskResponse)
        if utils.match_response(
            http_res, ["400", "401", "403", "404"], "application/json"
        ):
            response_data = utils.unmarshal_json(
                http_res.text, models.ErrorResponseData
            )
            raise models.ErrorResponse(data=response_data)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.HTTPValidationErrorData
            )
            raise models.HTTPValidationError(data=response_data)
        if utils.match_response(http_res, "500", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.ErrorResponseData
            )
            raise models.ErrorResponse(data=response_data)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def create_cluster_v1_clusters_post_async(
        self,
        *,
        collection_id: str,
        x_namespace: OptionalNullable[str] = UNSET,
        cluster_name: OptionalNullable[str] = UNSET,
        cluster_type: Optional[models.ClusterType] = None,
        vector_config: OptionalNullable[
            Union[models.VectorBasedConfig, models.VectorBasedConfigTypedDict]
        ] = UNSET,
        attribute_config: OptionalNullable[
            Union[models.AttributeBasedConfig, models.AttributeBasedConfigTypedDict]
        ] = UNSET,
        automatic_naming: Optional[
            Union[models.AutomaticNaming, models.AutomaticNamingTypedDict]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TaskResponse:
        r"""Create Cluster

        :param collection_id: ID of the collection to cluster
        :param x_namespace: Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint.
        :param cluster_name: Name for the cluster (auto-generated if empty)
        :param cluster_type:
        :param vector_config:
        :param attribute_config:
        :param automatic_naming:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.CreateClusterV1ClustersPostRequest(
            x_namespace=x_namespace,
            create_cluster_request=models.CreateClusterRequest(
                cluster_name=cluster_name,
                collection_id=collection_id,
                cluster_type=cluster_type,
                vector_config=utils.get_pydantic_model(
                    vector_config, OptionalNullable[models.VectorBasedConfig]
                ),
                attribute_config=utils.get_pydantic_model(
                    attribute_config, OptionalNullable[models.AttributeBasedConfig]
                ),
                automatic_naming=utils.get_pydantic_model(
                    automatic_naming, Optional[models.AutomaticNaming]
                ),
            ),
        )

        req = self._build_request_async(
            method="POST",
            path="/v1/clusters",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.create_cluster_request,
                False,
                False,
                "json",
                models.CreateClusterRequest,
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="create_cluster_v1_clusters_post",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "422", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.TaskResponse)
        if utils.match_response(
            http_res, ["400", "401", "403", "404"], "application/json"
        ):
            response_data = utils.unmarshal_json(
                http_res.text, models.ErrorResponseData
            )
            raise models.ErrorResponse(data=response_data)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.HTTPValidationErrorData
            )
            raise models.HTTPValidationError(data=response_data)
        if utils.match_response(http_res, "500", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.ErrorResponseData
            )
            raise models.ErrorResponse(data=response_data)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
