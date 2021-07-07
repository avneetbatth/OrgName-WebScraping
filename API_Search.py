import csv
from pprint import pprint
import googlemaps

API_KEY = open('API_KEY.txt').read()

# Create a google maps client instance
map_client = googlemaps.Client(API_KEY)

# Declare the list of queries whose address and lat-long coordinates will be searched for
business_names = []

with open('input_data.csv', encoding = 'utf8') as file_in:
    csv_reader = csv.reader(file_in)
    # Use this to skip the header
    next(csv_reader)
    for line in csv_reader:
        business_names.append(line)


# Given a location of a business name, get array of Business Name, Street Address, Latitude, Longitude
def get_place_info(business_names):
    total_info = []
    # business_names is a list, and I want to see each business in that list
    for business in business_names:
        for i in map_client.places(business)['results']:
            # Ensure that location is operational
            if (i['business_status'] == 'OPERATIONAL'):
                address_info = []
                address_info.append(i['name'])
                address_info.append(i['formatted_address'])
                address_info.append(i['geometry']['location']['lat'])
                address_info.append(i['geometry']['location']['lng'])
                total_info.append(address_info)     
    return(total_info)

list_of_locations = get_place_info(business_names)

# Write list of locations to a new .csv file
with open('location_file.csv', mode = 'w', newline = '') as location_file:
    writer = csv.writer(location_file)
    header = ['Business Name', 'Street Address', 'Latitude', 'Longitude']
    writer.writerow(header)
    writer.writerows(list_of_locations)
