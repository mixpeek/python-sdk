from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tokenizer_type import TokenizerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TextIndexParams")


@_attrs_define
class TextIndexParams:
    """Configuration for text index.

    Attributes:
        type_ (str | Unset):  Default: 'text'.
        tokenizer (TokenizerType | Unset): Tokenizer type.
        min_token_len (int | Unset):  Default: 2.
        max_token_len (int | Unset):  Default: 15.
        lowercase (bool | Unset):  Default: True.
    """

    type_: str | Unset = "text"
    tokenizer: TokenizerType | Unset = UNSET
    min_token_len: int | Unset = 2
    max_token_len: int | Unset = 15
    lowercase: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        tokenizer: str | Unset = UNSET
        if not isinstance(self.tokenizer, Unset):
            tokenizer = self.tokenizer.value

        min_token_len = self.min_token_len

        max_token_len = self.max_token_len

        lowercase = self.lowercase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if tokenizer is not UNSET:
            field_dict["tokenizer"] = tokenizer
        if min_token_len is not UNSET:
            field_dict["min_token_len"] = min_token_len
        if max_token_len is not UNSET:
            field_dict["max_token_len"] = max_token_len
        if lowercase is not UNSET:
            field_dict["lowercase"] = lowercase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _tokenizer = d.pop("tokenizer", UNSET)
        tokenizer: TokenizerType | Unset
        if isinstance(_tokenizer, Unset):
            tokenizer = UNSET
        else:
            tokenizer = TokenizerType(_tokenizer)

        min_token_len = d.pop("min_token_len", UNSET)

        max_token_len = d.pop("max_token_len", UNSET)

        lowercase = d.pop("lowercase", UNSET)

        text_index_params = cls(
            type_=type_,
            tokenizer=tokenizer,
            min_token_len=min_token_len,
            max_token_len=max_token_len,
            lowercase=lowercase,
        )

        text_index_params.additional_properties = d
        return text_index_params

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
