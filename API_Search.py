import csv
from pprint import pprint
import googlemaps
import time

start_time = time.time()

#API_KEY = open('API_KEY.txt').read()

# Create a google maps client instance
map_client = googlemaps.Client(API_KEY)

# Declare the list of queries whose address and lat-long coordinates will be searched for
business_names = []
state_data = []

# Get user input for the filenames to read in
business_file = input('Enter the name of the file with the business names. Make sure it\'s in the same directory:')
state_file = input('Enter the name of the file with the state data. Make sure it\'s in the same directory:')

# Input of business names
with open(business_file, encoding = 'utf8') as file_in:
    csv_reader = csv.reader(file_in)
    # Use this to skip the header
    next(csv_reader)
    for line in csv_reader:
        business_names.append(line)

# Input of state search data: Abbreviation, Latitude, Longitude, Full Name 
with open(state_file, encoding = 'utf8') as file_in:
    csv_reader = csv.reader(file_in)
    # Use this to skip the header
    next(csv_reader)
    for line in csv_reader:
        state_data.append(line)

# Given a location of a business name, get array of Business Name, Street Address, Latitude, Longitude
def get_place_info(business_names, state_data):
    total_info = []
    # business_names is a list, and I want to see each business in that list
    for business in business_names:
        for state in state_data: 
            #latitude == state[1] and longitude == state[2]
            # location format: location="19.898682, -155.665857"
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

# Remove duplicates from the list_of_locations
list_of_locations_final = []
[list_of_Locations_final.append(place) for place in list_of_locations if place not in list_of_locations_final]

# User input for output filename
output_file = input('Please enter the name of the output file as a csv:')

# Write list of locations to a new .csv file
with open(output_file, mode = 'w', newline = '') as location_file:
    writer = csv.writer(location_file)
    header = ['Query', 'Business Name', 'Street Address', 'Latitude', 'Longitude']
    writer.writerow(header)
    writer.writerows(list_of_locations_final)

# How long it took for the script to run
print("Process finished --- %s seconds ---" % (time.time() - start_time))
