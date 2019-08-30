# Datadog-Weather-Agent-Check
A simple Datadog Agent Check to query the OpenWeatherMap API (https://openweathermap.org/) and post weather data as a custom metric to Datadog.

Usage:
1. Create a OpenWeatherMap account and retrieve your API Key: https://home.openweathermap.org/api_keys
2. Download/Clone this repo
3. Update the `weather.py` file and add your OpenWeatherMap API Key at the end of the `url` variable
4. On any host running a Datadog Agent:
  - Place the `weather.yaml` file in `conf.d/` directory
  - Place the `weather.py` file in `checks.d/` directory
5. Restart the Datadog Agent
6. Rejoice!

Some helpful resources:
- Datadog Agent Check Docs: https://docs.datadoghq.com/developers/write_agent_check/?tab=agentv6
- OpenWeatherMap Docs: https://openweathermap.org/api
