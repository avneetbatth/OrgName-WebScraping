# OrgName-WebScraping
This project aims to web scrape the addresses of organizations just given their name. 

The organizations will be varied in type. Some will be large multi-nationals, others will be small organizations with only a single address. From the address, I want to also get the latitude-longitude of the location and use that for geo-spatial analysis. For an organization, I currently want to get all of their locations in the United States of America and US Territories. 

If an organization has an excessive amount of locations, say over 100, I would like to only consider 2 locations per state, for example, in a manner that a certain radius around those locations reaches the largest number of people. Additionally, I want to only consider locations that contain certain criteria. For example, given Company A, if they have 100 locations in New York, I would like to select their two locations with the largest number of amenities as the first condition.

I plan on using Python as the main language for this project. The end goal for this project is to have a robust web scraping algorithm that is able to pull the addresses of varied organization types. 

Stage 1: Read in query names from a CSV. Take those queries and output the Business Name, Street Address, Latitude, and Longitude into another CSV.
  - Update 1: Searching every state for every business name. Taking only the operational businesses. Bug: Hardee's returns 874 locations; it actually has 1,700 US locations. Search radius isn't large enough? And/or the Search API can't return enough results for each state (only 60 max). 
