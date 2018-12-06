from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)
forecasts_moscow = weather.lookup_by_location('moscow').forecast
forecasts_swamp = weather.lookup_by_location('petersburg').forecast
for forecast in forecasts_swamp:
    print(forecast.text)
    print(forecast.date)
    print(forecast.high)
    print(forecast.low)
