import csv
from pprint import pprint
import googlemaps
import time

start_time = time.time()

API_KEY = open('API_KEY.txt').read()

# Create a google maps client instance
map_client = googlemaps.Client(API_KEY)

# Declare the list of queries whose address and lat-long coordinates will be searched for
business_names = []
state_data = []

# Get user input for the filenames to read in

# Input of business names
with open('input_data.csv', encoding = 'utf8') as file_in:
    csv_reader = csv.reader(file_in)
    # Use this to skip the header
    next(csv_reader)
    for line in csv_reader:
        business_names.append(line)

# Input of state search data: Abbreviation, Latitude, Longitude, Full Name 
with open('state_data.csv', encoding = 'utf8') as file_in:
    csv_reader = csv.reader(file_in)
    # Use this to skip the header
    next(csv_reader)
    for line in csv_reader:
        state_data.append(line)

# Given a location of a business name, get array of Business Name, Street Address, Latitude, Longitude
def get_place_info(business_names, state_data):
    total_info = []
    # business_names is a list, and I want to see each business in that list
    # pprint(map_client.places("Costco", location="19.898682, -155.665857"))
    for business in business_names:
        for state in state_data: 
            #latitude = state[1]
            #longitude = state[2]
            location = state[1] + ', ' + state[2]
            for i in map_client.places(business[0], location)['results']:
                # Ensure that location is operational
                try:
                    if (i['business_status'] == 'OPERATIONAL'):
                            address_info = []
                            address_info.append(business)
                            address_info.append(i['name'])
                            address_info.append(i['formatted_address'])
                            address_info.append(i['geometry']['location']['lat'])
                            address_info.append(i['geometry']['location']['lng'])
                            total_info.append(address_info)
                except KeyError:
                    pass
    return(total_info)

list_of_locations = get_place_info(business_names, state_data)

# Write list of locations to a new .csv file
with open('VSS_output.csv', mode = 'w', newline = '') as location_file:
    writer = csv.writer(location_file)
    header = ['Query', 'Business Name', 'Street Address', 'Latitude', 'Longitude']
    writer.writerow(header)
    writer.writerows(list_of_locations)

print("Process finished --- %s seconds ---" % (time.time() - start_time))
