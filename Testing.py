import csv
from pprint import pprint
import googlemaps

API_KEY = open('API_KEY.txt').read()

# Create a google maps client instance
map_client = googlemaps.Client(API_KEY)

business_name = 'Super Duper Burgers San Francisco'
response = map_client.places(business_name)



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
    return(total_info)

list_of_locations = get_place_info(business_name)

# Write list of locations to a new .csv file
with open('location_file.csv', mode = 'w', newline = '') as location_file:
    location_writer = csv.writer(location_file, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
    writer = csv.writer(location_file)
    header = ['Business Name', 'Street Address', 'Latitude', 'Longitude']
    writer.writerow(header)
    writer.writerows(list_of_locations)
