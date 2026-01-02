from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_condition import FilterCondition


T = TypeVar("T", bound="LogicalOperator")


@_attrs_define
class LogicalOperator:
    """Represents a logical operation (AND, OR, NOT) on filter conditions.

    Allows nesting with a defined depth limit.

    Also supports shorthand syntax where field names can be passed directly
    as key-value pairs for equality filtering (e.g., {"metadata.title": "value"}).

        Attributes:
            and_ (list[FilterCondition | LogicalOperator] | None | Unset): Logical AND operation - all conditions must be
                true Example: [{'field': 'name', 'operator': 'eq', 'value': 'John'}, {'field': 'age', 'operator': 'gte',
                'value': 30}].
            or_ (list[FilterCondition | LogicalOperator] | None | Unset): Logical OR operation - at least one condition must
                be true Example: [{'field': 'status', 'operator': 'eq', 'value': 'active'}, {'field': 'role', 'operator': 'eq',
                'value': 'admin'}].
            not_ (list[FilterCondition | LogicalOperator] | None | Unset): Logical NOT operation - all conditions must be
                false Example: [{'field': 'department', 'operator': 'eq', 'value': 'HR'}, {'field': 'location', 'operator':
                'eq', 'value': 'remote'}].
            case_sensitive (bool | None | Unset): Whether to perform case-sensitive matching Default: False. Example: True.
    """

    and_: list[FilterCondition | LogicalOperator] | None | Unset = UNSET
    or_: list[FilterCondition | LogicalOperator] | None | Unset = UNSET
    not_: list[FilterCondition | LogicalOperator] | None | Unset = UNSET
    case_sensitive: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        and_: list[dict[str, Any]] | None | Unset
        if isinstance(self.and_, Unset):
            and_ = UNSET
        elif isinstance(self.and_, list):
            and_ = []
            for and_type_0_item_data in self.and_:
                and_type_0_item: dict[str, Any]
                if isinstance(and_type_0_item_data, LogicalOperator):
                    and_type_0_item = and_type_0_item_data.to_dict()
                else:
                    and_type_0_item = and_type_0_item_data.to_dict()

                and_.append(and_type_0_item)

        else:
            and_ = self.and_

        or_: list[dict[str, Any]] | None | Unset
        if isinstance(self.or_, Unset):
            or_ = UNSET
        elif isinstance(self.or_, list):
            or_ = []
            for or_type_0_item_data in self.or_:
                or_type_0_item: dict[str, Any]
                if isinstance(or_type_0_item_data, LogicalOperator):
                    or_type_0_item = or_type_0_item_data.to_dict()
                else:
                    or_type_0_item = or_type_0_item_data.to_dict()

                or_.append(or_type_0_item)

        else:
            or_ = self.or_

        not_: list[dict[str, Any]] | None | Unset
        if isinstance(self.not_, Unset):
            not_ = UNSET
        elif isinstance(self.not_, list):
            not_ = []
            for not_type_0_item_data in self.not_:
                not_type_0_item: dict[str, Any]
                if isinstance(not_type_0_item_data, LogicalOperator):
                    not_type_0_item = not_type_0_item_data.to_dict()
                else:
                    not_type_0_item = not_type_0_item_data.to_dict()

                not_.append(not_type_0_item)

        else:
            not_ = self.not_

        case_sensitive: bool | None | Unset
        if isinstance(self.case_sensitive, Unset):
            case_sensitive = UNSET
        else:
            case_sensitive = self.case_sensitive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if and_ is not UNSET:
            field_dict["AND"] = and_
        if or_ is not UNSET:
            field_dict["OR"] = or_
        if not_ is not UNSET:
            field_dict["NOT"] = not_
        if case_sensitive is not UNSET:
            field_dict["case_sensitive"] = case_sensitive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_condition import FilterCondition

        d = dict(src_dict)

        def _parse_and_(data: object) -> list[FilterCondition | LogicalOperator] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                and_type_0 = []
                _and_type_0 = data
                for and_type_0_item_data in _and_type_0:

                    def _parse_and_type_0_item(data: object) -> FilterCondition | LogicalOperator:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            and_type_0_item_type_0 = LogicalOperator.from_dict(data)

                            return and_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        and_type_0_item_type_1 = FilterCondition.from_dict(data)

                        return and_type_0_item_type_1

                    and_type_0_item = _parse_and_type_0_item(and_type_0_item_data)

                    and_type_0.append(and_type_0_item)

                return and_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FilterCondition | LogicalOperator] | None | Unset, data)

        and_ = _parse_and_(d.pop("AND", UNSET))

        def _parse_or_(data: object) -> list[FilterCondition | LogicalOperator] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                or_type_0 = []
                _or_type_0 = data
                for or_type_0_item_data in _or_type_0:

                    def _parse_or_type_0_item(data: object) -> FilterCondition | LogicalOperator:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            or_type_0_item_type_0 = LogicalOperator.from_dict(data)

                            return or_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        or_type_0_item_type_1 = FilterCondition.from_dict(data)

                        return or_type_0_item_type_1

                    or_type_0_item = _parse_or_type_0_item(or_type_0_item_data)

                    or_type_0.append(or_type_0_item)

                return or_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FilterCondition | LogicalOperator] | None | Unset, data)

        or_ = _parse_or_(d.pop("OR", UNSET))

        def _parse_not_(data: object) -> list[FilterCondition | LogicalOperator] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                not_type_0 = []
                _not_type_0 = data
                for not_type_0_item_data in _not_type_0:

                    def _parse_not_type_0_item(data: object) -> FilterCondition | LogicalOperator:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            not_type_0_item_type_0 = LogicalOperator.from_dict(data)

                            return not_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        not_type_0_item_type_1 = FilterCondition.from_dict(data)

                        return not_type_0_item_type_1

                    not_type_0_item = _parse_not_type_0_item(not_type_0_item_data)

                    not_type_0.append(not_type_0_item)

                return not_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FilterCondition | LogicalOperator] | None | Unset, data)

        not_ = _parse_not_(d.pop("NOT", UNSET))

        def _parse_case_sensitive(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        case_sensitive = _parse_case_sensitive(d.pop("case_sensitive", UNSET))

        logical_operator = cls(
            and_=and_,
            or_=or_,
            not_=not_,
            case_sensitive=case_sensitive,
        )

        logical_operator.additional_properties = d
        return logical_operator

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
