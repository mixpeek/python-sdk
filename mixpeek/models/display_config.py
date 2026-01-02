from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.components_config import ComponentsConfig
    from ..models.custom_cta import CustomCTA
    from ..models.display_config_extensions_type_0 import DisplayConfigExtensionsType0
    from ..models.display_config_field_config import DisplayConfigFieldConfig
    from ..models.display_config_field_mappings_type_0 import DisplayConfigFieldMappingsType0
    from ..models.input_rendering_config import InputRenderingConfig
    from ..models.layout_config import LayoutConfig
    from ..models.markdown_content import MarkdownContent
    from ..models.seo_config import SEOConfig
    from ..models.theme_config import ThemeConfig


T = TypeVar("T", bound="DisplayConfig")


@_attrs_define
class DisplayConfig:
    """Display configuration for public retriever UI.

    This model defines how the public search interface should be rendered,
    including input fields, theme, layout, and result card configuration.

    The frontend (apps.mixpeek.com) uses this to dynamically build the UI
    without hardcoded components.

        Attributes:
            title (str): Title/heading for the public search page
            inputs (list[InputRenderingConfig]): List of input fields to render in the search interface. Each input maps to
                a field in the retriever's input_schema. Frontend uses the field_schema to render the appropriate component
                type.
            exposed_fields (list[str]): List of document metadata fields to show in results. Only these fields are returned
                to end users.
            description (None | str | Unset): Optional description/subtitle for the page
            logo_url (None | str | Unset): URL to logo image
            seo (None | SEOConfig | Unset): SEO configuration for search engine and social media discoverability. Auto-
                generated during publishing with sensible defaults inferred from title, description, and retriever metadata. All
                fields can be overridden.
            markdowns (list[MarkdownContent] | Unset): Array of markdown content sections for documentation, guides, or
                informational modals. Each section has a title and markdown-formatted content. Displayed in modals, expandable
                sections, or tabs on the public interface. Examples: 'How it Works', 'Search Guide', 'About', 'FAQ', etc.
            theme (ThemeConfig | Unset): Theme configuration for public retriever UI.

                Defines colors, fonts, and visual styling for the public search interface.
            layout (LayoutConfig | Unset): Layout configuration for search results display.
            components (ComponentsConfig | Unset): Configuration for UI components.
            field_config (DisplayConfigFieldConfig | Unset): Configuration for how each field should be displayed. Keys are
                field names (must be subset of exposed_fields). Values are FieldConfig objects specifying format and display
                options.
            custom_cta (CustomCTA | None | Unset): Optional custom call-to-action button displayed in the header bar. Opens
                a markdown modal when clicked.
            template_type (None | str | Unset): Template identifier for frontend rendering. Built-in templates: portrait-
                gallery, media-search, document-search. Custom templates can use any string identifier.
            field_mappings (DisplayConfigFieldMappingsType0 | None | Unset): Field mappings from collection output fields to
                template display slots. Maps template slot names (e.g., 'thumbnail', 'title') to actual field names in the
                search results.
            extensions (DisplayConfigExtensionsType0 | None | Unset): Generic extensions for template-specific
                configuration. Allows templates to store custom config without schema changes.
    """

    title: str
    inputs: list[InputRenderingConfig]
    exposed_fields: list[str]
    description: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    seo: None | SEOConfig | Unset = UNSET
    markdowns: list[MarkdownContent] | Unset = UNSET
    theme: ThemeConfig | Unset = UNSET
    layout: LayoutConfig | Unset = UNSET
    components: ComponentsConfig | Unset = UNSET
    field_config: DisplayConfigFieldConfig | Unset = UNSET
    custom_cta: CustomCTA | None | Unset = UNSET
    template_type: None | str | Unset = UNSET
    field_mappings: DisplayConfigFieldMappingsType0 | None | Unset = UNSET
    extensions: DisplayConfigExtensionsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_cta import CustomCTA
        from ..models.display_config_extensions_type_0 import DisplayConfigExtensionsType0
        from ..models.display_config_field_mappings_type_0 import DisplayConfigFieldMappingsType0
        from ..models.seo_config import SEOConfig

        title = self.title

        inputs = []
        for inputs_item_data in self.inputs:
            inputs_item = inputs_item_data.to_dict()
            inputs.append(inputs_item)

        exposed_fields = self.exposed_fields

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        seo: dict[str, Any] | None | Unset
        if isinstance(self.seo, Unset):
            seo = UNSET
        elif isinstance(self.seo, SEOConfig):
            seo = self.seo.to_dict()
        else:
            seo = self.seo

        markdowns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.markdowns, Unset):
            markdowns = []
            for markdowns_item_data in self.markdowns:
                markdowns_item = markdowns_item_data.to_dict()
                markdowns.append(markdowns_item)

        theme: dict[str, Any] | Unset = UNSET
        if not isinstance(self.theme, Unset):
            theme = self.theme.to_dict()

        layout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.layout, Unset):
            layout = self.layout.to_dict()

        components: dict[str, Any] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = self.components.to_dict()

        field_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_config, Unset):
            field_config = self.field_config.to_dict()

        custom_cta: dict[str, Any] | None | Unset
        if isinstance(self.custom_cta, Unset):
            custom_cta = UNSET
        elif isinstance(self.custom_cta, CustomCTA):
            custom_cta = self.custom_cta.to_dict()
        else:
            custom_cta = self.custom_cta

        template_type: None | str | Unset
        if isinstance(self.template_type, Unset):
            template_type = UNSET
        else:
            template_type = self.template_type

        field_mappings: dict[str, Any] | None | Unset
        if isinstance(self.field_mappings, Unset):
            field_mappings = UNSET
        elif isinstance(self.field_mappings, DisplayConfigFieldMappingsType0):
            field_mappings = self.field_mappings.to_dict()
        else:
            field_mappings = self.field_mappings

        extensions: dict[str, Any] | None | Unset
        if isinstance(self.extensions, Unset):
            extensions = UNSET
        elif isinstance(self.extensions, DisplayConfigExtensionsType0):
            extensions = self.extensions.to_dict()
        else:
            extensions = self.extensions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "inputs": inputs,
                "exposed_fields": exposed_fields,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if seo is not UNSET:
            field_dict["seo"] = seo
        if markdowns is not UNSET:
            field_dict["markdowns"] = markdowns
        if theme is not UNSET:
            field_dict["theme"] = theme
        if layout is not UNSET:
            field_dict["layout"] = layout
        if components is not UNSET:
            field_dict["components"] = components
        if field_config is not UNSET:
            field_dict["field_config"] = field_config
        if custom_cta is not UNSET:
            field_dict["custom_cta"] = custom_cta
        if template_type is not UNSET:
            field_dict["template_type"] = template_type
        if field_mappings is not UNSET:
            field_dict["field_mappings"] = field_mappings
        if extensions is not UNSET:
            field_dict["extensions"] = extensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.components_config import ComponentsConfig
        from ..models.custom_cta import CustomCTA
        from ..models.display_config_extensions_type_0 import DisplayConfigExtensionsType0
        from ..models.display_config_field_config import DisplayConfigFieldConfig
        from ..models.display_config_field_mappings_type_0 import DisplayConfigFieldMappingsType0
        from ..models.input_rendering_config import InputRenderingConfig
        from ..models.layout_config import LayoutConfig
        from ..models.markdown_content import MarkdownContent
        from ..models.seo_config import SEOConfig
        from ..models.theme_config import ThemeConfig

        d = dict(src_dict)
        title = d.pop("title")

        inputs = []
        _inputs = d.pop("inputs")
        for inputs_item_data in _inputs:
            inputs_item = InputRenderingConfig.from_dict(inputs_item_data)

            inputs.append(inputs_item)

        exposed_fields = cast(list[str], d.pop("exposed_fields"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        def _parse_seo(data: object) -> None | SEOConfig | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                seo_type_0 = SEOConfig.from_dict(data)

                return seo_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SEOConfig | Unset, data)

        seo = _parse_seo(d.pop("seo", UNSET))

        _markdowns = d.pop("markdowns", UNSET)
        markdowns: list[MarkdownContent] | Unset = UNSET
        if _markdowns is not UNSET:
            markdowns = []
            for markdowns_item_data in _markdowns:
                markdowns_item = MarkdownContent.from_dict(markdowns_item_data)

                markdowns.append(markdowns_item)

        _theme = d.pop("theme", UNSET)
        theme: ThemeConfig | Unset
        if isinstance(_theme, Unset):
            theme = UNSET
        else:
            theme = ThemeConfig.from_dict(_theme)

        _layout = d.pop("layout", UNSET)
        layout: LayoutConfig | Unset
        if isinstance(_layout, Unset):
            layout = UNSET
        else:
            layout = LayoutConfig.from_dict(_layout)

        _components = d.pop("components", UNSET)
        components: ComponentsConfig | Unset
        if isinstance(_components, Unset):
            components = UNSET
        else:
            components = ComponentsConfig.from_dict(_components)

        _field_config = d.pop("field_config", UNSET)
        field_config: DisplayConfigFieldConfig | Unset
        if isinstance(_field_config, Unset):
            field_config = UNSET
        else:
            field_config = DisplayConfigFieldConfig.from_dict(_field_config)

        def _parse_custom_cta(data: object) -> CustomCTA | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_cta_type_0 = CustomCTA.from_dict(data)

                return custom_cta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomCTA | None | Unset, data)

        custom_cta = _parse_custom_cta(d.pop("custom_cta", UNSET))

        def _parse_template_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_type = _parse_template_type(d.pop("template_type", UNSET))

        def _parse_field_mappings(data: object) -> DisplayConfigFieldMappingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_mappings_type_0 = DisplayConfigFieldMappingsType0.from_dict(data)

                return field_mappings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DisplayConfigFieldMappingsType0 | None | Unset, data)

        field_mappings = _parse_field_mappings(d.pop("field_mappings", UNSET))

        def _parse_extensions(data: object) -> DisplayConfigExtensionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extensions_type_0 = DisplayConfigExtensionsType0.from_dict(data)

                return extensions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DisplayConfigExtensionsType0 | None | Unset, data)

        extensions = _parse_extensions(d.pop("extensions", UNSET))

        display_config = cls(
            title=title,
            inputs=inputs,
            exposed_fields=exposed_fields,
            description=description,
            logo_url=logo_url,
            seo=seo,
            markdowns=markdowns,
            theme=theme,
            layout=layout,
            components=components,
            field_config=field_config,
            custom_cta=custom_cta,
            template_type=template_type,
            field_mappings=field_mappings,
            extensions=extensions,
        )

        display_config.additional_properties = d
        return display_config

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
