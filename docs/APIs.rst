==============
API Documentation
==============

**Cryptocurrency Price Retrieval API (CoinGecko)**
----------------------------------------------

You can retrieve real-time cryptocurrency prices using the CoinGecko Cryptocurrency Price Retrieval API.

Endpoint: https://api.coingecko.com/api/v3/simple/price
Method: GET

Parameters:
- ids: List of cryptocurrency IDs (e.g., bitcoin, litecoin, ethereum, dogecoin)
- vs_currencies: The currency in which you want to get prices (e.g., usd)

Example Usage (JavaScript):
```javascript
// Example JavaScript code to retrieve cryptocurrency prices
var liveprice = {
    "async": true,
    "crossDomain": true,
    "url": "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Clitecoin%2Cethereum%2Cdogecoin&vs_currencies=usd",
    "method": "GET",
    "headers": {}
}

$.ajax(liveprice).done(function (response) {
    // Access cryptocurrency prices from the response
    var bitcoinPrice = response.bitcoin.usd;
    var litecoinPrice = response.litecoin.usd;
    var ethereumPrice = response.ethereum.usd;
    var dogecoinPrice = response.dogecoin.usd;
});





Mapbox API
----------

You can use the Mapbox API to display interactive maps and add location-related features to your web application. Here's how you can integrate Mapbox into your web application:

**Mapbox Access Token:**
------------------------

   To get started with Mapbox, you need to sign up for an account on [Mapbox](https://www.mapbox.com/) and obtain an access token.

   ```javascript
   mapboxgl.accessToken = 'YOUR_MAPBOX_ACCESS_TOKEN'; // Replace with your Mapbox access token



Map Initialization:
-------------------

Initialize your Mapbox map by providing the container where you want to display the map, the map style, the center coordinates, and the initial zoom level.


var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11', // Change this to your desired map style
    center: [-15.9780, 18.0841], // Center the map on Nouakchott
    zoom: 12 // Set the initial zoom level
});


Map Style Management:
--------------------

You can toggle between different map styles. Two styles, 'satellite' and 'roadmap', are provided in the example.

function toggleMapStyle(style) {
    if (style === 'satellite') {
        map.setStyle(satelliteStyle);
    } else if (style === 'roadmap') {
        map.setStyle(roadmapStyle);
    }
}


Geocoding Control:
------------------

Add a geocoding control to your map, allowing users to search for locations on the map.

var geocoder = new MapboxGeocoder({
    accessToken: mapboxgl.accessToken,
    mapboxgl: mapboxgl,
    placeholder: 'Search...',
    marker: false,
});



You can listen for the 'result' event to get the selected location's coordinates and fly to that location on the map.

geocoder.on('result', function (e) {
    var coordinates = e.result.geometry.coordinates;
    map.flyTo({ center: coordinates, zoom: 15 });
)
}


Directions Control:
------------------

Initialize Mapbox Directions to provide route navigation to users. You can set various options, such as unit, profile, and control elements.

var directions = new MapboxDirections({
    accessToken: mapboxgl.accessToken,
    unit: 'metric',
    profile: 'mapbox/driving',
    controls: {
        profileSwitcher: false
    }
});


Route Distance Calculation:
---------------------------

Calculate and display the route distance. This example adds a route source and layer to the map and updates the distance when a route is selected.


map.on('load', function () {
    // Add source and layer for route display
    map.addSource('route', { ... });
    map.addLayer({ ... });

    // Update the distance when a route is selected
    directions.on('route', function (e) { ... });
)
}






**OpenMapWeather API**
------------------

The OpenMapWeather API allows you to retrieve weather data for cities. Here's how you can integrate OpenMapWeather into your web application:

 **Function to Display City Information:**

   Create a function to display city information based on weather data. This function takes the city name and weather data as parameters and updates the HTML with the city's image, name, and weather information.

   ```javascript
   function displayCityInfo(cityName, weatherData) {
       // Implementation as provided in the code snippet
   }


Listening for Geocoder 'result' Event:
--------------------------------------

geocoder.on('result', (event) => {
    const selectedCity = event.result.text; // Get the selected city name from Mapbox geocoder result

    // Call the function to fetch city weather and display city information
    fetchCityWeather(selectedCity);
});

Function to Fetch City Weather:
-------------------------------

Create a function to fetch weather data for a given city using the OpenMapWeather API. This function uses an API key to make the request and then displays the weather information using the displayCityInfo function.

function fetchCityWeather(cityName) {
    const apiKey = 'YOUR_OPENMAPWEATHER_API_KEY'; // Replace with your OpenMapWeather API key
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&units=metric&appid=${apiKey}`;
    // Fetch and process weather data as provided in the code snippet
}

