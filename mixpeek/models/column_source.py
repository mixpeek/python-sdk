from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ColumnSource")


@_attrs_define
class ColumnSource:
    """Extract value from a database column (Snowflake, PostgreSQL, etc.).

    For database sync sources, maps a column from the source table/view
    to a bucket schema field. Column handling varies by database.

    Provider Compatibility: Snowflake, PostgreSQL (future), BigQuery (future)

    Example Snowflake table:
        CREATE TABLE CUSTOMERS (
            ID VARCHAR, NAME VARCHAR, CATEGORY VARCHAR,
            CREATED_AT TIMESTAMP, PROFILE_IMAGE_URL VARCHAR
        );

    Example mapping:
        {"type": "column", "name": "CATEGORY"} -> extracts the CATEGORY column value

    Database-Specific Notes:
        - Snowflake: Case-insensitive (internally uppercase), use unquoted names
        - PostgreSQL: Case-sensitive if quoted, defaults to lowercase
        - BigQuery: Case-sensitive

    Attributes:
        type: Must be "column" to identify this source type
        name: The column name to extract from

        Attributes:
            name (str): The column name to extract from. Case handling depends on the database. Snowflake: case-insensitive
                (defaults to uppercase). PostgreSQL: case-sensitive unless quoted. Column must exist in the source table/view.
            type_ (Literal['column'] | Unset): Source type identifier. Must be 'column' for database columns. Default:
                'column'.
    """

    name: str
    type_: Literal["column"] | Unset = "column"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = cast(Literal["column"] | Unset, d.pop("type", UNSET))
        if type_ != "column" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'column', got '{type_}'")

        column_source = cls(
            name=name,
            type_=type_,
        )

        column_source.additional_properties = d
        return column_source

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
