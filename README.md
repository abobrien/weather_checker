# weather_checker
Python web scraper to pull US weather data from NWS
using geopy, requests, BeautifulSoup.

Geopy is a library to find lat,long coordinates for a given location provided as a string. This allows the weather_checker function to be called with locations in various formats such as 'City, State', 'City State', 'City', 'Zip', etc. reducing need for user to inpu the function paramater in a specific format.

requests is used to establish an HTTP connection to the website and download the source code into a python object.

BeautifulSoup (imported from bs4) looks for specified HTML elements in the web page's source code and pulls strings from the elements that are later repurposed into data presented to the user.
