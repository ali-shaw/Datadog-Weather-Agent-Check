import requests

# the following try/except block will make the custom check compatible with any Agent version
try:
    # first, try to import the base class from old versions of the Agent...
    from checks import AgentCheck
except ImportError:
    # ...if the above failed, the check is running in Agent version 6 or later
    from datadog_checks.checks import AgentCheck

# content of the special variable __version__ will be shown in the Agent status page
__version__ = "1.0.0"

class WeatherTempCheck(AgentCheck):
    def check(self, instance):
        url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&units=metric&appid='YOUR_API_KEY'

        res = requests.get(url)

        data = res.json()

        temp = data['main']['temp']
        humidity = data['main']['humidity']
        clouds = data['clouds']['all']

        self.gauge('weather.temp', temp, tags=['location:london'])
        self.gauge('weather.humidity', humidity, tags=['location:london'])
        self.gauge('weather.clouds',clouds, tags=['location:london'])
