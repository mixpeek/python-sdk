from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThemeConfig")


@_attrs_define
class ThemeConfig:
    """Theme configuration for public retriever UI.

    Defines colors, fonts, and visual styling for the public search interface.

        Attributes:
            primary_color (str | Unset): Primary brand color (hex code) Default: '#007AFF'.
            secondary_color (None | str | Unset): Secondary/accent color (hex code)
            font_family (str | Unset): Font family for text Default: 'system-ui, -apple-system, sans-serif'.
            background_color (str | Unset): Background color (hex code) Default: '#FFFFFF'.
            text_color (str | Unset): Primary text color (hex code) Default: '#374151'.
            heading_font_family (None | str | Unset): Optional separate font family for headings
            surface_color (None | str | Unset): Surface/card background color (hex code)
            muted_color (None | str | Unset): Muted/secondary text color (hex code)
            border_color (None | str | Unset): Border color for cards and elements (hex code)
            border_radius (None | str | Unset): Default border radius for cards and elements Default: '12px'.
            card_style (None | str | Unset): Card visual style: elevated (shadow), flat (no shadow), bordered, or glass
                (frosted glass effect) Default: 'elevated'.
            card_hover_effect (None | str | Unset): Card hover animation effect: lift (move up), glow, scale, or none
                Default: 'lift'.
    """

    primary_color: str | Unset = "#007AFF"
    secondary_color: None | str | Unset = UNSET
    font_family: str | Unset = "system-ui, -apple-system, sans-serif"
    background_color: str | Unset = "#FFFFFF"
    text_color: str | Unset = "#374151"
    heading_font_family: None | str | Unset = UNSET
    surface_color: None | str | Unset = UNSET
    muted_color: None | str | Unset = UNSET
    border_color: None | str | Unset = UNSET
    border_radius: None | str | Unset = "12px"
    card_style: None | str | Unset = "elevated"
    card_hover_effect: None | str | Unset = "lift"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        primary_color = self.primary_color

        secondary_color: None | str | Unset
        if isinstance(self.secondary_color, Unset):
            secondary_color = UNSET
        else:
            secondary_color = self.secondary_color

        font_family = self.font_family

        background_color = self.background_color

        text_color = self.text_color

        heading_font_family: None | str | Unset
        if isinstance(self.heading_font_family, Unset):
            heading_font_family = UNSET
        else:
            heading_font_family = self.heading_font_family

        surface_color: None | str | Unset
        if isinstance(self.surface_color, Unset):
            surface_color = UNSET
        else:
            surface_color = self.surface_color

        muted_color: None | str | Unset
        if isinstance(self.muted_color, Unset):
            muted_color = UNSET
        else:
            muted_color = self.muted_color

        border_color: None | str | Unset
        if isinstance(self.border_color, Unset):
            border_color = UNSET
        else:
            border_color = self.border_color

        border_radius: None | str | Unset
        if isinstance(self.border_radius, Unset):
            border_radius = UNSET
        else:
            border_radius = self.border_radius

        card_style: None | str | Unset
        if isinstance(self.card_style, Unset):
            card_style = UNSET
        else:
            card_style = self.card_style

        card_hover_effect: None | str | Unset
        if isinstance(self.card_hover_effect, Unset):
            card_hover_effect = UNSET
        else:
            card_hover_effect = self.card_hover_effect

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary_color is not UNSET:
            field_dict["primary_color"] = primary_color
        if secondary_color is not UNSET:
            field_dict["secondary_color"] = secondary_color
        if font_family is not UNSET:
            field_dict["font_family"] = font_family
        if background_color is not UNSET:
            field_dict["background_color"] = background_color
        if text_color is not UNSET:
            field_dict["text_color"] = text_color
        if heading_font_family is not UNSET:
            field_dict["heading_font_family"] = heading_font_family
        if surface_color is not UNSET:
            field_dict["surface_color"] = surface_color
        if muted_color is not UNSET:
            field_dict["muted_color"] = muted_color
        if border_color is not UNSET:
            field_dict["border_color"] = border_color
        if border_radius is not UNSET:
            field_dict["border_radius"] = border_radius
        if card_style is not UNSET:
            field_dict["card_style"] = card_style
        if card_hover_effect is not UNSET:
            field_dict["card_hover_effect"] = card_hover_effect

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        primary_color = d.pop("primary_color", UNSET)

        def _parse_secondary_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secondary_color = _parse_secondary_color(d.pop("secondary_color", UNSET))

        font_family = d.pop("font_family", UNSET)

        background_color = d.pop("background_color", UNSET)

        text_color = d.pop("text_color", UNSET)

        def _parse_heading_font_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        heading_font_family = _parse_heading_font_family(d.pop("heading_font_family", UNSET))

        def _parse_surface_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        surface_color = _parse_surface_color(d.pop("surface_color", UNSET))

        def _parse_muted_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        muted_color = _parse_muted_color(d.pop("muted_color", UNSET))

        def _parse_border_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        border_color = _parse_border_color(d.pop("border_color", UNSET))

        def _parse_border_radius(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        border_radius = _parse_border_radius(d.pop("border_radius", UNSET))

        def _parse_card_style(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        card_style = _parse_card_style(d.pop("card_style", UNSET))

        def _parse_card_hover_effect(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        card_hover_effect = _parse_card_hover_effect(d.pop("card_hover_effect", UNSET))

        theme_config = cls(
            primary_color=primary_color,
            secondary_color=secondary_color,
            font_family=font_family,
            background_color=background_color,
            text_color=text_color,
            heading_font_family=heading_font_family,
            surface_color=surface_color,
            muted_color=muted_color,
            border_color=border_color,
            border_radius=border_radius,
            card_style=card_style,
            card_hover_effect=card_hover_effect,
        )

        theme_config.additional_properties = d
        return theme_config

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
