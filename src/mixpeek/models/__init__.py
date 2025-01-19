"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .actionusage import ActionUsage, ActionUsageTypedDict
from .apierror import APIError
from .apikey import APIKey, APIKeyTypedDict
from .apikeyupdate import APIKeyUpdate, APIKeyUpdateTypedDict
from .assetfeatures import AssetFeatures, AssetFeaturesTypedDict
from .assetresponse import (
    AssetResponse,
    AssetResponseTypedDict,
    FileData,
    FileDataTypedDict,
    Metadata,
    MetadataTypedDict,
)
from .assets_model_searchquery import (
    AssetsModelSearchQuery,
    AssetsModelSearchQueryTypedDict,
)
from .assetupdate import AssetUpdate, AssetUpdateTypedDict, Mode
from .assignmentconfig import AssignmentConfig, AssignmentConfigTypedDict
from .assignmentmode import AssignmentMode
from .availablemodels import AvailableModels
from .availablemodelsresponse import (
    AvailableModelsResponse,
    AvailableModelsResponseTypedDict,
)
from .boolindexparams import BoolIndexParams, BoolIndexParamsTypedDict
from .classificationmatch import ClassificationMatch, ClassificationMatchTypedDict
from .classificationwithfeature import (
    ClassificationWithFeature,
    ClassificationWithFeatureTypedDict,
)
from .classify_features_v1_entities_taxonomies_taxonomy_classify_postop import (
    ClassifyFeaturesV1EntitiesTaxonomiesTaxonomyClassifyPostRequest,
    ClassifyFeaturesV1EntitiesTaxonomiesTaxonomyClassifyPostRequestTypedDict,
)
from .collectionmodel import (
    CollectionModel,
    CollectionModelMetadata,
    CollectionModelMetadataTypedDict,
    CollectionModelTypedDict,
)
from .collectionresult import (
    CollectionResult,
    CollectionResultMetadata,
    CollectionResultMetadataTypedDict,
    CollectionResultTypedDict,
)
from .create_api_key_v1_organizations_users_user_email_api_keys_postop import (
    CreateAPIKeyV1OrganizationsUsersUserEmailAPIKeysPostRequest,
    CreateAPIKeyV1OrganizationsUsersUserEmailAPIKeysPostRequestTypedDict,
)
from .create_collection_v1_collections_postop import (
    CreateCollectionV1CollectionsPostRequest,
    CreateCollectionV1CollectionsPostRequestTypedDict,
)
from .create_taxonomy_v1_entities_taxonomies_postop import (
    CreateTaxonomyV1EntitiesTaxonomiesPostRequest,
    CreateTaxonomyV1EntitiesTaxonomiesPostRequestTypedDict,
)
from .createcollectionrequest import (
    CreateCollectionRequest,
    CreateCollectionRequestMetadata,
    CreateCollectionRequestMetadataTypedDict,
    CreateCollectionRequestTypedDict,
)
from .createnamespacerequest import (
    CreateNamespaceRequest,
    CreateNamespaceRequestTypedDict,
)
from .datetimeindexparams import DatetimeIndexParams, DatetimeIndexParamsTypedDict
from .dateusage import DateUsage, DateUsageTypedDict
from .db_model_paginationresponse import (
    DbModelPaginationResponse,
    DbModelPaginationResponseTypedDict,
)
from .delete_api_key_v1_organizations_users_user_email_api_keys_key_name_deleteop import (
    DeleteAPIKeyV1OrganizationsUsersUserEmailAPIKeysKeyNameDeleteRequest,
    DeleteAPIKeyV1OrganizationsUsersUserEmailAPIKeysKeyNameDeleteRequestTypedDict,
)
from .delete_asset_v1_assets_asset_id_deleteop import (
    DeleteAssetV1AssetsAssetIDDeleteRequest,
    DeleteAssetV1AssetsAssetIDDeleteRequestTypedDict,
)
from .delete_classifications_v1_entities_taxonomies_taxonomy_classifications_classification_id_deleteop import (
    DeleteClassificationsV1EntitiesTaxonomiesTaxonomyClassificationsClassificationIDDeleteRequest,
    DeleteClassificationsV1EntitiesTaxonomiesTaxonomyClassificationsClassificationIDDeleteRequestTypedDict,
)
from .delete_collection_v1_collections_collection_deleteop import (
    DeleteCollectionV1CollectionsCollectionDeleteRequest,
    DeleteCollectionV1CollectionsCollectionDeleteRequestTypedDict,
)
from .delete_feature_v1_features_feature_id_deleteop import (
    DeleteFeatureV1FeaturesFeatureIDDeleteRequest,
    DeleteFeatureV1FeaturesFeatureIDDeleteRequestTypedDict,
)
from .delete_namespace_v1_namespaces_namespace_deleteop import (
    DeleteNamespaceV1NamespacesNamespaceDeleteRequest,
    DeleteNamespaceV1NamespacesNamespaceDeleteRequestTypedDict,
)
from .delete_taxonomy_v1_entities_taxonomies_taxonomy_deleteop import (
    DeleteTaxonomyV1EntitiesTaxonomiesTaxonomyDeleteRequest,
    DeleteTaxonomyV1EntitiesTaxonomiesTaxonomyDeleteRequestTypedDict,
)
from .delete_user_v1_organizations_users_user_email_deleteop import (
    DeleteUserV1OrganizationsUsersUserEmailDeleteRequest,
    DeleteUserV1OrganizationsUsersUserEmailDeleteRequestTypedDict,
)
from .denseembedding import DenseEmbedding, DenseEmbeddingTypedDict
from .discoverrequest import DiscoverRequest, DiscoverRequestTypedDict
from .embeddingconfig import (
    EmbeddingConfig,
    EmbeddingConfigType,
    EmbeddingConfigTypedDict,
)
from .embeddingrequest import EmbeddingRequest, EmbeddingRequestTypedDict
from .embeddingresponse import (
    Embedding,
    EmbeddingResponse,
    EmbeddingResponseTypedDict,
    EmbeddingTypedDict,
)
from .entitysettings import EntitySettings, EntitySettingsTypedDict
from .errordetail import Details, DetailsTypedDict, ErrorDetail, ErrorDetailTypedDict
from .errorresponse import ErrorResponse, ErrorResponseData
from .featureextractionembeddingrequest import (
    FeatureExtractionEmbeddingRequest,
    FeatureExtractionEmbeddingRequestTypedDict,
)
from .featureoptions import FeatureOptions, FeatureOptionsTypedDict
from .featureresponse import FeatureResponse, FeatureResponseTypedDict
from .features_model_paginationresponse import (
    FeaturesModelPaginationResponse,
    FeaturesModelPaginationResponseTypedDict,
)
from .featureupdaterequest import (
    FeatureUpdateRequest,
    FeatureUpdateRequestMetadata,
    FeatureUpdateRequestMetadataTypedDict,
    FeatureUpdateRequestTypedDict,
)
from .filtercondition import FilterCondition, FilterConditionTypedDict, Operator
from .floatindexparams import FloatIndexParams, FloatIndexParamsTypedDict
from .full_asset_update_v1_assets_asset_id_putop import (
    FullAssetUpdateV1AssetsAssetIDPutRequest,
    FullAssetUpdateV1AssetsAssetIDPutRequestTypedDict,
)
from .full_feature_update_v1_features_feature_id_putop import (
    FullFeatureUpdateV1FeaturesFeatureIDPutRequest,
    FullFeatureUpdateV1FeaturesFeatureIDPutRequestTypedDict,
)
from .genericsuccessresponse import (
    GenericSuccessResponse,
    GenericSuccessResponseTypedDict,
)
from .geoindexparams import GeoIndexParams, GeoIndexParamsTypedDict
from .get_asset_v1_assets_asset_id_getop import (
    GetAssetV1AssetsAssetIDGetRequest,
    GetAssetV1AssetsAssetIDGetRequestTypedDict,
)
from .get_asset_with_features_v1_assets_asset_id_features_getop import (
    GetAssetWithFeaturesV1AssetsAssetIDFeaturesGetRequest,
    GetAssetWithFeaturesV1AssetsAssetIDFeaturesGetRequestTypedDict,
)
from .get_collection_v1_collections_collection_getop import (
    GetCollectionV1CollectionsCollectionGetRequest,
    GetCollectionV1CollectionsCollectionGetRequestTypedDict,
)
from .get_feature_v1_features_feature_id_getop import (
    GetFeatureV1FeaturesFeatureIDGetRequest,
    GetFeatureV1FeaturesFeatureIDGetRequestTypedDict,
)
from .get_namespace_v1_namespaces_namespace_getop import (
    GetNamespaceV1NamespacesNamespaceGetRequest,
    GetNamespaceV1NamespacesNamespaceGetRequestTypedDict,
)
from .get_task_v1_tasks_task_id_getop import (
    GetTaskV1TasksTaskIDGetRequest,
    GetTaskV1TasksTaskIDGetRequestTypedDict,
)
from .get_taxonomy_node_v1_entities_taxonomies_nodes_node_getop import (
    GetTaxonomyNodeV1EntitiesTaxonomiesNodesNodeGetRequest,
    GetTaxonomyNodeV1EntitiesTaxonomiesNodesNodeGetRequestTypedDict,
)
from .get_taxonomy_v1_entities_taxonomies_taxonomy_getop import (
    GetTaxonomyV1EntitiesTaxonomiesTaxonomyGetRequest,
    GetTaxonomyV1EntitiesTaxonomiesTaxonomyGetRequestTypedDict,
)
from .get_user_v1_organizations_users_user_email_getop import (
    GetUserV1OrganizationsUsersUserEmailGetRequest,
    GetUserV1OrganizationsUsersUserEmailGetRequestTypedDict,
)
from .groupbyoptions import GroupByOptions, GroupByOptionsTypedDict
from .groupbyoptionsasset import GroupByOptionsAsset, GroupByOptionsAssetTypedDict
from .groupedassetdata import GroupedAssetData, GroupedAssetDataTypedDict
from .healthcheckresponse import HealthCheckResponse, HealthCheckResponseTypedDict
from .httpvalidationerror import HTTPValidationError, HTTPValidationErrorData
from .imagedescribesettings import (
    ImageDescribeSettings,
    ImageDescribeSettingsJSONOutput,
    ImageDescribeSettingsJSONOutputTypedDict,
    ImageDescribeSettingsTypedDict,
)
from .imagedetectsettings import ImageDetectSettings, ImageDetectSettingsTypedDict
from .imagereadsettings import (
    ImageReadSettings,
    ImageReadSettingsJSONOutput,
    ImageReadSettingsJSONOutputTypedDict,
    ImageReadSettingsTypedDict,
)
from .imagesettings import ImageSettings, ImageSettingsTypedDict
from .ingest_image_url_v1_ingest_images_url_postop import (
    IngestImageURLV1IngestImagesURLPostRequest,
    IngestImageURLV1IngestImagesURLPostRequestTypedDict,
)
from .ingest_text_v1_ingest_text_postop import (
    IngestTextV1IngestTextPostRequest,
    IngestTextV1IngestTextPostRequestTypedDict,
)
from .ingest_video_url_v1_ingest_videos_url_postop import (
    IngestVideoURLV1IngestVideosURLPostRequest,
    IngestVideoURLV1IngestVideosURLPostRequestTypedDict,
)
from .inputtype import InputType
from .integerindexparams import IntegerIndexParams, IntegerIndexParamsTypedDict
from .jsonimageoutputsettings import (
    JSONImageOutputSettings,
    JSONImageOutputSettingsResponseShape,
    JSONImageOutputSettingsResponseShapeTypedDict,
    JSONImageOutputSettingsTypedDict,
)
from .jsontextoutputsettings import (
    JSONTextOutputSettings,
    JSONTextOutputSettingsTypedDict,
    ResponseShape,
    ResponseShapeTypedDict,
)
from .jsonvideooutputsettings import (
    JSONVideoOutputSettings,
    JSONVideoOutputSettingsResponseShape,
    JSONVideoOutputSettingsResponseShapeTypedDict,
    JSONVideoOutputSettingsTypedDict,
)
from .keywordindexparams import KeywordIndexParams, KeywordIndexParamsTypedDict
from .kill_task_v1_tasks_task_id_deleteop import (
    KillTaskV1TasksTaskIDDeleteRequest,
    KillTaskV1TasksTaskIDDeleteRequestTypedDict,
)
from .list_active_tasks_v1_tasks_getop import (
    ListActiveTasksV1TasksGetRequest,
    ListActiveTasksV1TasksGetRequestTypedDict,
)
from .list_assets_v1_assets_postop import (
    ListAssetsV1AssetsPostRequest,
    ListAssetsV1AssetsPostRequestTypedDict,
)
from .list_classifications_v1_entities_taxonomies_taxonomy_classifications_postop import (
    ListClassificationsV1EntitiesTaxonomiesTaxonomyClassificationsPostRequest,
    ListClassificationsV1EntitiesTaxonomiesTaxonomyClassificationsPostRequestTypedDict,
)
from .list_collections_v1_collections_getop import (
    ListCollectionsV1CollectionsGetRequest,
    ListCollectionsV1CollectionsGetRequestTypedDict,
)
from .list_features_v1_features_postop import (
    ListFeaturesV1FeaturesPostRequest,
    ListFeaturesV1FeaturesPostRequestTypedDict,
)
from .list_taxonomies_v1_entities_taxonomies_getop import (
    ListTaxonomiesV1EntitiesTaxonomiesGetRequest,
    ListTaxonomiesV1EntitiesTaxonomiesGetRequestTypedDict,
)
from .listassetsrequest import ListAssetsRequest, ListAssetsRequestTypedDict
from .listassetsresponse import ListAssetsResponse, ListAssetsResponseTypedDict
from .listclassificationsrequest import (
    ListClassificationsRequest,
    ListClassificationsRequestTypedDict,
)
from .listclassificationsresponse import (
    ListClassificationsResponse,
    ListClassificationsResponseTypedDict,
)
from .listcollectionsresponse import (
    ListCollectionsResponse,
    ListCollectionsResponseTypedDict,
)
from .listfeaturesrequest import ListFeaturesRequest, ListFeaturesRequestTypedDict
from .listfeaturesresponse import ListFeaturesResponse, ListFeaturesResponseTypedDict
from .listtasksresponse import ListTasksResponse, ListTasksResponseTypedDict
from .listtaxonomiesresponse import (
    ListTaxonomiesResponse,
    ListTaxonomiesResponseTypedDict,
)
from .logicaloperator import (
    And,
    AndTypedDict,
    LogicalOperator,
    LogicalOperatorTypedDict,
    Nor,
    NorTypedDict,
    Or,
    OrTypedDict,
)
from .logodetectsettings import LogoDetectSettings, LogoDetectSettingsTypedDict
from .modality import Modality
from .modeldetails import ModelDetails, ModelDetailsTypedDict
from .namespaceresponse import NamespaceResponse, NamespaceResponseTypedDict
from .nodeoptions import NodeOptions, NodeOptionsTypedDict
from .nodeupdate import NodeUpdate, NodeUpdateTypedDict
from .organizationmodel import (
    OrganizationModel,
    OrganizationModelMetadata,
    OrganizationModelMetadataTypedDict,
    OrganizationModelTypedDict,
)
from .partial_asset_update_v1_assets_asset_id_patchop import (
    PartialAssetUpdateV1AssetsAssetIDPatchRequest,
    PartialAssetUpdateV1AssetsAssetIDPatchRequestTypedDict,
)
from .payloadindexconfig import (
    FieldSchema,
    FieldSchemaTypedDict,
    PayloadIndexConfig,
    PayloadIndexConfigTypedDict,
)
from .payloadindextype import PayloadIndexType, PayloadIndexTypeTypedDict
from .payloadschematype import PayloadSchemaType
from .permission import Permission
from .processimageurlinput import (
    ProcessImageURLInput,
    ProcessImageURLInputMetadata,
    ProcessImageURLInputMetadataTypedDict,
    ProcessImageURLInputTypedDict,
)
from .processtextinput import (
    ProcessTextInput,
    ProcessTextInputMetadata,
    ProcessTextInputMetadataTypedDict,
    ProcessTextInputTypedDict,
)
from .processvideourlinput import (
    ProcessVideoURLInput,
    ProcessVideoURLInputMetadata,
    ProcessVideoURLInputMetadataTypedDict,
    ProcessVideoURLInputTypedDict,
)
from .querysettings import QuerySettings, QuerySettingsTypedDict
from .rerankingoptions import RerankingOptions, RerankingOptionsTypedDict
from .search_assets_v1_assets_search_postop import (
    SearchAssetsV1AssetsSearchPostRequest,
    SearchAssetsV1AssetsSearchPostRequestTypedDict,
)
from .search_features_v1_features_search_postop import (
    SearchFeaturesV1FeaturesSearchPostRequest,
    SearchFeaturesV1FeaturesSearchPostRequestTypedDict,
    SearchFeaturesV1FeaturesSearchPostResponseSearchFeaturesV1FeaturesSearchPost,
    SearchFeaturesV1FeaturesSearchPostResponseSearchFeaturesV1FeaturesSearchPostTypedDict,
)
from .search_model_searchquery import (
    SearchModelSearchQuery,
    SearchModelSearchQueryTypedDict,
    Type,
)
from .searchassetsrequest import SearchAssetsRequest, SearchAssetsRequestTypedDict
from .searchrequestfeatures import SearchRequestFeatures, SearchRequestFeaturesTypedDict
from .security import Security, SecurityTypedDict
from .sortoption import Direction, SortOption, SortOptionTypedDict
from .sparseembedding import SparseEmbedding, SparseEmbeddingTypedDict
from .taskresponse import TaskResponse, TaskResponseTypedDict
from .taskstatus import TaskStatus
from .taxonomycreate import TaxonomyCreate, TaxonomyCreateTypedDict
from .taxonomyextractionconfig import (
    TaxonomyExtractionConfig,
    TaxonomyExtractionConfigTypedDict,
)
from .taxonomymodel import TaxonomyModel, TaxonomyModelTypedDict
from .taxonomynode import TaxonomyNode, TaxonomyNodeTypedDict
from .taxonomynodecreate import TaxonomyNodeCreate, TaxonomyNodeCreateTypedDict
from .taxonomyupdate import TaxonomyUpdate, TaxonomyUpdateTypedDict
from .textindexparams import TextIndexParams, TextIndexParamsTypedDict
from .textsettings import TextSettings, TextSettingsTypedDict
from .tokenizertype import TokenizerType
from .update_api_key_v1_organizations_users_user_email_api_keys_key_name_patchop import (
    UpdateAPIKeyV1OrganizationsUsersUserEmailAPIKeysKeyNamePatchRequest,
    UpdateAPIKeyV1OrganizationsUsersUserEmailAPIKeysKeyNamePatchRequestTypedDict,
)
from .update_collection_v1_collections_collection_putop import (
    UpdateCollectionV1CollectionsCollectionPutRequest,
    UpdateCollectionV1CollectionsCollectionPutRequestTypedDict,
)
from .update_namespace_v1_namespaces_namespace_putop import (
    UpdateNamespaceV1NamespacesNamespacePutRequest,
    UpdateNamespaceV1NamespacesNamespacePutRequestTypedDict,
)
from .update_node_v1_entities_taxonomies_nodes_node_patchop import (
    UpdateNodeV1EntitiesTaxonomiesNodesNodePatchRequest,
    UpdateNodeV1EntitiesTaxonomiesNodesNodePatchRequestTypedDict,
)
from .update_taxonomy_v1_entities_taxonomies_taxonomy_patchop import (
    UpdateTaxonomyV1EntitiesTaxonomiesTaxonomyPatchRequest,
    UpdateTaxonomyV1EntitiesTaxonomiesTaxonomyPatchRequestTypedDict,
)
from .updateassetrequest import (
    UpdateAssetRequest,
    UpdateAssetRequestMetadata,
    UpdateAssetRequestMetadataTypedDict,
    UpdateAssetRequestTypedDict,
)
from .updatenamespacerequest import (
    UpdateNamespaceRequest,
    UpdateNamespaceRequestTypedDict,
)
from .usage import Usage, UsageTypedDict
from .usermodel_input import (
    UserModelInput,
    UserModelInputMetadata,
    UserModelInputMetadataTypedDict,
    UserModelInputTypedDict,
)
from .usermodel_output import (
    UserModelOutput,
    UserModelOutputMetadata,
    UserModelOutputMetadataTypedDict,
    UserModelOutputTypedDict,
)
from .uuidindexparams import UUIDIndexParams, UUIDIndexParamsTypedDict
from .validationerror import (
    Loc,
    LocTypedDict,
    ValidationError,
    ValidationErrorTypedDict,
)
from .vectormodel import VectorModel
from .vectortype import VectorType
from .videodescribesettings import (
    VideoDescribeSettings,
    VideoDescribeSettingsJSONOutput,
    VideoDescribeSettingsJSONOutputTypedDict,
    VideoDescribeSettingsTypedDict,
)
from .videodetectsettings import VideoDetectSettings, VideoDetectSettingsTypedDict
from .videoreadsettings import (
    JSONOutput,
    JSONOutputTypedDict,
    VideoReadSettings,
    VideoReadSettingsTypedDict,
)
from .videosettings import VideoSettings, VideoSettingsTypedDict
from .videotranscriptionsettings import (
    VideoTranscriptionSettings,
    VideoTranscriptionSettingsJSONOutput,
    VideoTranscriptionSettingsJSONOutputTypedDict,
    VideoTranscriptionSettingsTypedDict,
)


