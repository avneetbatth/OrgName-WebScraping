import os
from pprint import pprint
import googlemaps

API_KEY = ''

# Create a google maps client instance
map_client = googlemaps.Client(API_KEY)

#print(dir(map_client))

# def get_place_info()
location_name = 'Super Duper Burgers San Francisco'
response = map_client.places(location_name)
#pprint(response['results'][0])

for i in response['results']:
    print(i['formatted_address'])


#pprint('Address: ' + response['results'][0]['formatted_address'])
#pprint(response['results'][0]['geometry']['location'])

#work_place_address = '1 Market Street, San Francisco, CA'
#organization_name = 'East Orange VA'
#map_client.
#response = map_client.geocode(work_place_address)
#pprint(response)

#pprint(response[0]['formatted_address'])
# Take in the Excel file as a CSV? Put all the names of the locations into an array

# Interact with Google Maps API to get the addresses of the business given its name

# Put addresses into another object? Use dict? Key is the business name. Value is a list of addresses for it. 
