# SnowflakeUsernamePasswordCredentials

Snowflake username/password authentication (FALLBACK option).  Traditional username/password authentication for Snowflake. Less secure than key pair authentication but simpler to set up.  Security:     - Password encrypted at rest via CSFLE     - Consider using key pair auth for production     - Enable MFA on Snowflake user account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'username_password']
**username** | **str** | REQUIRED. Snowflake username (case-insensitive). | 
**password** | **str** | REQUIRED. Snowflake password for authentication. SECURITY: This field is encrypted at rest via CSFLE. Never log or expose. | 

## Example

```python
from mixpeek.models.snowflake_username_password_credentials import SnowflakeUsernamePasswordCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeUsernamePasswordCredentials from a JSON string
snowflake_username_password_credentials_instance = SnowflakeUsernamePasswordCredentials.from_json(json)
# print the JSON string representation of the object
print(SnowflakeUsernamePasswordCredentials.to_json())

# convert the object into a dict
snowflake_username_password_credentials_dict = snowflake_username_password_credentials_instance.to_dict()
# create an instance of SnowflakeUsernamePasswordCredentials from a dict
snowflake_username_password_credentials_from_dict = SnowflakeUsernamePasswordCredentials.from_dict(snowflake_username_password_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


