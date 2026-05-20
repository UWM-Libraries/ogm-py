# DYCU 2025

Project workspace for preparing the Data You Can Use 2025 MKE Indicators update for GeoDiscovery and OpenGeoMetadata.

Source page: [MKE Indicators | Data, Resources, Archives](https://datayoucanuse.org/mke-indicators-archive/data-resources-archives/)

- `json_output/`: Exported OpenGeoMetadata Aardvark JSON records.
- `existing_records`: Exported example records from previous ingest.
- `README.md`: Project notes, source decisions, and mappings to prior 2020 or 2024 records.

## Existing GeoBlacklight Examples

| Role | GeoBlacklight record | ID | Local example file |
| --- | --- | --- | --- |
| 2020 collection | [Data You Can Use MKE Indicators Milwaukee, Wisconsin 2020](https://geodiscovery.uwm.edu/catalog/ark:-77981-gmgsvt4bc1t) | `ark:-77981-gmgsvt4bc1t` | `existing_records/gmgsvt4bc1t.json` |
| 2020 dataset example | [Access to Work Milwaukee, Wisconsin 2012-2016](https://geodiscovery.uwm.edu/catalog/ark:-77981-gmgshdr7v8s) | `ark:-77981-gmgshdr7v8s` | `existing_records/gmgshdr7v8s.json` |
| 2024 collection | [Data You Can Use MKE Indicators Milwaukee, Wisconsin 2024](https://geodiscovery.uwm.edu/catalog/ark:-77981-gmgswdbrxmc) | `ark:-77981-gmgswdbrxmc` | `existing_records/gmgswdbrxmc.json` |
| 2024 subcollection | [Data You Can Use Equitable Housing MKE Indicators Milwaukee, Wisconsin 2024](https://geodiscovery.uwm.edu/catalog/ark:-77981-gmgs4f4qrxn) | `ark:-77981-gmgs4f4qrxn` | `existing_records/gmgs4f4qrxn.json` |
| 2024 dataset example | [Black Homeownership Milwaukee, Wisconsin 2018-2022](https://geodiscovery.uwm.edu/catalog/ark:-77981-gmgsvx0k8z0) | `ark:-77981-gmgsvx0k8z0` | `existing_records/gmgsvx0k8z0.json` |

## Access To Healthy Food Change

The 2025 Access to Healthy Food indicator should not be treated as directly comparable to earlier MKE Indicators releases. Data You Can Use notes that previous releases measured Access to Healthy Food using a USDA-based measure, while the 2025 update switches to CDC PLACES data and measures food access as the prevalence of adults age 18 and older who report food insecurity in the past 12 months.

This matters for metadata because the title may look continuous across releases, but the underlying source and measure changed. The 2025 record description should include a clear comparability note, and any relationship to 2020 or 2024 Healthy Food records should be framed as topical continuity rather than a like-for-like time series.

CDC PLACES health-related social needs data include food insecurity among several modeled measures. CDC describes PLACES estimates as using small area estimation methods, including multilevel regression and poststratification, to support local geographies where direct survey sample sizes may be too small. Sources: [Data You Can Use 2025 Update Data](https://datayoucanuse.org/mke-indicators-archive/data-resources-archives/), [CDC PLACES Health-Related Social Needs](https://www.cdc.gov/places/measure-definitions/health-related-social-needs.html), and [CDC PLACES FAQ](https://www.cdc.gov/places/faqs/index.html).

## 2025 Dataset Inventory

| Category | Indicator | Basic measure | Data download |
| --- | --- | --- | --- |
| Equitable Housing | Latinx Homeownership | Rate of homeownership by Hispanic / Latino individuals | [Latinx-Hispanic-Homeownership-2023.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Latinx-Hispanic-Homeownership-2023.xlsx) |
| Equitable Housing | Black / African American Homeownership | Rate of homeownership by Black / African American individuals | [Black-African-American-Homeownership-2023.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Black-African-American-Homeownership-2023.xlsx) |
| Equitable Housing | Rental Housing Cost Burden | Percent of occupied rental units paying 30% or more of income on rent | [Rental-Burden-2023.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Rental-Burden-2023.xlsx) |
| Equitable Housing | Access to Broadband Internet | Percent of households with an internet subscription | [Broadband-Access-2023.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Broadband-Access-2023.xlsx) |
| Equitable Housing | Access to Healthy Food | Prevalence of adults age 18+ reporting food insecurity in the past 12 months | [Food-Insecurity-2022.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Food-Insecurity-2022.xlsx) |
| Population | Black / African American Population | Percent of Black / African American residents | [Black-African-American-Population-2023.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Black-African-American-Population-2023.xlsx) |
| Population | Asian Population | Percent of Asian residents | [Asian-Population-2023.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Asian-Population-2023.xlsx) |
| Population | Latinx Population | Percent of Latinx / Hispanic residents | [Latinx-Hispanic-Population-2023.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Latinx-Hispanic-Population-2023.xlsx) |
| Population | White Population | Percent of White residents | [White-Population-2023.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/White-Population-2023.xlsx) |
| Market Value | Vacancy Rate | Percent of housing units that are vacant | [Vacancy-2023.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Vacancy-2023.xlsx) |
| Market Value | Homeownership | Percent of occupied housing units that are owner-occupied | [Homeownership-2023.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Homeownership-2023.xlsx) |
| Equity & Access | Access to Basic Needs | Percent of households below poverty level | [Poverty-2023.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Poverty-2023.xlsx) |
| Equity & Access | Access to Employment | Travel time to work | [Travel-Time-to-Work-2023.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Travel-Time-to-Work-2023.xlsx) |
| Equity & Access | Diversity Index | Racial diversity measure using a modified Simpson's Diversity Index | [Racial-Diversity-2023.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Racial-Diversity-2023.xlsx) |
| Health | Housing Units Built Prior to 1950 | Percent of housing units built before 1950 | [Units-Built-Before-1950-2023.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Units-Built-Before-1950-2023.xlsx) |
| Health | Asthma | Asthma prevalence among adults age 18+ | [Asthma-2022.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Asthma-2022.xlsx) |
| Health | Obesity | Obesity prevalence among adults age 18+ | [Obesity-2022.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Obesity-2022.xlsx) |
| Health | Mental Health | Prevalence of adults age 18+ reporting 14 or more poor mental health days | [Mental-Health-2022.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Mental-Health-2022.xlsx) |
| Health | Visits to Dentist or Dental Clinic | Prevalence of adults age 18+ reporting a dental visit in the last year | [Dental-Visits-2022.xlsx](https://datayoucanuse.org/wp-content/uploads/2025/03/Dental-Visits-2022.xlsx) |

## Proposed Collection Structure

Model the 2025 release as one top-level collection, five category subcollections, and 19 dataset records.

- Top-level collection: `Data You Can Use MKE Indicators Milwaukee, Wisconsin 2025`
- Category subcollections: Equitable Housing, Population, Market Value, Equity & Access, and Health
- Dataset records: one record for each 2025 indicator listed above

Use `Member Of` relationships to connect the records:

- Category subcollections are members of the 2025 top-level collection.
- Dataset records are members of both the 2025 top-level collection and their category subcollection.

This follows the existing 2024 example pattern while matching the category structure on the Data You Can Use source page.
