"""Core Python dataclasses for OGM Aardvark resources and distributions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

AardvarkJson = dict[str, Any]


REPEATABLE_STRING_FIELDS: list[str] = [
    "dct_alternative_sm",
    "dct_description_sm",
    "dct_language_sm",
    "gbl_displayNote_sm",
    "dct_creator_sm",
    "dct_publisher_sm",
    "gbl_resourceClass_sm",
    "gbl_resourceType_sm",
    "dct_subject_sm",
    "dcat_theme_sm",
    "dcat_keyword_sm",
    "dct_temporal_sm",
    "gbl_dateRange_drsim",
    "dct_spatial_sm",
    "dct_identifier_sm",
    "dct_rights_sm",
    "dct_rightsHolder_sm",
    "dct_license_sm",
    "pcdm_memberOf_sm",
    "dct_isPartOf_sm",
    "dct_source_sm",
    "dct_isVersionOf_sm",
    "dct_replaces_sm",
    "dct_isReplacedBy_sm",
    "dct_relation_sm",
]

REPEATABLE_INT_FIELDS: list[str] = [
    "gbl_indexYear_im",
]

SCALAR_FIELDS: list[str] = [
    "id",
    "dct_title_s",
    "dct_accessRights_s",
    "dct_format_s",
    "gbl_mdVersion_s",
    "schema_provider_s",
    "dct_issued_s",
    "dcat_bbox",
    "locn_geometry",
    "dcat_centroid",
    "gbl_georeferenced_b",
    "gbl_wxsIdentifier_s",
    "gbl_suppressed_b",
    "gbl_fileSize_s",
    "dct_references_s",
    "gbl_mdModified_dt",
]

CSV_HEADER_MAPPING: dict[str, str] = {
    "Title": "dct_title_s",
    "Alternative Title": "dct_alternative_sm",
    "Description": "dct_description_sm",
    "Language": "dct_language_sm",
    "Display Note": "gbl_displayNote_sm",
    "Creator": "dct_creator_sm",
    "Publisher": "dct_publisher_sm",
    "Provider": "schema_provider_s",
    "Resource Class": "gbl_resourceClass_sm",
    "Resource Type": "gbl_resourceType_sm",
    "Subject": "dct_subject_sm",
    "Theme": "dcat_theme_sm",
    "Keyword": "dcat_keyword_sm",
    "Temporal Coverage": "dct_temporal_sm",
    "Date Issued": "dct_issued_s",
    "Index Year": "gbl_indexYear_im",
    "Date Range": "gbl_dateRange_drsim",
    "Spatial Coverage": "dct_spatial_sm",
    "Geometry": "locn_geometry",
    "Bounding Box": "dcat_bbox",
    "Centroid": "dcat_centroid",
    "Georeferenced": "gbl_georeferenced_b",
    "Relation": "dct_relation_sm",
    "Member Of": "pcdm_memberOf_sm",
    "Is Part Of": "dct_isPartOf_sm",
    "Source": "dct_source_sm",
    "Is Version Of": "dct_isVersionOf_sm",
    "Replaces": "dct_replaces_sm",
    "Is Replaced By": "dct_isReplacedBy_sm",
    "Rights": "dct_rights_sm",
    "Rights Holder": "dct_rightsHolder_sm",
    "License": "dct_license_sm",
    "Access Rights": "dct_accessRights_s",
    "Format": "dct_format_s",
    "File Size": "gbl_fileSize_s",
    "WxS Identifier": "gbl_wxsIdentifier_s",
    "ID": "id",
    "Identifier": "dct_identifier_sm",
    "Suppressed": "gbl_suppressed_b",
}

REFERENCE_URI_MAPPING: dict[str, str] = {
    # Services
    "wms": "http://www.opengis.net/def/serviceType/ogc/wms",
    "wfs": "http://www.opengis.net/def/serviceType/ogc/wfs",
    "wcs": "http://www.opengis.net/def/serviceType/ogc/wcs",
    "wmts": "http://www.opengis.net/def/serviceType/ogc/wmts",
    "tile_map_service": "https://wiki.osgeo.org/wiki/Tile_Map_Service_Specification",
    "tms": "https://wiki.osgeo.org/wiki/Tile_Map_Service_Specification",
    "xyz_tiles": "https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames",
    # Downloads
    "download": "http://schema.org/downloadUrl",
    "file": "http://schema.org/downloadUrl",
    # Information / Metadata
    "documentation": "http://schema.org/url",
    "url": "http://schema.org/url",
    "metadata": "http://www.isotc211.org/schemas/2005/gmd/",
    "ai_enrichments": "https://opengeometadata.org/reference/ai-enrichments",
    "ai-enrichments": "https://opengeometadata.org/reference/ai-enrichments",
    "fgdc": "http://www.opengis.net/cat/csw/csdgm",
    "mods": "http://www.loc.gov/mods/v3",
    "html": "http://www.w3.org/1999/xhtml",
    # Manifests
    "iiif": "http://iiif.io/api/image",
    "iiif_presentation": "http://iiif.io/api/presentation#manifest",
    "iiif_manifest": "http://iiif.io/api/presentation#manifest",
    "oembed": "https://oembed.com",
    # Esri
    "feature_layer": "urn:x-esri:serviceType:ArcGIS#FeatureLayer",
    "tiled_map_layer": "urn:x-esri:serviceType:ArcGIS#TiledMapLayer",
    "dynamic_map_layer": "urn:x-esri:serviceType:ArcGIS#DynamicMapLayer",
    "image_map_layer": "urn:x-esri:serviceType:ArcGIS#ImageMapLayer",
}

REQUIRED_FIELDS: list[str] = [
    "id",
    "dct_title_s",
    "gbl_resourceClass_sm",
    "dct_accessRights_s",
    "gbl_mdVersion_s",
]


def _ensure_md_version(data: AardvarkJson) -> None:
    if data.get("gbl_mdVersion_s") != "Aardvark":
        data["gbl_mdVersion_s"] = "Aardvark"


def _string_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def _int_list(value: Any) -> list[int]:
    if value is None:
        return []
    if isinstance(value, list):
        return [int(item) for item in value]
    return [int(value)]


@dataclass
class Resource:
    # Required
    id: str
    dct_title_s: str
    gbl_resourceClass_sm: list[str]
    dct_accessRights_s: str
    gbl_mdVersion_s: str = "Aardvark"
    dct_format_s: str | None = None
    dct_references_s: str | None = None

    # Identification
    dct_alternative_sm: list[str] = field(default_factory=list)
    dct_description_sm: list[str] = field(default_factory=list)
    dct_language_sm: list[str] = field(default_factory=list)
    gbl_displayNote_sm: list[str] = field(default_factory=list)

    # Credits
    dct_creator_sm: list[str] = field(default_factory=list)
    dct_publisher_sm: list[str] = field(default_factory=list)
    schema_provider_s: str | None = None

    # Categories
    gbl_resourceType_sm: list[str] = field(default_factory=list)
    dct_subject_sm: list[str] = field(default_factory=list)
    dcat_theme_sm: list[str] = field(default_factory=list)
    dcat_keyword_sm: list[str] = field(default_factory=list)

    # Temporal
    dct_temporal_sm: list[str] = field(default_factory=list)
    dct_issued_s: str | None = None
    gbl_dateRange_drsim: list[str] = field(default_factory=list)
    gbl_indexYear_im: list[int] = field(default_factory=list)

    # Spatial
    dct_spatial_sm: list[str] = field(default_factory=list)
    dcat_bbox: str | None = None
    locn_geometry: str | None = None
    dcat_centroid: str | None = None
    gbl_georeferenced_b: bool | None = None

    # Administrative
    dct_identifier_sm: list[str] = field(default_factory=list)
    gbl_wxsIdentifier_s: str | None = None
    dct_rights_sm: list[str] = field(default_factory=list)
    dct_rightsHolder_sm: list[str] = field(default_factory=list)
    dct_license_sm: list[str] = field(default_factory=list)

    # Image Service
    thumbnail: str | None = None
    gbl_suppressed_b: bool | None = None

    # Object
    gbl_fileSize_s: str | None = None

    # Relations
    pcdm_memberOf_sm: list[str] = field(default_factory=list)
    dct_isPartOf_sm: list[str] = field(default_factory=list)
    dct_source_sm: list[str] = field(default_factory=list)
    dct_isVersionOf_sm: list[str] = field(default_factory=list)
    dct_replaces_sm: list[str] = field(default_factory=list)
    dct_isReplacedBy_sm: list[str] = field(default_factory=list)
    dct_relation_sm: list[str] = field(default_factory=list)

    # Bag for any unmodeled fields so we do not lose information.
    extra: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, raw: AardvarkJson) -> "Resource":
        data = dict(raw)
        _ensure_md_version(data)

        if not data.get("id"):
            raise ValueError("Missing required field: id")

        classes = _string_list(data.get("gbl_resourceClass_sm"))
        if not classes:
            classes = ["Other"]

        modeled_keys = (
            set(SCALAR_FIELDS)
            | set(REPEATABLE_STRING_FIELDS)
            | set(REPEATABLE_INT_FIELDS)
            | {"thumbnail"}
        )
        extra = {
            key: value
            for key, value in data.items()
            if key not in modeled_keys and key != "dct_references_s"
        }

        return cls(
            id=str(data["id"]),
            dct_title_s=str(data.get("dct_title_s") or "[Untitled]"),
            dct_accessRights_s=str(data.get("dct_accessRights_s") or "Public"),
            gbl_resourceClass_sm=classes,
            gbl_mdVersion_s=str(data.get("gbl_mdVersion_s") or "Aardvark"),
            dct_format_s=data.get("dct_format_s"),
            dct_references_s=data.get("dct_references_s"),
            dct_alternative_sm=_string_list(data.get("dct_alternative_sm")),
            dct_description_sm=_string_list(data.get("dct_description_sm")),
            dct_language_sm=_string_list(data.get("dct_language_sm")),
            gbl_displayNote_sm=_string_list(data.get("gbl_displayNote_sm")),
            dct_creator_sm=_string_list(data.get("dct_creator_sm")),
            dct_publisher_sm=_string_list(data.get("dct_publisher_sm")),
            schema_provider_s=data.get("schema_provider_s"),
            gbl_resourceType_sm=_string_list(data.get("gbl_resourceType_sm")),
            dct_subject_sm=_string_list(data.get("dct_subject_sm")),
            dcat_theme_sm=_string_list(data.get("dcat_theme_sm")),
            dcat_keyword_sm=_string_list(data.get("dcat_keyword_sm")),
            dct_temporal_sm=_string_list(data.get("dct_temporal_sm")),
            dct_issued_s=data.get("dct_issued_s"),
            gbl_indexYear_im=_int_list(data.get("gbl_indexYear_im")),
            gbl_dateRange_drsim=_string_list(data.get("gbl_dateRange_drsim")),
            dct_spatial_sm=_string_list(data.get("dct_spatial_sm")),
            dcat_bbox=data.get("dcat_bbox"),
            locn_geometry=data.get("locn_geometry"),
            dcat_centroid=data.get("dcat_centroid"),
            gbl_georeferenced_b=data.get("gbl_georeferenced_b"),
            dct_identifier_sm=_string_list(data.get("dct_identifier_sm")),
            gbl_wxsIdentifier_s=data.get("gbl_wxsIdentifier_s"),
            dct_rights_sm=_string_list(data.get("dct_rights_sm")),
            dct_rightsHolder_sm=_string_list(data.get("dct_rightsHolder_sm")),
            dct_license_sm=_string_list(data.get("dct_license_sm")),
            thumbnail=data.get("thumbnail"),
            gbl_suppressed_b=data.get("gbl_suppressed_b"),
            gbl_fileSize_s=data.get("gbl_fileSize_s"),
            pcdm_memberOf_sm=_string_list(data.get("pcdm_memberOf_sm")),
            dct_isPartOf_sm=_string_list(data.get("dct_isPartOf_sm")),
            dct_source_sm=_string_list(data.get("dct_source_sm")),
            dct_isVersionOf_sm=_string_list(data.get("dct_isVersionOf_sm")),
            dct_replaces_sm=_string_list(data.get("dct_replaces_sm")),
            dct_isReplacedBy_sm=_string_list(data.get("dct_isReplacedBy_sm")),
            dct_relation_sm=_string_list(data.get("dct_relation_sm")),
            extra=extra,
        )

    def to_json(self) -> AardvarkJson:
        data: AardvarkJson = {
            # Required
            "id": self.id,
            "dct_title_s": self.dct_title_s,
            "dct_accessRights_s": self.dct_accessRights_s,
            "gbl_resourceClass_sm": self.gbl_resourceClass_sm,
            "gbl_mdVersion_s": self.gbl_mdVersion_s,
            # Identification
            "dct_alternative_sm": self.dct_alternative_sm,
            "dct_description_sm": self.dct_description_sm,
            "dct_language_sm": self.dct_language_sm,
            "gbl_displayNote_sm": self.gbl_displayNote_sm,
            # Credits
            "dct_creator_sm": self.dct_creator_sm,
            "dct_publisher_sm": self.dct_publisher_sm,
            # Categories
            "gbl_resourceType_sm": self.gbl_resourceType_sm,
            "dct_subject_sm": self.dct_subject_sm,
            "dcat_theme_sm": self.dcat_theme_sm,
            "dcat_keyword_sm": self.dcat_keyword_sm,
            # Temporal
            "dct_temporal_sm": self.dct_temporal_sm,
            "gbl_indexYear_im": self.gbl_indexYear_im,
            "gbl_dateRange_drsim": self.gbl_dateRange_drsim,
            # Spatial
            "dct_spatial_sm": self.dct_spatial_sm,
            # Administrative
            "dct_identifier_sm": self.dct_identifier_sm,
            "dct_rights_sm": self.dct_rights_sm,
            "dct_rightsHolder_sm": self.dct_rightsHolder_sm,
            "dct_license_sm": self.dct_license_sm,
            # Relations
            "pcdm_memberOf_sm": self.pcdm_memberOf_sm,
            "dct_isPartOf_sm": self.dct_isPartOf_sm,
            "dct_source_sm": self.dct_source_sm,
            "dct_isVersionOf_sm": self.dct_isVersionOf_sm,
            "dct_replaces_sm": self.dct_replaces_sm,
            "dct_isReplacedBy_sm": self.dct_isReplacedBy_sm,
            "dct_relation_sm": self.dct_relation_sm,
        }

        optional_values: AardvarkJson = {
            "dct_format_s": self.dct_format_s,
            "schema_provider_s": self.schema_provider_s,
            "dct_issued_s": self.dct_issued_s,
            "dcat_bbox": self.dcat_bbox,
            "locn_geometry": self.locn_geometry,
            "dcat_centroid": self.dcat_centroid,
            "gbl_georeferenced_b": self.gbl_georeferenced_b,
            "gbl_wxsIdentifier_s": self.gbl_wxsIdentifier_s,
            "thumbnail": self.thumbnail,
            "gbl_suppressed_b": self.gbl_suppressed_b,
            "gbl_fileSize_s": self.gbl_fileSize_s,
            "dct_references_s": self.dct_references_s,
        }
        for key, value in optional_values.items():
            if value is not None and value != "":
                data[key] = value

        data.update(self.extra)
        _ensure_md_version(data)
        return data


@dataclass
class Distribution:
    resource_id: str
    relation_key: str
    url: str
    label: str | None = None


def resource_from_json(raw: AardvarkJson) -> Resource:
    return Resource.from_json(raw)


def resource_to_json(resource: Resource) -> AardvarkJson:
    return resource.to_json()
