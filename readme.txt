to clone existing repo from wwcollins at github

gh repo clone wwcollins/noaa-weather-and-tides OR

using CircleCI:  https://app.circleci.com/pipelines/github/wwcollins/noaa-weather-and-tides
setup repo


openweathermap.org

API_KEY:  d7794bbe3d41d7dbcd0c93c331d5e819  Name: weatheralert

with key...

no exlusions
https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid=d7794bbe3d41d7dbcd0c93c331d5e819

with exclusions
https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}




Call below, with exclusions...
https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=d7794bbe3d41d7dbcd0c93c331d5e819




--------------------------------------------------------------------------

e.g.

older 2.0 API
http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}

3.0 One Call API
https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

weatheralert will use above for now...


Call API

Getting current, minute, hourly and daily forecast weather data

https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

Getting historical weather data by specified timestamp from 1st January 1979

https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API key}


Useage: API 3.0 https://openweathermap.org/api/one-call-3

How to make an API call
API call

https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

Parameters
lat, lon	required	Geographical coordinates (latitude, longitude). If you need the geocoder to automatic convert city names and zip-codes to geo coordinates and the other way around, please use our Geocoding API.
appid	required	Your unique API key (you can always find it on your account page under the "API key" tab)
exclude	optional	By using this parameter you can exclude some parts of the weather data from the API response. It should be a comma-delimited list (without spaces).
Available values:

current
minutely
hourly
daily
alerts
units	optional	Units of measurement. standard, metric and imperial units are available. If you do not use the units parameter, standard units will be applied by default. Learn more
lang	optional	You can use the lang parameter to get the output in your language. Learn more
Example of API call

Before making an API call, please note, that One Call 3.0 is included in the "One Call by Call" subscription only. Learn more

https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}




---------------------------------------------------------------------------
How to migrate from Dark Sky API to OpenWeather One Call API 3.0

Parameters
lat, lon	required	Geographical coordinates (latitude, longitude)
appid	required	Your unique API key (you can always find it on your account page under the "API key" tab)
dt	required	Date from the 5 previous days (unix time, UTC time zone), e.g. dt=1586468027
exclude	optional	By using this parameter you can exclude some parts of the weather data from the API response. It should be a comma-delimited list (without spaces).
Available values:

current
minutely
hourly
daily
alerts
One Call API 3.0 documentation (complete description of API calls and parameters in API response, with examples).
One Call API documentation
Matching parameters
One Call API	Dark Sky API	Description
timezone	timezone	Time zone name of the requested location
Current weather
(parameters of current weather and historical weather are the same)
dt	time	UTC time zone
sunrise	sunriseTime	Sunrise time, unix, UTC
sunset	sunsetTime	Sunset time, unix, UTC
temp	temperature	Temperature. Unit Default: Kelvin.
How to change units format
feels_like	apparentTemperature	Feels like. Unit Default: Kelvin.
How to change units format
pressure	pressure	Atmospheric pressure on the sea level, hPa
humidity	humidity	Humidity, %
dew_point	dewPoint	Dew point. Unit Default: Kelvin.
How to change units format
clouds	cloudCover	Cloudiness, %
wind_speed	windSpeed	Wind speed. Unit Default: meter/sec.
How to change units format
wind_gust	windGust	Wind gust. Unit Default: meter/sec.
How to change units format
wind_deg	windBearing	Wind direction, degrees (meteorological)
weather.description	summary	Weather condition within the group.
Full list of weather conditions
You can get the output in your language.
Learn more
weather.icon	icon	Weather icon id. How to get icons
rain	precipIntensity	Precipitation volume, mm
snow	precipIntensity	Snow volume, mm
uvi	uvIndex	UV index
visibility	visibility	Average visibility, meters
Minute forecast for 1 hour
dt	time	Time of forecasted data, unix, UTC
precipitation	precipIntensity	Precipitation volume, mm
Hourly forecast for 48 hours
(parameters of hourly forecast and historical weather are the same)
dt	time	Time of forecasted data, unix, UTC
temp	temperature	Temperature. Unit Default: Kelvin.
How to change units format
feels_like	apparentTemperature	Feels like. Unit Default: Kelvin.
How to change units format
pressure	pressure	Atmospheric pressure on the sea level, hPa
humidity	humidity	Humidity, %
dew_point	dewPoint	Dew point. Unit Default: Kelvin.
How to change units format
clouds	cloudCover	Cloudiness, %
wind_speed	windSpeed	Wind speed. Unit Default: meter/sec.
How to change units format
wind_gust	windGust	Wind gust. Unit Default: meter/sec.
How to change units format
wind_deg	windBearing	Wind direction, degrees (meteorological)
weather.description	summary	Weather condition within the group.
Full list of weather conditions
You can get the output in your language.
Learn more
weather.icon	icon	Weather icon id. How to get icons
rain	precipIntensity	Precipitation volume, mm
snow	precipIntensity	Snow volume, mm
visibility	visibility	Average visibility, meters
Daily forecast for 8 days
dt	time	Time of data forecasted, unix, UTC
sunrise	sunriseTime	Sunrise time, unix, UTC
sunset	sunsetTime	Sunset time, unix, UTC
temp.day	temperatureHigh	Day temperature. Unit Default: Kelvin.
How to change units format
temp.night	temperatureLow	Night temperature. Unit Default: Kelvin.
How to change units format
temp.morn	-	Morning temperature. Unit Default: Kelvin.
How to change units format
temp.eve	-	Evening temperature. Unit Default: Kelvin.
How to change units format
temp.min	temperatureMin	Unit Default: Kelvin.
How to change units format
temp.max	temperatureMax	Unit Default: Kelvin.
How to change units format
feels_like.day	apparentTemperatureHigh	Unit Default: Kelvin.
How to change units format
feels_like.night	apparentTemperatureLow	Unit Default: Kelvin.
How to change units format
feels_like.morn	-	Unit Default: Kelvin.
How to change units format
feels_like.eve	-	Unit Default: Kelvin.
How to change units format
pressure	pressure	Atmospheric pressure on the sea level, hPa
humidity	humidity	Humidity, %
dew_point	dewPoint	Unit Default: Kelvin.
How to change units format
clouds	cloudCover	Cloudiness, %
wind_speed	windSpeed	Wind speed. Unit Default: meter/sec.
How to change units format
wind_gust	windGust	Wind gust. Unit Default: meter/sec.
How to change units format
wind_deg	windBearing	Wind direction, degrees (meteorological)
weather.description	summary	Weather condition within the group.
Full list of weather conditions
You can get the output in your language.
Learn more
weather.icon	icon	Weather icon id. How to get icons
rain	precipIntensity	Precipitation volume, mm
snow	precipIntensity	Snow volume, mm
uvi	uvIndex	UV index
visibility	visibility	Average visibility, meters







