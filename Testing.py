import os
from pprint import pprint
import googlemaps

API_KEY = ''

# Create a google maps client instance
map_client = googlemaps.Client(API_KEY)

#print(dir(map_client))

# def get_place_info()
business_name = 'Super Duper Burgers San Francisco'
response = map_client.places(business_name)
#pprint(response['results'][0])


# For each location, get array of Business Name, Street Address, Latitude, Longitude
def get_place_info(business_name):
    total_info = []
    for i in map_client.places(business_name)['results']:
        address_info = []
        address_info.append(i['name'])
        address_info.append(i['formatted_address'])
        address_info.append(i['geometry']['location']['lat'])
        address_info.append(i['geometry']['location']['lng'])
        total_info.append(address_info)
        #print(address_info)
    #pprint(total_info)


with open('location_file.csv', mode = 'w') as location_file:
    location_writer = csv.writer(location_file, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)

    for i in get_place_info(business_name):
        location_writer.writerow(i)
        #address_info = []

# Take in the Excel file as a CSV? Put all the names of the locations into an array

# Interact with Google Maps API to get the addresses of the business given its name

# Put addresses into another object? Use dict? Key is the business name. Value is a list of addresses for it. 
