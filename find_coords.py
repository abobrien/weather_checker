# Import required libaries
import geopy

# Define location service to use
locator = geopy.geocoders.Nominatim(user_agent='myGeocoder')

# Define term to search for
location = locator.geocode('Los Angeles, CA')

# Print location name, latitude, longitude
print(location)
print('Latitude = {}'.format(location.latitude))
print('Longitude = {}'.format(location.longitude))
print(format(location.latitude))
print(format(location.longitude))