__all__ = [
    "APIError",
    "APIKey",
    "APIKeyTypedDict",
    "APIKeyUpdate",
    "APIKeyUpdateTypedDict",
    "ActionUsage",
    "ActionUsageTypedDict",
    "And",
    "AndTypedDict",
    "AssetFeatures",
    "AssetFeaturesTypedDict",
    "AssetResponse",
    "AssetResponseTypedDict",
    "AssetUpdate",
    "AssetUpdateTypedDict",
    "AssetsModelSearchQuery",
    "AssetsModelSearchQueryTypedDict",
    "AssignmentConfig",
    "AssignmentConfigTypedDict",
    "AssignmentMode",
    "AvailableModels",
    "AvailableModelsResponse",
    "AvailableModelsResponseTypedDict",
    "BoolIndexParams",
    "BoolIndexParamsTypedDict",
    "ClassificationMatch",
    "ClassificationMatchTypedDict",
    "ClassificationWithFeature",
    "ClassificationWithFeatureTypedDict",
    "ClassifyFeaturesV1EntitiesTaxonomiesTaxonomyClassifyPostRequest",
    "ClassifyFeaturesV1EntitiesTaxonomiesTaxonomyClassifyPostRequestTypedDict",
    "CollectionModel",
    "CollectionModelMetadata",
    "CollectionModelMetadataTypedDict",
    "CollectionModelTypedDict",
    "CollectionResult",
    "CollectionResultMetadata",
    "CollectionResultMetadataTypedDict",
    "CollectionResultTypedDict",
    "CreateAPIKeyV1OrganizationsUsersUserEmailAPIKeysPostRequest",
    "CreateAPIKeyV1OrganizationsUsersUserEmailAPIKeysPostRequestTypedDict",
    "CreateCollectionRequest",
    "CreateCollectionRequestMetadata",
    "CreateCollectionRequestMetadataTypedDict",
    "CreateCollectionRequestTypedDict",
    "CreateCollectionV1CollectionsPostRequest",
    "CreateCollectionV1CollectionsPostRequestTypedDict",
    "CreateNamespaceRequest",
    "CreateNamespaceRequestTypedDict",
    "CreateTaxonomyV1EntitiesTaxonomiesPostRequest",
    "CreateTaxonomyV1EntitiesTaxonomiesPostRequestTypedDict",
    "DateUsage",
    "DateUsageTypedDict",
    "DatetimeIndexParams",
    "DatetimeIndexParamsTypedDict",
    "DbModelPaginationResponse",
    "DbModelPaginationResponseTypedDict",
    "DeleteAPIKeyV1OrganizationsUsersUserEmailAPIKeysKeyNameDeleteRequest",
    "DeleteAPIKeyV1OrganizationsUsersUserEmailAPIKeysKeyNameDeleteRequestTypedDict",
    "DeleteAssetV1AssetsAssetIDDeleteRequest",
    "DeleteAssetV1AssetsAssetIDDeleteRequestTypedDict",
    "DeleteClassificationsV1EntitiesTaxonomiesTaxonomyClassificationsClassificationIDDeleteRequest",
    "DeleteClassificationsV1EntitiesTaxonomiesTaxonomyClassificationsClassificationIDDeleteRequestTypedDict",
    "DeleteCollectionV1CollectionsCollectionDeleteRequest",
    "DeleteCollectionV1CollectionsCollectionDeleteRequestTypedDict",
    "DeleteFeatureV1FeaturesFeatureIDDeleteRequest",
    "DeleteFeatureV1FeaturesFeatureIDDeleteRequestTypedDict",
    "DeleteNamespaceV1NamespacesNamespaceDeleteRequest",
    "DeleteNamespaceV1NamespacesNamespaceDeleteRequestTypedDict",
    "DeleteTaxonomyV1EntitiesTaxonomiesTaxonomyDeleteRequest",
    "DeleteTaxonomyV1EntitiesTaxonomiesTaxonomyDeleteRequestTypedDict",
    "DeleteUserV1OrganizationsUsersUserEmailDeleteRequest",
    "DeleteUserV1OrganizationsUsersUserEmailDeleteRequestTypedDict",
    "DenseEmbedding",
    "DenseEmbeddingTypedDict",
    "Details",
    "DetailsTypedDict",
    "Direction",
    "DiscoverRequest",
    "DiscoverRequestTypedDict",
    "Embedding",
    "EmbeddingConfig",
    "EmbeddingConfigType",
    "EmbeddingConfigTypedDict",
    "EmbeddingRequest",
    "EmbeddingRequestTypedDict",
    "EmbeddingResponse",
    "EmbeddingResponseTypedDict",
    "EmbeddingTypedDict",
    "EntitySettings",
    "EntitySettingsTypedDict",
    "ErrorDetail",
    "ErrorDetailTypedDict",
    "ErrorResponse",
    "ErrorResponseData",
    "FeatureExtractionEmbeddingRequest",
    "FeatureExtractionEmbeddingRequestTypedDict",
    "FeatureOptions",
    "FeatureOptionsTypedDict",
    "FeatureResponse",
    "FeatureResponseTypedDict",
    "FeatureUpdateRequest",
    "FeatureUpdateRequestMetadata",
    "FeatureUpdateRequestMetadataTypedDict",
    "FeatureUpdateRequestTypedDict",
    "FeaturesModelPaginationResponse",
    "FeaturesModelPaginationResponseTypedDict",
    "FieldSchema",
    "FieldSchemaTypedDict",
    "FileData",
    "FileDataTypedDict",
    "FilterCondition",
    "FilterConditionTypedDict",
    "FloatIndexParams",
    "FloatIndexParamsTypedDict",
    "FullAssetUpdateV1AssetsAssetIDPutRequest",
    "FullAssetUpdateV1AssetsAssetIDPutRequestTypedDict",
    "FullFeatureUpdateV1FeaturesFeatureIDPutRequest",
    "FullFeatureUpdateV1FeaturesFeatureIDPutRequestTypedDict",
    "GenericSuccessResponse",
    "GenericSuccessResponseTypedDict",
    "GeoIndexParams",
    "GeoIndexParamsTypedDict",
    "GetAssetV1AssetsAssetIDGetRequest",
    "GetAssetV1AssetsAssetIDGetRequestTypedDict",
    "GetAssetWithFeaturesV1AssetsAssetIDFeaturesGetRequest",
    "GetAssetWithFeaturesV1AssetsAssetIDFeaturesGetRequestTypedDict",
    "GetCollectionV1CollectionsCollectionGetRequest",
    "GetCollectionV1CollectionsCollectionGetRequestTypedDict",
    "GetFeatureV1FeaturesFeatureIDGetRequest",
    "GetFeatureV1FeaturesFeatureIDGetRequestTypedDict",
    "GetNamespaceV1NamespacesNamespaceGetRequest",
    "GetNamespaceV1NamespacesNamespaceGetRequestTypedDict",
    "GetTaskV1TasksTaskIDGetRequest",
    "GetTaskV1TasksTaskIDGetRequestTypedDict",
    "GetTaxonomyNodeV1EntitiesTaxonomiesNodesNodeGetRequest",
    "GetTaxonomyNodeV1EntitiesTaxonomiesNodesNodeGetRequestTypedDict",
    "GetTaxonomyV1EntitiesTaxonomiesTaxonomyGetRequest",
    "GetTaxonomyV1EntitiesTaxonomiesTaxonomyGetRequestTypedDict",
    "GetUserV1OrganizationsUsersUserEmailGetRequest",
    "GetUserV1OrganizationsUsersUserEmailGetRequestTypedDict",
    "GroupByOptions",
    "GroupByOptionsAsset",
    "GroupByOptionsAssetTypedDict",
    "GroupByOptionsTypedDict",
    "GroupedAssetData",
    "GroupedAssetDataTypedDict",
    "HTTPValidationError",
    "HTTPValidationErrorData",
    "HealthCheckResponse",
    "HealthCheckResponseTypedDict",
    "ImageDescribeSettings",
    "ImageDescribeSettingsJSONOutput",
    "ImageDescribeSettingsJSONOutputTypedDict",
    "ImageDescribeSettingsTypedDict",
    "ImageDetectSettings",
    "ImageDetectSettingsTypedDict",
    "ImageReadSettings",
    "ImageReadSettingsJSONOutput",
    "ImageReadSettingsJSONOutputTypedDict",
    "ImageReadSettingsTypedDict",
    "ImageSettings",
    "ImageSettingsTypedDict",
    "IngestImageURLV1IngestImagesURLPostRequest",
    "IngestImageURLV1IngestImagesURLPostRequestTypedDict",
    "IngestTextV1IngestTextPostRequest",
    "IngestTextV1IngestTextPostRequestTypedDict",
    "IngestVideoURLV1IngestVideosURLPostRequest",
    "IngestVideoURLV1IngestVideosURLPostRequestTypedDict",
    "InputType",
    "IntegerIndexParams",
    "IntegerIndexParamsTypedDict",
    "JSONImageOutputSettings",
    "JSONImageOutputSettingsResponseShape",
    "JSONImageOutputSettingsResponseShapeTypedDict",
    "JSONImageOutputSettingsTypedDict",
    "JSONOutput",
    "JSONOutputTypedDict",
    "JSONTextOutputSettings",
    "JSONTextOutputSettingsTypedDict",
    "JSONVideoOutputSettings",
    "JSONVideoOutputSettingsResponseShape",
    "JSONVideoOutputSettingsResponseShapeTypedDict",
    "JSONVideoOutputSettingsTypedDict",
    "KeywordIndexParams",
    "KeywordIndexParamsTypedDict",
    "KillTaskV1TasksTaskIDDeleteRequest",
    "KillTaskV1TasksTaskIDDeleteRequestTypedDict",
    "ListActiveTasksV1TasksGetRequest",
    "ListActiveTasksV1TasksGetRequestTypedDict",
    "ListAssetsRequest",
    "ListAssetsRequestTypedDict",
    "ListAssetsResponse",
    "ListAssetsResponseTypedDict",
    "ListAssetsV1AssetsPostRequest",
    "ListAssetsV1AssetsPostRequestTypedDict",
    "ListClassificationsRequest",
    "ListClassificationsRequestTypedDict",
    "ListClassificationsResponse",
    "ListClassificationsResponseTypedDict",
    "ListClassificationsV1EntitiesTaxonomiesTaxonomyClassificationsPostRequest",
    "ListClassificationsV1EntitiesTaxonomiesTaxonomyClassificationsPostRequestTypedDict",
    "ListCollectionsResponse",
    "ListCollectionsResponseTypedDict",
    "ListCollectionsV1CollectionsGetRequest",
    "ListCollectionsV1CollectionsGetRequestTypedDict",
    "ListFeaturesRequest",
    "ListFeaturesRequestTypedDict",
    "ListFeaturesResponse",
    "ListFeaturesResponseTypedDict",
    "ListFeaturesV1FeaturesPostRequest",
    "ListFeaturesV1FeaturesPostRequestTypedDict",
    "ListTasksResponse",
    "ListTasksResponseTypedDict",
    "ListTaxonomiesResponse",
    "ListTaxonomiesResponseTypedDict",
    "ListTaxonomiesV1EntitiesTaxonomiesGetRequest",
    "ListTaxonomiesV1EntitiesTaxonomiesGetRequestTypedDict",
    "Loc",
    "LocTypedDict",
    "LogicalOperator",
    "LogicalOperatorTypedDict",
    "LogoDetectSettings",
    "LogoDetectSettingsTypedDict",
    "Metadata",
    "MetadataTypedDict",
    "Modality",
    "Mode",
    "ModelDetails",
    "ModelDetailsTypedDict",
    "NamespaceResponse",
    "NamespaceResponseTypedDict",
    "NodeOptions",
    "NodeOptionsTypedDict",
    "NodeUpdate",
    "NodeUpdateTypedDict",
    "Nor",
    "NorTypedDict",
    "Operator",
    "Or",
    "OrTypedDict",
    "OrganizationModel",
    "OrganizationModelMetadata",
    "OrganizationModelMetadataTypedDict",
    "OrganizationModelTypedDict",
    "PartialAssetUpdateV1AssetsAssetIDPatchRequest",
    "PartialAssetUpdateV1AssetsAssetIDPatchRequestTypedDict",
    "PayloadIndexConfig",
    "PayloadIndexConfigTypedDict",
    "PayloadIndexType",
    "PayloadIndexTypeTypedDict",
    "PayloadSchemaType",
    "Permission",
    "ProcessImageURLInput",
    "ProcessImageURLInputMetadata",
    "ProcessImageURLInputMetadataTypedDict",
    "ProcessImageURLInputTypedDict",
    "ProcessTextInput",
    "ProcessTextInputMetadata",
    "ProcessTextInputMetadataTypedDict",
    "ProcessTextInputTypedDict",
    "ProcessVideoURLInput",
    "ProcessVideoURLInputMetadata",
    "ProcessVideoURLInputMetadataTypedDict",
    "ProcessVideoURLInputTypedDict",
    "QuerySettings",
    "QuerySettingsTypedDict",
    "RerankingOptions",
    "RerankingOptionsTypedDict",
    "ResponseShape",
    "ResponseShapeTypedDict",
    "SearchAssetsRequest",
    "SearchAssetsRequestTypedDict",
    "SearchAssetsV1AssetsSearchPostRequest",
    "SearchAssetsV1AssetsSearchPostRequestTypedDict",
    "SearchFeaturesV1FeaturesSearchPostRequest",
    "SearchFeaturesV1FeaturesSearchPostRequestTypedDict",
    "SearchFeaturesV1FeaturesSearchPostResponseSearchFeaturesV1FeaturesSearchPost",
    "SearchFeaturesV1FeaturesSearchPostResponseSearchFeaturesV1FeaturesSearchPostTypedDict",
    "SearchModelSearchQuery",
    "SearchModelSearchQueryTypedDict",
    "SearchRequestFeatures",
    "SearchRequestFeaturesTypedDict",
    "Security",
    "SecurityTypedDict",
    "SortOption",
    "SortOptionTypedDict",
    "SparseEmbedding",
    "SparseEmbeddingTypedDict",
    "TaskResponse",
    "TaskResponseTypedDict",
    "TaskStatus",
    "TaxonomyCreate",
    "TaxonomyCreateTypedDict",
    "TaxonomyExtractionConfig",
    "TaxonomyExtractionConfigTypedDict",
    "TaxonomyModel",
    "TaxonomyModelTypedDict",
    "TaxonomyNode",
    "TaxonomyNodeCreate",
    "TaxonomyNodeCreateTypedDict",
    "TaxonomyNodeTypedDict",
    "TaxonomyUpdate",
    "TaxonomyUpdateTypedDict",
    "TextIndexParams",
    "TextIndexParamsTypedDict",
    "TextSettings",
    "TextSettingsTypedDict",
    "TokenizerType",
    "Type",
    "UUIDIndexParams",
    "UUIDIndexParamsTypedDict",
    "UpdateAPIKeyV1OrganizationsUsersUserEmailAPIKeysKeyNamePatchRequest",
    "UpdateAPIKeyV1OrganizationsUsersUserEmailAPIKeysKeyNamePatchRequestTypedDict",
    "UpdateAssetRequest",
    "UpdateAssetRequestMetadata",
    "UpdateAssetRequestMetadataTypedDict",
    "UpdateAssetRequestTypedDict",
    "UpdateCollectionV1CollectionsCollectionPutRequest",
    "UpdateCollectionV1CollectionsCollectionPutRequestTypedDict",
    "UpdateNamespaceRequest",
    "UpdateNamespaceRequestTypedDict",
    "UpdateNamespaceV1NamespacesNamespacePutRequest",
    "UpdateNamespaceV1NamespacesNamespacePutRequestTypedDict",
    "UpdateNodeV1EntitiesTaxonomiesNodesNodePatchRequest",
    "UpdateNodeV1EntitiesTaxonomiesNodesNodePatchRequestTypedDict",
    "UpdateTaxonomyV1EntitiesTaxonomiesTaxonomyPatchRequest",
    "UpdateTaxonomyV1EntitiesTaxonomiesTaxonomyPatchRequestTypedDict",
    "Usage",
    "UsageTypedDict",
    "UserModelInput",
    "UserModelInputMetadata",
    "UserModelInputMetadataTypedDict",
    "UserModelInputTypedDict",
    "UserModelOutput",
    "UserModelOutputMetadata",
    "UserModelOutputMetadataTypedDict",
    "UserModelOutputTypedDict",
    "ValidationError",
    "ValidationErrorTypedDict",
    "VectorModel",
    "VectorType",
    "VideoDescribeSettings",
    "VideoDescribeSettingsJSONOutput",
    "VideoDescribeSettingsJSONOutputTypedDict",
    "VideoDescribeSettingsTypedDict",
    "VideoDetectSettings",
    "VideoDetectSettingsTypedDict",
    "VideoReadSettings",
    "VideoReadSettingsTypedDict",
    "VideoSettings",
    "VideoSettingsTypedDict",
    "VideoTranscriptionSettings",
    "VideoTranscriptionSettingsJSONOutput",
    "VideoTranscriptionSettingsJSONOutputTypedDict",
    "VideoTranscriptionSettingsTypedDict",
]
