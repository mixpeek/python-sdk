from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="S3RoleCredentials")


@_attrs_define
class S3RoleCredentials:
    """AWS S3 IAM role assumption credentials (RECOMMENDED for production).

    IAM role assumption provides secure, temporary credentials for accessing customer
    S3 buckets without sharing long-lived access keys. This is the recommended
    authentication method for production deployments.

    How It Works:
        1. Customer creates an IAM role in their AWS account
        2. Role trust policy allows Mixpeek AWS account to assume the role
        3. External ID provides additional security against confused deputy attacks
        4. Mixpeek assumes the role and receives temporary credentials (auto-renewed)
        5. Temporary credentials are used to access the customer's S3 bucket

    Prerequisites:
        1. Create IAM role in customer AWS account
        2. Attach policy granting s3:GetObject, s3:ListBucket permissions
        3. Configure trust relationship to allow Mixpeek account
        4. Use organization-specific external_id for security
        5. Share role ARN with Mixpeek

    Security Advantages:
        - No long-lived credentials shared with third parties
        - Temporary credentials automatically rotate (1-hour sessions by default)
        - Customer retains full control and can revoke access anytime
        - External ID prevents confused deputy attacks
        - Audit trail in CloudTrail for all access

    Use Cases:
        - Production deployments accessing customer S3 buckets
        - Enterprise integrations requiring strong security
        - Multi-tenant environments with customer-owned storage
        - Compliance-sensitive workloads (HIPAA, SOC 2, etc.)

        Attributes:
            role_arn (str): REQUIRED. Amazon Resource Name (ARN) of the IAM role to assume. This role must exist in the
                customer's AWS account and have a trust relationship configured to allow Mixpeek to assume it. Format:
                arn:aws:iam::{account-id}:role/{role-name} Example trust policy should allow principal: arn:aws:iam::{mixpeek-
                account}:root Recommended role name: mixpeek-storage-sync-role
            external_id (str): REQUIRED. External ID for secure role assumption (prevents confused deputy attacks). This
                value should be unique to your organization and kept confidential. Mixpeek provides this value during connection
                setup. Must match the ExternalId condition in the role's trust policy. Format: Recommended pattern is
                mixpeek-{organization_id} Security: Include this in the trust policy Condition statement
            type_ (Literal['iam_role'] | Unset):  Default: 'iam_role'.
    """

    role_arn: str
    external_id: str
    type_: Literal["iam_role"] | Unset = "iam_role"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role_arn = self.role_arn

        external_id = self.external_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role_arn": role_arn,
                "external_id": external_id,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role_arn = d.pop("role_arn")

        external_id = d.pop("external_id")

        type_ = cast(Literal["iam_role"] | Unset, d.pop("type", UNSET))
        if type_ != "iam_role" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'iam_role', got '{type_}'")

        s3_role_credentials = cls(
            role_arn=role_arn,
            external_id=external_id,
            type_=type_,
        )

        s3_role_credentials.additional_properties = d
        return s3_role_credentials

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
