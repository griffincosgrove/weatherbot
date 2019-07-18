# purpose of this program is to create a bot that texts me with the weather for each day.

from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather
import datetime

API_KEY = '984f861bb9c84baa5744eb667835b824'

darksky = DarkSky(API_KEY)

latitude = 38.998440

longitude = -77.293022

# cords for Harrisonburg
# 38.435982
# -78.879997

forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
)

forecast.latitude
forecast.longitude
forecast.timezone


def daily_forecast():
    daily_summary = ''
    for item in forecast.daily.data:
        daily_summary = ('High is ' + str(item.temperature_high) + " but it will feel like " +
                         (str(item.apparent_temperature_high)))
        daily_summary += (' at ' + str(item.temperature_high_time.strftime("%I %p")))
        daily_summary += '\n'
        daily_summary += ('Low is ' + str(item.temperature_low) +  " but it will feel like " +
                          (str(item.apparent_temperature_low)))
        daily_summary += ' at ' + str(item.temperature_low_time.strftime("%I %p"))
        daily_summary += '\n'
        daily_summary += 'With a ' + str(item.precip_probability) + ' chance of precipitation'
        break

    return daily_summary


daily_forecast()

# add logic to send to email.
