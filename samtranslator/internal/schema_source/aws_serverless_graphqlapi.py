from typing import Dict, List, Optional, Union

from typing_extensions import Literal

from samtranslator.internal.schema_source.common import (
    BaseModel,
    DictStrAny,
    PassThroughProp,
    PermissionsType,
    get_prop,
)

AuthenticationTypes = Literal["AWS_IAM", "API_KEY", "AWS_LAMBDA", "OPENID_CONNECT", "AMAZON_COGNITO_USER_POOLS"]

properties = get_prop("sam-resource-graphqlapi")


# TODO: add docs
class LambdaAuthorizer(BaseModel):
    AuthorizerResultTtlInSeconds: Optional[PassThroughProp]
    AuthorizerUri: Optional[PassThroughProp]
    IdentityValidationExpression: Optional[PassThroughProp]


class OpenIDConnect(BaseModel):
    AuthTTL: Optional[PassThroughProp]
    ClientId: Optional[PassThroughProp]
    IatTTL: Optional[PassThroughProp]
    Issuer: Optional[PassThroughProp]


class UserPool(BaseModel):
    AppIdClientRegex: Optional[PassThroughProp]
    AwsRegion: Optional[PassThroughProp]
    DefaultAction: Optional[PassThroughProp]
    UserPoolId: Optional[PassThroughProp]


class AdditionalAuth(BaseModel):
    Type: AuthenticationTypes
    LambdaAuthorizer: Optional[LambdaAuthorizer]
    OpenIDConnect: Optional[OpenIDConnect]
    UserPool: Optional[UserPool]


class Auth(BaseModel):
    Type: AuthenticationTypes
    LambdaAuthorizer: Optional[LambdaAuthorizer]
    OpenIDConnect: Optional[OpenIDConnect]
    UserPool: Optional[UserPool]
    Additional: Optional[List[AdditionalAuth]]


class ApiKey(BaseModel):
    ApiKeyId: Optional[PassThroughProp]
    Description: Optional[PassThroughProp]
    ExpiresOn: Optional[PassThroughProp]


class Logging(BaseModel):
    CloudWatchLogsRoleArn: Optional[PassThroughProp]
    ExcludeVerboseContent: Optional[PassThroughProp]
    FieldLogLevel: Optional[str]


class DeltaSync(BaseModel):
    BaseTableTTL: str
    DeltaSyncTableName: str
    DeltaSyncTableTTL: str


class DynamoDBDataSource(BaseModel):
    TableName: PassThroughProp
    ServiceRoleArn: Optional[PassThroughProp]
    TableArn: Optional[PassThroughProp]
    Permissions: Optional[PermissionsType]
    Name: Optional[str]
    Description: Optional[PassThroughProp]
    Region: Optional[PassThroughProp]
    DeltaSync: Optional[DeltaSync]
    UseCallerCredentials: Optional[PassThroughProp]
    Versioned: Optional[PassThroughProp]


class LambdaDataSource(BaseModel):
    FunctionArn: PassThroughProp
    ServiceRoleArn: Optional[PassThroughProp]
    Name: Optional[str]
    Description: Optional[PassThroughProp]


class DataSources(BaseModel):
    DynamoDb: Optional[Dict[str, DynamoDBDataSource]]
    Lambda: Optional[Dict[str, LambdaDataSource]]


class Runtime(BaseModel):
    Name: PassThroughProp
    Version: PassThroughProp


class ResolverCodeSettings(BaseModel):
    CodeRootPath: str
    Runtime: Runtime
    FunctionsFolder: Optional[str]


class LambdaConflictHandlerConfig(BaseModel):
    LambdaConflictHandlerArn: PassThroughProp


class Sync(BaseModel):
    ConflictDetection: PassThroughProp
    ConflictHandler: Optional[PassThroughProp]
    LambdaConflictHandlerConfig: Optional[LambdaConflictHandlerConfig]


class Function(BaseModel):
    DataSource: Optional[str]
    DataSourceName: Optional[str]
    Runtime: Optional[Runtime]
    InlineCode: Optional[PassThroughProp]
    CodeUri: Optional[PassThroughProp]
    Description: Optional[PassThroughProp]
    MaxBatchSize: Optional[PassThroughProp]
    Name: Optional[str]
    Id: Optional[PassThroughProp]
    Sync: Optional[Sync]


class Caching(BaseModel):
    Ttl: PassThroughProp
    CachingKeys: Optional[List[PassThroughProp]]


class AppSyncResolver(BaseModel):
    FieldName: Optional[str]
    Caching: Optional[Caching]
    InlineCode: Optional[PassThroughProp]
    CodeUri: Optional[PassThroughProp]
    DataSource: Optional[str]
    DataSourceName: Optional[str]
    MaxBatchSize: Optional[PassThroughProp]
    Functions: Optional[List[Union[str, Dict[str, Function]]]]
    Runtime: Optional[Runtime]
    Sync: Optional[Sync]


class DomainName(BaseModel):
    CertificateArn: PassThroughProp
    DomainName: PassThroughProp
    Description: Optional[PassThroughProp]


class Cache(BaseModel):
    ApiCachingBehavior: PassThroughProp
    Ttl: PassThroughProp
    Type: PassThroughProp
    AtRestEncryptionEnabled: Optional[PassThroughProp]
    TransitEncryptionEnabled: Optional[PassThroughProp]


class Properties(BaseModel):
    Auth: Auth
    Tags: Optional[DictStrAny]
    Name: Optional[str]
    XrayEnabled: Optional[bool]
    SchemaInline: Optional[PassThroughProp]
    SchemaUri: Optional[PassThroughProp]
    Logging: Optional[Union[Logging, bool]]
    DataSources: Optional[DataSources]
    ResolverCodeSettings: Optional[ResolverCodeSettings]
    Functions: Optional[Dict[str, Function]]
    AppSyncResolvers: Optional[Dict[str, Dict[str, AppSyncResolver]]]
    ApiKey: Optional[Dict[str, ApiKey]]
    DomainName: Optional[DomainName]
    Cache: Optional[Cache]


class Resource(BaseModel):
    Type: Literal["AWS::Serverless::GraphQLApi"]
    Properties: Properties