# Import required libaries
import geopy

# Define location service to use
# Full list of available services found in documentation under Geocoders: https://geopy.readthedocs.io/en/stable/
locator = geopy.geocoders.Nominatim(user_agent='myGeocoder')

# Define term to search for
location = locator.geocode('Los Angeles, CA')

# Print location name, latitude, longitude
print(location)
print('Latitude = {}'.format(location.latitude))
print('Longitude = {}'.format(location.longitude))
print(format(location.latitude))
print(format(location.longitude))
