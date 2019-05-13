# AirBnB Data Details

### Data Sources:

1. [Inside AirBnB](http://insideairbnb.com/about.html)
2. [Companies House (businesses)](http://download.companieshouse.gov.uk/en_output.html)
3. [London Datastore (crime data)](https://data.london.gov.uk/dataset/recorded_crime_summary)
4. [HM Land Registry (house prices)](http://landregistry.data.gov.uk/)
5. [ALVA (Tourism data)](http://www.alva.org.uk/details.cfm?p=609)

---

# Tables:

There are 4 Airbnb tables provided and 4 contextual tables.

The main table is **AllListings**. Each row is a unique listing on AirBnB. It contains information like the number of beds, the location, and the cancellation policy. 

There is a **Hosts** table that contains information about each host. A host can have 1+ listings. 

The other 2 tables are information that changes over time for each listing. 

- **Calendar:** For each month-year from March 2019 to March 2020, and listing, this shows the number of days listed as available, and the pricing for that month.
- **Reviews:** For each month-year and listing, this table shows the number of reviews it received, the avg word count and average sentiment score (via [Text Blob](https://textblob.readthedocs.io/en/dev/))

To see how London neighborhoods have changed over time, we've included the following context datasets: 

- **Housing:** Median housing prices, and count of houses sold for each borough and month
- **Businesses:** Businesses by type and neighbourhood
- **Crimes:** Monthly crimes by type, neighbourhood
- **Tourism:** 2018 visitor information for top 50 UK attractions

Key:

🔑: designates the key(s) of the table

💔: designates columns with ≥33% null values

### AllListings

- 🔑 id: The unique id for a listing (a.k.a. property)
- last scraped: the date the listing information was gathered (scraped)
- listing url: link to the listing
- name: The title of the listing
- host id: the unique id for the listing's host [links to "host id" in **Hosts** table]
- experiences: {none, business, family, social, romantic}
- neighbourhood: maps to London's boroughs {e.g. City of London, Tower Hamlets, etc.}
- latitude
- longitude
- property type: {e.g. Apartment, House}
- room type: {Private room, Shared room, Entire house/apt}
- accommodates: Number of people the listing can accommodate.
- bathrooms: Number of bathrooms
- bedrooms: Number of bedrooms
- beds: Number of available beds
- bed type: {Real Bed, Pull-out Sofa, Futon, Couch, Airbed}
- minNights
- maxNights
- reviewCount
- instant bookable {t,f}
- is business travel ready: {t,f}
- cancellation policy: {e.g. flexible, moderate}
- first review
- last review
- review rating
- review accuracy
- review cleanliness
- review checkin
- review communication
- review location
- review value
- price
- 💔security deposit
- cleaning fee
- guests included
- extra people

### Hosts

- 🔑 host id: unique id for each host
- host url
- name
- host since
- location
- 💔response time: {e.g. within a day, within an hour}
- 💔response rate: (in %)
- is superhost: {t,f}
- 💔neighbourhood: unfortunately, does not match London boroughs. {e.g. Hampstead, Shoreditch}
- listingsCount: number of listings each host has
- verifications
- has profile pic
- identity verified:

### Calendar

- 🔑listing id: The unique id for a listing (a.k.a. property)
- 🔑month year
- days available: days listed as available for that listing in that month
- mean price: (in USD) average nightly listing price for available days in that month
- max price (in USD)
- min price (in USD)

### Reviews

- 🔑listing id: The unique id for a listing (a.k.a. property)
- 🔑month year
- 🔑neighbourhood
- number of reviewers: unique reviewers for that month
- average sentiment: {-1: very negative, 1 very positive}
- average wordcount

## Contextual Data

### Housing

- 🔑neighbourhood (a.k.a. borough)
- 🔑mon_yr
- medianDetached
- medianFlat
- medianOther
- medianSemiDet
- medianTerraced
- countDetached
- countFlat
- countOther
- countSemiDet
- countTerraced
- medianOverall
- countOverall

### Businesses

- 🔑neighbourhood (a.k.a. borough)
- 🔑incorpYear: Year business was incorporated
- 🔑company status: {e.g. Active}
- 🔑company type: {e.g. Construction}
- companyCount

### Crimes

- 🔑crime type 
- 🔑neighbourhood
- 🔑mon_yr
- crimes

### Tourism

- 🔑Rank
- Site
- Total visits
- Charge/free
- Group
- Neighbourhood
