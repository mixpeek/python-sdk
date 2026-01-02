from enum import Enum


class StorageProvider(str, Enum):
    GOOGLE_DRIVE = "google_drive"
    POSTGRESQL = "postgresql"
    S3 = "s3"
    SHAREPOINT = "sharepoint"
    SNOWFLAKE = "snowflake"
    TIGRIS = "tigris"

    def __str__(self) -> str:
        return str(self.value)
