from enum import Enum


class NotificationType(str, Enum):
    AUDIT_ALERT = "audit_alert"
    BILLING_ALERT = "billing_alert"
    CUSTOM = "custom"
    FEATURE_EXTRACTION_FAILURE = "feature_extraction_failure"
    FEATURE_EXTRACTION_SUCCESS = "feature_extraction_success"
    MAINTENANCE_ALERT = "maintenance_alert"
    PIPELINE_FAILURE = "pipeline_failure"
    PIPELINE_SUCCESS = "pipeline_success"
    QUOTA_ALERT = "quota_alert"
    SYSTEM_ALERT = "system_alert"

    def __str__(self) -> str:
        return str(self.value)
