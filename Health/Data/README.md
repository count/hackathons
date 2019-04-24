# Health Data Details

### Data Sources:

1. [Public Health England](https://fingertips.phe.org.uk/)
2. [NHS England](https://digital.nhs.uk/data-and-information/publications/statistical/quality-and-outcomes-framework-achievement-prevalence-and-exceptions-data)
3. [Data.uk (for ccg to county mapping)](http://data.UKhttps://data.gov.uk/dataset/d304a541-c315-42af-883f-558b8de9228c/lower-layer-super-output-area-2011-to-clinical-commissioning-group-to-local-authority-district-april-2017-lookup-in-england-version-4)
4. [ONS (for population data)](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration)

---

### File Schemas

1. SocialStats.csv

This file contains social indicators by Year, and County. 

- **AreaCode**: Unique area code intentifier
- **AreaType**: Upper Authority Level (ULTA) or Lower Authority Level (LTA)
- **AreaName**: Name of the Area
- **UtlaName**: Upper Authority Level Name (will be the same as AreaName, if the area in question is a ULTA)
- **UtlaCode**: Upper Authority Level Code
- **Year**: 2010-2017
- **mortality_attributable_to_air_pollution**: Fraction of mortality attributable to particulate air pollution.
    - Fraction of annual all-cause adult mortality attributable to anthropogenic (human-made) particulate air pollution (measured as fine particulate matter, PM2.5*).
- **access_to_healthy_assets**: Percentage of the population who live in LSOAs which score in the poorest performing 20% on the Access to Healthy Assets & Hazards (AHAH) index.
    - The AHAH index is comprised of three domains: access to retail services (fast food outlets, gambling outlets, pubs/bars/nightclubs, off licences, tobacconists), access to health services (GP surgeries, A&E hospitals, pharmacies, dentists and leisure centres), and physical environment (access to green spaces, and three air pollutants: NO2 level, PM10 level, SO2 level). The AHAH index provides a summary of an area's relative performance on these indicators (the second and third domains conceptualised as health promoting and the first (access to retail) as health demoting). It therefore provides information on how conducive to good health an area is relative to other areas, for the specific indicators.
- **access_to_woodlands**: Percentage of the population in each local authority that has accessible woodland of at least 2 hectare within 500 metres of where they live
- **affordability_of_home**: Ratio of median house price to median gross annual residence-based earnings (A higher ratio indicates that on average, it is less affordable for a resident to purchase a house in their local authority district)
- **air_pollution_particulate_mat**: Air pollution: fine particulate matter
    - Annual concentration of human-made fine particulate matter at an area level, adjusted to account for population exposure. Fine particulate matter is also known as PM2.5 and has a metric of micrograms per cubic metre (µg/m3).
- **crime_deprivation_score:**

    The score derived from the aggregate crime indicators in the English Indices of Deprivation 2015. A higher score means that an area is more deprived.

    The indicators that contribute to the score are:

    - Violence: The rate of violence per 1,000 at-risk population
    - Burglary: The rate of burglary per 1,000 at-risk properties
    - Theft: The rate of theft per 1,000 at-risk population
    - Criminal Damage: The rate of criminal damage per 1,000 at-risk population
- **density_of_fast_food**: Crude rate per 100,000 population: the number of fast food outlets is divided by the population of the area and multiplied by 100,000.
- **deprivation_score**: The English Indices of Deprivation 2015 use 37 separate indicators, organised across seven distinct domains of deprivation which can be combined, using appropriate weights, to calculate the Index of Multiple Deprivation 2015 (IMD 2015). This is an overall measure of multiple deprivation experienced by people living in an area.
- **employment_deprivation_score:**

    The score derived from the aggregate employment indicators in the English Indices of Deprivation 2015. A higher score means that an area is more deprived.

    The indicators that contribute to the score are:

    - Claimants of Jobseeker’s Allowance (both contribution-based and income-based), women aged 18 to 59 and men aged 18 to 64
    - Claimants of Employment and Support Allowance (both contribution-based and income-based) , women aged 18 to 59 and men aged 18 to 64
    - Claimants of Incapacity Benefit, women aged 18 to 59 and men aged 18 to 64
    - Claimants of Severe Disablement Allowance, women aged 18 to 59 and men aged 18 to 64
    - Claimants of Carer’s Allowance, women aged 18 to 59 and men aged 18 to 64
- **housing_affordability_ratio**: The ratio of lower quartile house price to lower quartile earnings
- **income_deprivation**: The Income Deprivation Domain measures the proportion of the population experiencing deprivation relating to low income. The definition of low income used includes both those people that are out-of-work, and those that are in work but who have low earnings (and who satisfy the respective means tests).
- **prop_living_in_aqmas:** Proportion of population living within AQMAs (%)(Air Quality Management Areas)
- **CountyCode**: Unique code for each County
- **RegionName**: Region Name

2. HealthStats.csv

This file contains data by Year, County, Age Group, and Sex

- **AreaCode**: Unique area code intentifier
- **AreaType**: Upper Authority Level (ULTA) or Lower Authority Level (LTA)
- **AreaName**: Name of the Area
- **UtlaName**: Upper Authority Level Name (will be the same as AreaName, if the area in question is a ULTA)
- **UtlaCode**: Upper Authority Level Code
- **Year**: 2010-2017
- **Age:** Age groups
- **diupr_resp_rate**: DiUPR - Respiratory disease (%), Persons, All Ages
    - Place of death indicator calculated as: (Deaths at usual residence/All Deaths) x 100%
    - Usual residence is defined as: home, care homes (local authority and non-local authority) and religious establishments.
- **asmr_0-64**: Directly Age Standardised Mortality Rate (ASMR), Persons, Aged 0 - 64 years
    - The directly age standardised mortality rate (ASMR) per 100,000 persons aged under 65 years in each Strategic Clinical Network (SCN), for each year.
- **asmr_65-74:** see above.
- **asmr_75-84:** see above.
- **asmr_85+:** see above.
- **asmr_all:** see above.
- **resp_death_per_0-64**: Respiratory disease deaths (%), Persons, Aged 0 - 64 years
    - The number of deaths for persons aged under 65 years where respiratory disease is the underlying cause of death divided by the total number of residents aged under 65 years who died each year, multiplied by 100
- **resp_death_per_65-74**: see above
- **resp_death_per_75-84**: see above
- **resp_death_per_85+**: see above
- **resp_death_per_all**: see above
- **admin_resp_tract_inf_1y**: Admissions for respiratory tract infections in infants aged under 1 year
- **admin_resp_tract_inf_2-4:** Admissions for respiratory tract infections in infants aged 2, 3 and 4 years
- **admin_resp_tract_inf_<1:** Admissions for respiratory tract infections in infants aged under 1 year
- **CountyCode:** Unique county code
- **RegionName:** Region Name

3. HealthCCG.csv

This file contains data by CCG Code, and Year

- **ccg code:** Clinical commissioning groups
- **UtlaCode**: Upper Authority Level Code
- **Year**: 2014-2017
- **asthma_prev_rate:** Asthma prevelance rate
- **copd_prev_rate:** COPD (Chronic Obstructive Pulmonary Disease) prevalence rate
- **diabetes_prev_rate:** Diabetes prevalence rate
- **obesity_prev_rate:** Obesity prevalence rate
- **hypertension_prev_rate:** Hypertension prevalence rate
- **smoker_count:** Number of self-identified smokers aged 15+

4. CCGMap.csv

This file contains the mapping from CCG to County.

- **ccg_code:** Clinical commissioning groups
- **UtlaCode:** Unique Upper Authority Level Code

5. CountyPopulations.csv

File containing the populations for each County, and Sex from 2001-2016.

- **AreaName**: LAD Name
- **LadCode**: LAD Code
- **UtlaCode**: UTLA Code
- **UtlaName**: UTLA Name
- **Year**
- **Sex**: Male, Female, Persons (Male + Female)
- **Population**:

6. Alltogether.csv

This is a pre-merged file that contains all of the indicators listed above at the level of UtlaCode,UtlaName, Year. 
