# Import required libraries
import requests
from bs4 import BeautifulSoup
import geopy

# Define location service to use
locator = geopy.geocoders.Nominatim(user_agent='myGeocoder')

# Define function: check_weather()
def check_weather(param1):

    # Define term to search for
    location = locator.geocode(param1)

    # Define location variables
    loc_name = location
    loc_lat = format(location.latitude)
    loc_lon = format(location.longitude)

    # Define URL to scrape
    URL = 'https://forecast.weather.gov/MapClick.php?lat=' + loc_lat + '&lon=' + loc_lon + '#.XglxxXOSmCo'
    page = requests.get(URL)

    # Initialize scraper
    soup = BeautifulSoup(page.content, 'html.parser')

    # Narrow the scraper to search within the appropriate ID
    weather = soup.find_all(id='current_conditions-summary')  # build object for each section/class break
    
    # Iterate over each object to extract relevant data
    for element in weather:
        conditions = element.find('p', class_='myforecast-current')
        temp_high = element.find('p', class_='myforecast-current-lrg')
        temp_low = element.find('p', class_='myforecast-current-sm')
        if None in (conditions, temp_high, temp_low):  # if an element is missing, skip and continue
            continue
    
    # Print elements
    print('-'* 125)
    print('Current Weather for ' + str(loc_name))
    print('-'* 125)
    print('Current Conditions: ' + conditions.text.strip())
    print('High: ' + temp_high.text.strip())
    print('Low: ' + temp_low.text.strip())
    print('-'* 125)
    print('Detailed forecast: ' + URL)
    print('-'* 125)
    print()

# Call the function: check_weather
check_weather('Blacklick OH')