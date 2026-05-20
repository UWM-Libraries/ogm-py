# OGM Python Metadata Workflow

Interactive Python and Jupyter workflows for preparing OpenGeoMetadata Aardvark metadata for AGSL GeoDiscovery.

Maybe it will be a library some day?

**Requirements**:

* Python 3
* Jupyter Notebook (https://jupyter.org/install)
* Pandas (https://pandas.pydata.org/getting_started.html)
* Numpy* (https://numpy.org/install/)

*only needed for `clean-validate`

## export-aardvark-json

* CSV template for OGM Aardvark metadata
* Jupyter Notebook that transforms a metadata CSV into OGM Aardvark JSON files

## clean-validate

* CSV of sample OGM Aardvark metadata that has missing or incorrect values
* Jupyter Notebook scans the metadata, fixes it, and produces a log of actions taken

## package-ingest

* Jupyter Notebook for packaging project files for ingest workflows


## metadata-profile

* `aardvark.csv`: Documentation of the OGM Aardvark profile
* `referenceURIs.csv`: Keys and values of the types of references specified in the OGM Aardvark profile and viewable with GeoBlacklight
