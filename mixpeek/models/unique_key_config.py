from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.unique_key_config_default_policy_type_0 import UniqueKeyConfigDefaultPolicyType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="UniqueKeyConfig")


@_attrs_define
class UniqueKeyConfig:
    """Configuration for bucket unique key enforcement.

    Enables automatic uniqueness enforcement on one or more fields from the bucket schema.
    Supports both single field and compound (multi-field) uniqueness constraints.

    When configured, the bucket will maintain a lookup table mapping unique key values
    to document IDs, enabling efficient upsert operations and preventing duplicates.

    **Impact on Collection Trigger/Re-processing:**
    When a collection is triggered (POST /collections/{id}/trigger), the unique_key
    determines whether documents are overwritten or duplicated:
    - WITH unique_key: Documents get deterministic IDs → re-triggering OVERWRITES existing docs
    - WITHOUT unique_key: Documents get random IDs → re-triggering CREATES DUPLICATES

    For idempotent pipelines where re-triggering is safe, configure a unique_key.

    **Relationship to Extractor position_fields:**
    The `unique_key` (bucket-level) and `position_fields` (extractor-level) work together
    to generate deterministic document IDs:

    - `unique_key`: Identifies unique SOURCE OBJECTS in the bucket (e.g., video_id)
    - `position_fields`: Identifies unique OUTPUT DOCUMENTS from a single object (e.g., start_time, end_time)

    Document ID Formula:
        document_id = hash(source_object_key + extractor_id + collection_id + position_field_values)

    Example - Processing a 60-second video with 10-second segments:
        - Bucket unique_key: ["video_id"] → Identifies the source video
        - Extractor position_fields: ["start_time", "end_time"] → Identifies each segment
        - Result: 6 unique document IDs (one per segment), all deterministic

    Without position_fields, all segments would get the SAME document_id and overwrite each other.
    Without unique_key, reprocessing would create DUPLICATE documents instead of updating.

    Requirements:
        - fields: REQUIRED - Array of field names from bucket schema to use as unique constraint
        - default_policy: OPTIONAL - Bucket-level default insertion policy (can be overridden per request)
        - All specified fields must exist in the bucket schema
        - All fields must be scalar types (string, integer, float, uuid)
        - Field values cannot be null or empty in uploaded objects
        - Cannot be changed after bucket creation (v1 limitation)

    Use Cases:
        - Single field uniqueness: ["video_id"], ["product_sku"], ["user_email"]
        - Compound uniqueness: ["sensor_id", "timestamp"], ["product_id", "size", "color"]
        - With default policy: Enables idempotent ingestion without per-request policy
        - Without default: Requires explicit policy on each upload (safer, more intentional)

    Insertion Policies:
        - 'insert': Fail with 409 Conflict if key exists (prevents accidental overwrites)
        - 'update': Fail with 404 Not Found if key doesn't exist (updates only)
        - 'upsert': Update if exists, insert if not (idempotent ingestion)

    Policy Resolution (when uploading objects):
        1. Use request-level ?policy= parameter if provided (highest priority)
        2. Fall back to bucket-level default_policy if configured
        3. Return 400 Bad Request if neither is specified (prevents accidental operations)

    Examples:
        Single field with upsert default (idempotent video ingestion):
            {
                "fields": ["video_id"],
                "default_policy": "upsert"
            }

        Single field with insert default (prevent duplicate products):
            {
                "fields": ["product_sku"],
                "default_policy": "insert"
            }

        Compound fields with upsert (time-series sensor data):
            {
                "fields": ["sensor_id", "timestamp"],
                "default_policy": "upsert"
            }

        Compound fields without default (explicit policy required):
            {
                "fields": ["user_id", "session_id"]
            }

        Attributes:
            fields (list[str]): Field name(s) from bucket schema to use as unique constraint. REQUIRED - must provide at
                least one field name.

                Single field example: ['video_id'] - Enforces uniqueness on video_id alone. Compound example: ['sensor_id',
                'timestamp'] - Uniqueness requires BOTH fields to match.

                All specified fields must:
                  - Exist in the bucket schema
                  - Be scalar types (string, integer, float, uuid - NOT objects or arrays)
                  - Have non-null, non-empty values in all uploaded objects
                  - Be 255 characters or less per string field value


                Field order doesn't matter (sorted internally for consistency). ['timestamp', 'sensor_id'] is equivalent to
                ['sensor_id', 'timestamp'].
            default_policy (None | UniqueKeyConfigDefaultPolicyType0 | Unset): Default insertion policy for this bucket when
                not specified per request. OPTIONAL - if omitted, you must provide ?policy= parameter on each upload request.

                Policies:
                  - 'insert': Create new object only. Fail with 409 Conflict if unique key already exists.
                              Use when: You want to prevent accidental overwrites (safest option).

                  - 'update': Update existing object only. Fail with 404 Not Found if unique key doesn't exist.
                              Use when: You only want to update existing records, never create new ones.

                  - 'upsert': Update if exists, create if not (idempotent operation).
                              Use when: You want idempotent ingestion (re-running is safe).

                Policy Resolution:
                  1. Request-level ?policy= parameter takes precedence (if provided)
                  2. Falls back to this default_policy (if configured)
                  3. Returns 400 Bad Request if neither is specified

                Recommendation: Omit default_policy if you want explicit control on each upload. Set default_policy='upsert' for
                idempotent pipelines.
    """

    fields: list[str]
    default_policy: None | UniqueKeyConfigDefaultPolicyType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields = self.fields

        default_policy: None | str | Unset
        if isinstance(self.default_policy, Unset):
            default_policy = UNSET
        elif isinstance(self.default_policy, UniqueKeyConfigDefaultPolicyType0):
            default_policy = self.default_policy.value
        else:
            default_policy = self.default_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields": fields,
            }
        )
        if default_policy is not UNSET:
            field_dict["default_policy"] = default_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fields = cast(list[str], d.pop("fields"))

        def _parse_default_policy(data: object) -> None | UniqueKeyConfigDefaultPolicyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_policy_type_0 = UniqueKeyConfigDefaultPolicyType0(data)

                return default_policy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UniqueKeyConfigDefaultPolicyType0 | Unset, data)

        default_policy = _parse_default_policy(d.pop("default_policy", UNSET))

        unique_key_config = cls(
            fields=fields,
            default_policy=default_policy,
        )

        unique_key_config.additional_properties = d
        return unique_key_config

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
