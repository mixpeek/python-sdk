from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.structured_data_config import StructuredDataConfig


T = TypeVar("T", bound="SEOConfig")


@_attrs_define
class SEOConfig:
    """SEO configuration for public retriever discoverability.

    Auto-generated during publishing with sensible defaults inferred from
    the retriever's display_config. All fields can be overridden manually.

    This configuration controls how the public retriever appears in:
    - Search engine results (Google, Bing, etc.)
    - Social media shares (Twitter, Facebook, LinkedIn)
    - Link previews in messaging apps

        Attributes:
            meta_title (None | str | Unset): SEO-optimized page title (50-60 chars recommended). Auto-generated from
                display_config.title + site_name if not provided.
            meta_description (None | str | Unset): Meta description for search engine snippets (max 160 chars). Auto-
                generated from display_config.description if not provided.
            keywords (list[str] | Unset): Relevant keywords for search engines. Auto-inferred from title, description, and
                retriever tags.
            og_image_url (None | str | Unset): URL to OG image for social previews (1200x630px recommended). Auto-generated
                and uploaded to public S3 bucket during publishing.
            og_image_alt (None | str | Unset): Alt text for OG image (accessibility and SEO)
            og_type (str | Unset): Open Graph content type Default: 'website'.
            twitter_card (str | Unset): Twitter card display style Default: 'summary_large_image'.
            twitter_site (None | str | Unset): Twitter @handle for the site Default: '@mixpeek'.
            twitter_creator (None | str | Unset): Twitter @handle for content creator (optional)
            robots (str | Unset): Robots meta directive for search engine crawlers. Use 'noindex, nofollow' to hide from
                search engines. Default: 'index, follow'.
            canonical_url (None | str | Unset): Canonical URL if different from default. Auto-set to
                https://apps.mixpeek.com/r/{public_name} if not provided.
            site_name (str | Unset): Site name for OG tags and branding Default: 'Mixpeek'.
            author (None | str | Unset): Content author/creator name
            locale (str | Unset): Content language/locale Default: 'en_US'.
            logo_url (None | str | Unset): URL to organization/brand logo for SEO and branding. Used in structured data and
                can be displayed in search results.
            favicon_url (None | str | Unset): URL to favicon/icon for the public retriever page. Recommended sizes: 32x32,
                48x48, or 180x180 for Apple touch icon.
            structured_data (StructuredDataConfig | Unset): Schema.org structured data configuration for search engines.

                Enables rich search results and better understanding of the page content.
    """

    meta_title: None | str | Unset = UNSET
    meta_description: None | str | Unset = UNSET
    keywords: list[str] | Unset = UNSET
    og_image_url: None | str | Unset = UNSET
    og_image_alt: None | str | Unset = UNSET
    og_type: str | Unset = "website"
    twitter_card: str | Unset = "summary_large_image"
    twitter_site: None | str | Unset = "@mixpeek"
    twitter_creator: None | str | Unset = UNSET
    robots: str | Unset = "index, follow"
    canonical_url: None | str | Unset = UNSET
    site_name: str | Unset = "Mixpeek"
    author: None | str | Unset = UNSET
    locale: str | Unset = "en_US"
    logo_url: None | str | Unset = UNSET
    favicon_url: None | str | Unset = UNSET
    structured_data: StructuredDataConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta_title: None | str | Unset
        if isinstance(self.meta_title, Unset):
            meta_title = UNSET
        else:
            meta_title = self.meta_title

        meta_description: None | str | Unset
        if isinstance(self.meta_description, Unset):
            meta_description = UNSET
        else:
            meta_description = self.meta_description

        keywords: list[str] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        og_image_url: None | str | Unset
        if isinstance(self.og_image_url, Unset):
            og_image_url = UNSET
        else:
            og_image_url = self.og_image_url

        og_image_alt: None | str | Unset
        if isinstance(self.og_image_alt, Unset):
            og_image_alt = UNSET
        else:
            og_image_alt = self.og_image_alt

        og_type = self.og_type

        twitter_card = self.twitter_card

        twitter_site: None | str | Unset
        if isinstance(self.twitter_site, Unset):
            twitter_site = UNSET
        else:
            twitter_site = self.twitter_site

        twitter_creator: None | str | Unset
        if isinstance(self.twitter_creator, Unset):
            twitter_creator = UNSET
        else:
            twitter_creator = self.twitter_creator

        robots = self.robots

        canonical_url: None | str | Unset
        if isinstance(self.canonical_url, Unset):
            canonical_url = UNSET
        else:
            canonical_url = self.canonical_url

        site_name = self.site_name

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        locale = self.locale

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        favicon_url: None | str | Unset
        if isinstance(self.favicon_url, Unset):
            favicon_url = UNSET
        else:
            favicon_url = self.favicon_url

        structured_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.structured_data, Unset):
            structured_data = self.structured_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta_title is not UNSET:
            field_dict["meta_title"] = meta_title
        if meta_description is not UNSET:
            field_dict["meta_description"] = meta_description
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if og_image_url is not UNSET:
            field_dict["og_image_url"] = og_image_url
        if og_image_alt is not UNSET:
            field_dict["og_image_alt"] = og_image_alt
        if og_type is not UNSET:
            field_dict["og_type"] = og_type
        if twitter_card is not UNSET:
            field_dict["twitter_card"] = twitter_card
        if twitter_site is not UNSET:
            field_dict["twitter_site"] = twitter_site
        if twitter_creator is not UNSET:
            field_dict["twitter_creator"] = twitter_creator
        if robots is not UNSET:
            field_dict["robots"] = robots
        if canonical_url is not UNSET:
            field_dict["canonical_url"] = canonical_url
        if site_name is not UNSET:
            field_dict["site_name"] = site_name
        if author is not UNSET:
            field_dict["author"] = author
        if locale is not UNSET:
            field_dict["locale"] = locale
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if favicon_url is not UNSET:
            field_dict["favicon_url"] = favicon_url
        if structured_data is not UNSET:
            field_dict["structured_data"] = structured_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structured_data_config import StructuredDataConfig

        d = dict(src_dict)

        def _parse_meta_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meta_title = _parse_meta_title(d.pop("meta_title", UNSET))

        def _parse_meta_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meta_description = _parse_meta_description(d.pop("meta_description", UNSET))

        keywords = cast(list[str], d.pop("keywords", UNSET))

        def _parse_og_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        og_image_url = _parse_og_image_url(d.pop("og_image_url", UNSET))

        def _parse_og_image_alt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        og_image_alt = _parse_og_image_alt(d.pop("og_image_alt", UNSET))

        og_type = d.pop("og_type", UNSET)

        twitter_card = d.pop("twitter_card", UNSET)

        def _parse_twitter_site(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        twitter_site = _parse_twitter_site(d.pop("twitter_site", UNSET))

        def _parse_twitter_creator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        twitter_creator = _parse_twitter_creator(d.pop("twitter_creator", UNSET))

        robots = d.pop("robots", UNSET)

        def _parse_canonical_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        canonical_url = _parse_canonical_url(d.pop("canonical_url", UNSET))

        site_name = d.pop("site_name", UNSET)

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        locale = d.pop("locale", UNSET)

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        def _parse_favicon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        favicon_url = _parse_favicon_url(d.pop("favicon_url", UNSET))

        _structured_data = d.pop("structured_data", UNSET)
        structured_data: StructuredDataConfig | Unset
        if isinstance(_structured_data, Unset):
            structured_data = UNSET
        else:
            structured_data = StructuredDataConfig.from_dict(_structured_data)

        seo_config = cls(
            meta_title=meta_title,
            meta_description=meta_description,
            keywords=keywords,
            og_image_url=og_image_url,
            og_image_alt=og_image_alt,
            og_type=og_type,
            twitter_card=twitter_card,
            twitter_site=twitter_site,
            twitter_creator=twitter_creator,
            robots=robots,
            canonical_url=canonical_url,
            site_name=site_name,
            author=author,
            locale=locale,
            logo_url=logo_url,
            favicon_url=favicon_url,
            structured_data=structured_data,
        )

        seo_config.additional_properties = d
        return seo_config

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
