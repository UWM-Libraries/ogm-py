# OGM Python Metadata Workflow

Interactive Python and Jupyter workflows for preparing OpenGeoMetadata Aardvark metadata for AGSL GeoDiscovery.

Maybe it will be a library some day?

**Requirements**:

* mise
* Python 3.12
* Jupyter Notebook (https://jupyter.org/install)
* Pandas (https://pandas.pydata.org/getting_started.html)
* Numpy* (https://numpy.org/install/)

*only needed for `clean-validate`

## Environment

This repo uses `mise` to pin the Python version and a local `.venv` for dependencies.

```bash
mise install
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name ogm-py --display-name "Python (ogm-py)"
```

## export-aardvark-json

* CSV template for OGM Aardvark metadata
* Jupyter Notebook that transforms a metadata CSV into OGM Aardvark JSON files

## clean-validate

* CSV of sample OGM Aardvark metadata that has missing or incorrect values
* Jupyter Notebook scans the metadata, fixes it, and produces a log of actions taken

## metadata-profile

* `aardvark.csv`: Documentation of the OGM Aardvark profile
* `referenceURIs.csv`: Keys and values of the types of references specified in the OGM Aardvark profile and viewable with GeoBlacklight

## archive

* `archive/cuba-census`: Older Cuba Census ingest packaging notebook retained for reference.
