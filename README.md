# weather_checker
Python-based web scraper to pull US weather data from NWS using geopy, requests, BeautifulSoup. The program runs in CLI or returns variable that could integrate into other applications.

Geopy is a library to find latitude , longitude coordinates for a given location provided as a string. This allows the weather_checker function to be called with locations in various formats such as 'City, State', 'City State', 'City', 'Zip', etc. reducing dependence on the user entering their location in the right format.

requests is used to establish an HTTP connection to the website and download the source code into a local object for further analysis.

BeautifulSoup (package name: bs4) iterates over the HMTL source object and looks for specified elements to extract as strings that are later repurposed into the output presented to the user.
