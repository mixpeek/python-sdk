from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResultCardProperties")


@_attrs_define
class ResultCardProperties:
    """Properties for result card display configuration.

    Attributes:
        layout (str | Unset): Card layout orientation Default: 'vertical'.
        show_thumbnail (bool | Unset): Whether to show thumbnail image in results Default: True.
        thumbnail_aspect_ratio (str | Unset): Aspect ratio for thumbnail images Default: '16/9'.
        thumbnail_fit (str | Unset): How thumbnail should fit in container Default: 'cover'.
        show_score (bool | Unset): Whether to display relevance score Default: False.
        truncate_title (int | None | Unset): Maximum characters for title before truncation
        truncate_description (int | None | Unset): Maximum characters for description before truncation
        field_order (list[str] | Unset): Order of fields to display in result card. Fields not in this list won't be
            shown. Must be subset of exposed_fields.
        show_find_similar (bool | Unset): Whether to show a 'Find Similar' button on result cards Default: False.
        card_click_action (str | Unset): Action when card is clicked: none (no action), findSimilar (trigger similar
            search), viewDetails (open detail modal) Default: 'viewDetails'.
        thumbnail_field (None | str | Unset): Field name to use as thumbnail image source
        title_field (None | str | Unset): Field name to use as card title
        card_fields (list[str] | None | Unset): Fields to display on the card (alternative to field_order for template
            compatibility)
        modal_fields (list[str] | None | Unset): Fields to display in the detail modal when card is clicked
        card_style (None | str | Unset): Card style preset: default, portrait-discovery, media-search, document-search,
            or custom template-specific styles Default: 'default'.
    """

    layout: str | Unset = "vertical"
    show_thumbnail: bool | Unset = True
    thumbnail_aspect_ratio: str | Unset = "16/9"
    thumbnail_fit: str | Unset = "cover"
    show_score: bool | Unset = False
    truncate_title: int | None | Unset = UNSET
    truncate_description: int | None | Unset = UNSET
    field_order: list[str] | Unset = UNSET
    show_find_similar: bool | Unset = False
    card_click_action: str | Unset = "viewDetails"
    thumbnail_field: None | str | Unset = UNSET
    title_field: None | str | Unset = UNSET
    card_fields: list[str] | None | Unset = UNSET
    modal_fields: list[str] | None | Unset = UNSET
    card_style: None | str | Unset = "default"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        layout = self.layout

        show_thumbnail = self.show_thumbnail

        thumbnail_aspect_ratio = self.thumbnail_aspect_ratio

        thumbnail_fit = self.thumbnail_fit

        show_score = self.show_score

        truncate_title: int | None | Unset
        if isinstance(self.truncate_title, Unset):
            truncate_title = UNSET
        else:
            truncate_title = self.truncate_title

        truncate_description: int | None | Unset
        if isinstance(self.truncate_description, Unset):
            truncate_description = UNSET
        else:
            truncate_description = self.truncate_description

        field_order: list[str] | Unset = UNSET
        if not isinstance(self.field_order, Unset):
            field_order = self.field_order

        show_find_similar = self.show_find_similar

        card_click_action = self.card_click_action

        thumbnail_field: None | str | Unset
        if isinstance(self.thumbnail_field, Unset):
            thumbnail_field = UNSET
        else:
            thumbnail_field = self.thumbnail_field

        title_field: None | str | Unset
        if isinstance(self.title_field, Unset):
            title_field = UNSET
        else:
            title_field = self.title_field

        card_fields: list[str] | None | Unset
        if isinstance(self.card_fields, Unset):
            card_fields = UNSET
        elif isinstance(self.card_fields, list):
            card_fields = self.card_fields

        else:
            card_fields = self.card_fields

        modal_fields: list[str] | None | Unset
        if isinstance(self.modal_fields, Unset):
            modal_fields = UNSET
        elif isinstance(self.modal_fields, list):
            modal_fields = self.modal_fields

        else:
            modal_fields = self.modal_fields

        card_style: None | str | Unset
        if isinstance(self.card_style, Unset):
            card_style = UNSET
        else:
            card_style = self.card_style

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if layout is not UNSET:
            field_dict["layout"] = layout
        if show_thumbnail is not UNSET:
            field_dict["show_thumbnail"] = show_thumbnail
        if thumbnail_aspect_ratio is not UNSET:
            field_dict["thumbnail_aspect_ratio"] = thumbnail_aspect_ratio
        if thumbnail_fit is not UNSET:
            field_dict["thumbnail_fit"] = thumbnail_fit
        if show_score is not UNSET:
            field_dict["show_score"] = show_score
        if truncate_title is not UNSET:
            field_dict["truncate_title"] = truncate_title
        if truncate_description is not UNSET:
            field_dict["truncate_description"] = truncate_description
        if field_order is not UNSET:
            field_dict["field_order"] = field_order
        if show_find_similar is not UNSET:
            field_dict["show_find_similar"] = show_find_similar
        if card_click_action is not UNSET:
            field_dict["card_click_action"] = card_click_action
        if thumbnail_field is not UNSET:
            field_dict["thumbnail_field"] = thumbnail_field
        if title_field is not UNSET:
            field_dict["title_field"] = title_field
        if card_fields is not UNSET:
            field_dict["card_fields"] = card_fields
        if modal_fields is not UNSET:
            field_dict["modal_fields"] = modal_fields
        if card_style is not UNSET:
            field_dict["card_style"] = card_style

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        layout = d.pop("layout", UNSET)

        show_thumbnail = d.pop("show_thumbnail", UNSET)

        thumbnail_aspect_ratio = d.pop("thumbnail_aspect_ratio", UNSET)

        thumbnail_fit = d.pop("thumbnail_fit", UNSET)

        show_score = d.pop("show_score", UNSET)

        def _parse_truncate_title(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        truncate_title = _parse_truncate_title(d.pop("truncate_title", UNSET))

        def _parse_truncate_description(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        truncate_description = _parse_truncate_description(d.pop("truncate_description", UNSET))

        field_order = cast(list[str], d.pop("field_order", UNSET))

        show_find_similar = d.pop("show_find_similar", UNSET)

        card_click_action = d.pop("card_click_action", UNSET)

        def _parse_thumbnail_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_field = _parse_thumbnail_field(d.pop("thumbnail_field", UNSET))

        def _parse_title_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_field = _parse_title_field(d.pop("title_field", UNSET))

        def _parse_card_fields(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                card_fields_type_0 = cast(list[str], data)

                return card_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        card_fields = _parse_card_fields(d.pop("card_fields", UNSET))

        def _parse_modal_fields(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                modal_fields_type_0 = cast(list[str], data)

                return modal_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        modal_fields = _parse_modal_fields(d.pop("modal_fields", UNSET))

        def _parse_card_style(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        card_style = _parse_card_style(d.pop("card_style", UNSET))

        result_card_properties = cls(
            layout=layout,
            show_thumbnail=show_thumbnail,
            thumbnail_aspect_ratio=thumbnail_aspect_ratio,
            thumbnail_fit=thumbnail_fit,
            show_score=show_score,
            truncate_title=truncate_title,
            truncate_description=truncate_description,
            field_order=field_order,
            show_find_similar=show_find_similar,
            card_click_action=card_click_action,
            thumbnail_field=thumbnail_field,
            title_field=title_field,
            card_fields=card_fields,
            modal_fields=modal_fields,
            card_style=card_style,
        )

        result_card_properties.additional_properties = d
        return result_card_properties

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
