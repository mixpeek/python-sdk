"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from mixpeek import models, utils
from mixpeek._hooks import HookContext
from mixpeek.types import OptionalNullable, UNSET
from mixpeek.utils import get_security_from_env
from typing import Any, List, Mapping, Optional, Union


class Ingest(BaseSDK):
    def text(
        self,
        *,
        collection: str,
        x_namespace: OptionalNullable[str] = UNSET,
        asset_update: OptionalNullable[
            Union[models.AssetUpdate, models.AssetUpdateTypedDict]
        ] = UNSET,
        metadata: Optional[
            Union[
                models.ProcessTextInputMetadata,
                models.ProcessTextInputMetadataTypedDict,
            ]
        ] = None,
        feature_extractors: OptionalNullable[
            Union[models.TextSettings, models.TextSettingsTypedDict]
        ] = UNSET,
        skip_duplicate: OptionalNullable[bool] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TaskResponse:
        r"""Ingest Text

        :param collection: Unique identifier for the collection where the processed asset will be stored, can be the collection name or collection ID. If neither exist, the collection will be created.
        :param x_namespace: Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint.
        :param asset_update: Controls how processing results are stored - either creating a new asset or updating an existing one.
        :param metadata: Additional metadata associated with the file. Can include any key-value pairs relevant to the file.
        :param feature_extractors: Settings for text processing.
        :param skip_duplicate: Skips processing when a duplicate hash is found and stores an error by the task_id with the existing asset_id
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

        request = models.IngestTextIngestTextPostRequest(
            x_namespace=x_namespace,
            process_text_input=models.ProcessTextInput(
                collection=collection,
                asset_update=utils.get_pydantic_model(
                    asset_update, OptionalNullable[models.AssetUpdate]
                ),
                metadata=utils.get_pydantic_model(
                    metadata, Optional[models.ProcessTextInputMetadata]
                ),
                feature_extractors=utils.get_pydantic_model(
                    feature_extractors, OptionalNullable[models.TextSettings]
                ),
                skip_duplicate=skip_duplicate,
            ),
        )

        req = self._build_request(
            method="POST",
            path="/ingest/text",
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
                request.process_text_input,
                False,
                False,
                "json",
                models.ProcessTextInput,
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
                operation_id="ingest_text_ingest_text_post",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "422", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.TaskResponse)
        if utils.match_response(
            http_res, ["400", "401", "403", "404", "500"], "application/json"
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseData)
            raise models.ErrorResponse(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
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

    async def text_async(
        self,
        *,
        collection: str,
        x_namespace: OptionalNullable[str] = UNSET,
        asset_update: OptionalNullable[
            Union[models.AssetUpdate, models.AssetUpdateTypedDict]
        ] = UNSET,
        metadata: Optional[
            Union[
                models.ProcessTextInputMetadata,
                models.ProcessTextInputMetadataTypedDict,
            ]
        ] = None,
        feature_extractors: OptionalNullable[
            Union[models.TextSettings, models.TextSettingsTypedDict]
        ] = UNSET,
        skip_duplicate: OptionalNullable[bool] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TaskResponse:
        r"""Ingest Text

        :param collection: Unique identifier for the collection where the processed asset will be stored, can be the collection name or collection ID. If neither exist, the collection will be created.
        :param x_namespace: Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint.
        :param asset_update: Controls how processing results are stored - either creating a new asset or updating an existing one.
        :param metadata: Additional metadata associated with the file. Can include any key-value pairs relevant to the file.
        :param feature_extractors: Settings for text processing.
        :param skip_duplicate: Skips processing when a duplicate hash is found and stores an error by the task_id with the existing asset_id
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

        request = models.IngestTextIngestTextPostRequest(
            x_namespace=x_namespace,
            process_text_input=models.ProcessTextInput(
                collection=collection,
                asset_update=utils.get_pydantic_model(
                    asset_update, OptionalNullable[models.AssetUpdate]
                ),
                metadata=utils.get_pydantic_model(
                    metadata, Optional[models.ProcessTextInputMetadata]
                ),
                feature_extractors=utils.get_pydantic_model(
                    feature_extractors, OptionalNullable[models.TextSettings]
                ),
                skip_duplicate=skip_duplicate,
            ),
        )

        req = self._build_request_async(
            method="POST",
            path="/ingest/text",
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
                request.process_text_input,
                False,
                False,
                "json",
                models.ProcessTextInput,
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
                operation_id="ingest_text_ingest_text_post",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "422", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.TaskResponse)
        if utils.match_response(
            http_res, ["400", "401", "403", "404", "500"], "application/json"
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseData)
            raise models.ErrorResponse(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
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

    def video_from_url(
        self,
        *,
        url: str,
        collection: str,
        x_namespace: OptionalNullable[str] = UNSET,
        asset_update: OptionalNullable[
            Union[models.AssetUpdate, models.AssetUpdateTypedDict]
        ] = UNSET,
        metadata: Optional[
            Union[
                models.ProcessVideoURLInputMetadata,
                models.ProcessVideoURLInputMetadataTypedDict,
            ]
        ] = None,
        skip_duplicate: OptionalNullable[bool] = UNSET,
        feature_extractors: OptionalNullable[
            Union[List[models.VideoSettings], List[models.VideoSettingsTypedDict]]
        ] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TaskResponse:
        r"""Ingest Video Url

        :param url: The URL of the asset to be processed. Must be a valid HTTP or HTTPS URL.
        :param collection: Unique identifier for the collection where the processed asset will be stored, can be the collection name or collection ID. If neither exist, the collection will be created.
        :param x_namespace: Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint.
        :param asset_update: Controls how processing results are stored - either creating a new asset or updating an existing one.
        :param metadata: Additional metadata associated with the asset. Can include any key-value pairs relevant to the asset.
        :param skip_duplicate: Makes feature extraction idempotent. When True and a duplicate file hash is found, copies features from the existing asset instead of reprocessing. This allows the same file to be used multiple times with different metadata while avoiding redundant processing.
        :param feature_extractors: Settings for video processing. Only applicable if the URL points to a video file.
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

        request = models.IngestVideoURLIngestVideosURLPostRequest(
            x_namespace=x_namespace,
            process_video_url_input=models.ProcessVideoURLInput(
                url=url,
                collection=collection,
                asset_update=utils.get_pydantic_model(
                    asset_update, OptionalNullable[models.AssetUpdate]
                ),
                metadata=utils.get_pydantic_model(
                    metadata, Optional[models.ProcessVideoURLInputMetadata]
                ),
                skip_duplicate=skip_duplicate,
                feature_extractors=utils.get_pydantic_model(
                    feature_extractors, OptionalNullable[List[models.VideoSettings]]
                ),
            ),
        )

        req = self._build_request(
            method="POST",
            path="/ingest/videos/url",
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
                request.process_video_url_input,
                False,
                False,
                "json",
                models.ProcessVideoURLInput,
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
                operation_id="ingest_video_url_ingest_videos_url_post",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "422", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.TaskResponse)
        if utils.match_response(
            http_res, ["400", "401", "403", "404", "500"], "application/json"
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseData)
            raise models.ErrorResponse(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
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

    async def video_from_url_async(
        self,
        *,
        url: str,
        collection: str,
        x_namespace: OptionalNullable[str] = UNSET,
        asset_update: OptionalNullable[
            Union[models.AssetUpdate, models.AssetUpdateTypedDict]
        ] = UNSET,
        metadata: Optional[
            Union[
                models.ProcessVideoURLInputMetadata,
                models.ProcessVideoURLInputMetadataTypedDict,
            ]
        ] = None,
        skip_duplicate: OptionalNullable[bool] = UNSET,
        feature_extractors: OptionalNullable[
            Union[List[models.VideoSettings], List[models.VideoSettingsTypedDict]]
        ] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TaskResponse:
        r"""Ingest Video Url

        :param url: The URL of the asset to be processed. Must be a valid HTTP or HTTPS URL.
        :param collection: Unique identifier for the collection where the processed asset will be stored, can be the collection name or collection ID. If neither exist, the collection will be created.
        :param x_namespace: Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint.
        :param asset_update: Controls how processing results are stored - either creating a new asset or updating an existing one.
        :param metadata: Additional metadata associated with the asset. Can include any key-value pairs relevant to the asset.
        :param skip_duplicate: Makes feature extraction idempotent. When True and a duplicate file hash is found, copies features from the existing asset instead of reprocessing. This allows the same file to be used multiple times with different metadata while avoiding redundant processing.
        :param feature_extractors: Settings for video processing. Only applicable if the URL points to a video file.
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

        request = models.IngestVideoURLIngestVideosURLPostRequest(
            x_namespace=x_namespace,
            process_video_url_input=models.ProcessVideoURLInput(
                url=url,
                collection=collection,
                asset_update=utils.get_pydantic_model(
                    asset_update, OptionalNullable[models.AssetUpdate]
                ),
                metadata=utils.get_pydantic_model(
                    metadata, Optional[models.ProcessVideoURLInputMetadata]
                ),
                skip_duplicate=skip_duplicate,
                feature_extractors=utils.get_pydantic_model(
                    feature_extractors, OptionalNullable[List[models.VideoSettings]]
                ),
            ),
        )

        req = self._build_request_async(
            method="POST",
            path="/ingest/videos/url",
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
                request.process_video_url_input,
                False,
                False,
                "json",
                models.ProcessVideoURLInput,
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
                operation_id="ingest_video_url_ingest_videos_url_post",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "422", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.TaskResponse)
        if utils.match_response(
            http_res, ["400", "401", "403", "404", "500"], "application/json"
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseData)
            raise models.ErrorResponse(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
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

    def image_url(
        self,
        *,
        url: str,
        collection: str,
        x_namespace: OptionalNullable[str] = UNSET,
        asset_update: OptionalNullable[
            Union[models.AssetUpdate, models.AssetUpdateTypedDict]
        ] = UNSET,
        metadata: Optional[
            Union[
                models.ProcessImageURLInputMetadata,
                models.ProcessImageURLInputMetadataTypedDict,
            ]
        ] = None,
        skip_duplicate: OptionalNullable[bool] = UNSET,
        feature_extractors: OptionalNullable[
            Union[models.ImageSettings, models.ImageSettingsTypedDict]
        ] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TaskResponse:
        r"""Ingest Image Url

        :param url: The URL of the asset to be processed. Must be a valid HTTP or HTTPS URL.
        :param collection: Unique identifier for the collection where the processed asset will be stored, can be the collection name or collection ID. If neither exist, the collection will be created.
        :param x_namespace: Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint.
        :param asset_update: Controls how processing results are stored - either creating a new asset or updating an existing one.
        :param metadata: Additional metadata associated with the asset. Can include any key-value pairs relevant to the asset.
        :param skip_duplicate: Makes feature extraction idempotent. When True and a duplicate file hash is found, copies features from the existing asset instead of reprocessing. This allows the same file to be used multiple times with different metadata while avoiding redundant processing.
        :param feature_extractors: Settings for image processing. Only applicable if the URL points to an image file.
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

        request = models.IngestImageURLIngestImagesURLPostRequest(
            x_namespace=x_namespace,
            process_image_url_input=models.ProcessImageURLInput(
                url=url,
                collection=collection,
                asset_update=utils.get_pydantic_model(
                    asset_update, OptionalNullable[models.AssetUpdate]
                ),
                metadata=utils.get_pydantic_model(
                    metadata, Optional[models.ProcessImageURLInputMetadata]
                ),
                skip_duplicate=skip_duplicate,
                feature_extractors=utils.get_pydantic_model(
                    feature_extractors, OptionalNullable[models.ImageSettings]
                ),
            ),
        )

        req = self._build_request(
            method="POST",
            path="/ingest/images/url",
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
                request.process_image_url_input,
                False,
                False,
                "json",
                models.ProcessImageURLInput,
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
                operation_id="ingest_image_url_ingest_images_url_post",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "422", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.TaskResponse)
        if utils.match_response(
            http_res, ["400", "401", "403", "404", "500"], "application/json"
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseData)
            raise models.ErrorResponse(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
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

    async def image_url_async(
        self,
        *,
        url: str,
        collection: str,
        x_namespace: OptionalNullable[str] = UNSET,
        asset_update: OptionalNullable[
            Union[models.AssetUpdate, models.AssetUpdateTypedDict]
        ] = UNSET,
        metadata: Optional[
            Union[
                models.ProcessImageURLInputMetadata,
                models.ProcessImageURLInputMetadataTypedDict,
            ]
        ] = None,
        skip_duplicate: OptionalNullable[bool] = UNSET,
        feature_extractors: OptionalNullable[
            Union[models.ImageSettings, models.ImageSettingsTypedDict]
        ] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TaskResponse:
        r"""Ingest Image Url

        :param url: The URL of the asset to be processed. Must be a valid HTTP or HTTPS URL.
        :param collection: Unique identifier for the collection where the processed asset will be stored, can be the collection name or collection ID. If neither exist, the collection will be created.
        :param x_namespace: Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint.
        :param asset_update: Controls how processing results are stored - either creating a new asset or updating an existing one.
        :param metadata: Additional metadata associated with the asset. Can include any key-value pairs relevant to the asset.
        :param skip_duplicate: Makes feature extraction idempotent. When True and a duplicate file hash is found, copies features from the existing asset instead of reprocessing. This allows the same file to be used multiple times with different metadata while avoiding redundant processing.
        :param feature_extractors: Settings for image processing. Only applicable if the URL points to an image file.
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

        request = models.IngestImageURLIngestImagesURLPostRequest(
            x_namespace=x_namespace,
            process_image_url_input=models.ProcessImageURLInput(
                url=url,
                collection=collection,
                asset_update=utils.get_pydantic_model(
                    asset_update, OptionalNullable[models.AssetUpdate]
                ),
                metadata=utils.get_pydantic_model(
                    metadata, Optional[models.ProcessImageURLInputMetadata]
                ),
                skip_duplicate=skip_duplicate,
                feature_extractors=utils.get_pydantic_model(
                    feature_extractors, OptionalNullable[models.ImageSettings]
                ),
            ),
        )

        req = self._build_request_async(
            method="POST",
            path="/ingest/images/url",
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
                request.process_image_url_input,
                False,
                False,
                "json",
                models.ProcessImageURLInput,
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
                operation_id="ingest_image_url_ingest_images_url_post",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "422", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.TaskResponse)
        if utils.match_response(
            http_res, ["400", "401", "403", "404", "500"], "application/json"
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseData)
            raise models.ErrorResponse(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
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
