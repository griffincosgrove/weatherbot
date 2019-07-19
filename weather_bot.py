# purpose of this program is to create a bot that texts me with the weather for each day.

from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather
import datetime
import smtplib as smp

API_KEY = 'your key'  # replace with your API key from darksky developers

darksky = DarkSky(API_KEY)

latitude = 38.998440

longitude = -77.293022

# cords for Harrisonburg
# 38.435982
# -78.879997

forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False,
    lang=languages.ENGLISH,
    units=units.AUTO,
    exclude=[weather.MINUTELY, weather.ALERTS]
)

forecast.latitude
forecast.longitude
forecast.timezone


# this method builds the string for the daily weather report.
def daily_forecast():
    daily_summary = ''
    for item in forecast.daily.data:
        daily_summary = ('High is ' + str(item.temperature_high) + " but it will feel like " +
                         (str(item.apparent_temperature_high)))
        daily_summary += (' at ' + str(item.temperature_high_time.strftime("%I %p")))
        daily_summary += '\n'
        daily_summary += ('Low is ' + str(item.temperature_low) + " but it will feel like " +
                          (str(item.apparent_temperature_low)))
        daily_summary += ' at ' + str(item.temperature_low_time.strftime("%I %p"))
        daily_summary += '\n'
        daily_summary += 'With a ' + str(item.precip_probability) + ' chance of precipitation'
        break

    return daily_summary


# email logic. plugin your credentials in the place holder

smtp_obj = smp.SMTP('smtp.gmail.com', 587)
smtp_obj.starttls()
smtp_obj.login('user@gmail.com', 'password')
smtp_obj.sendmail('me@gmail.com', 'recipient@gmail.com', 'Subject: Weather. \n' + daily_forecast())
smtp_obj.quit()
