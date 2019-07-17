# purpose of this program is to create a bot that texts me with the weather for each day.

from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather

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

# add logic to send to email.