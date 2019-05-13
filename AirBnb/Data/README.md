# AirBnB Data Details

### Data Sources:

1. [Inside AirBnB](http://insideairbnb.com/about.html)
2. [HM Land Registry (house prices)](http://landregistry.data.gov.uk/)

---

# Tables:

There are 4 Airbnb tables provided and 1 contextual table.

The main table is **Listings**. Each row is a unique listing on AirBnB. It contains information like the number of beds, the location, and the cancellation policy. 

There is a **Hosts** table that contains information about each host. A host can have 1+ listings. 

The other 2 tables are information that changes over time for each listing. 

- **Calendar:** For each month-year from March 2019 to March 2020, and listing, this shows the number of days listed as available, and the pricing for that month.
- **Reviews:** For each month-year and listing, this table shows the number of reviews it received, the avg word count and average sentiment score (via [Text Blob](https://textblob.readthedocs.io/en/dev/))

We've included the following contextual dataset: 

- **Housing:** Median housing prices, and count of houses sold for each borough and month

Key:

🔑: designates the key(s) of the table

💔: designates columns with ≥33% null values

### Listings

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
- reviewerCount: unique reviewers for that month
- avgsentiment: {-1: very negative, 1 very positive}
- averageWordcount

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
