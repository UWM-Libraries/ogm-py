# Project Notes

## Metadata Authoring

- Before working on a project folder, read that project's `README.md` and follow any project-specific notes, source decisions, and relationship decisions documented there.
- Do not author or edit Solr/index-managed fields in source metadata for new records. Examples include `_version_`, `timestamp`, and `solr_bboxtype__minX` / `solr_bboxtype__minY` / `solr_bboxtype__maxX` / `solr_bboxtype__maxY`.
- Existing exported GeoBlacklight records may include those fields as examples, but 2025 source metadata should only track author-controlled Aardvark fields.
