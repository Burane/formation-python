from datetime import date, timedelta
from weatherapp.weather import Weather

print("hello world")


caen = (49.183, -0.38)
w = Weather()
# w.display_currrent_weather(caen[0], caen[1], 1)
today = date.today() - timedelta(weeks=1)
yesterday = today - timedelta(days=1, weeks=1)
w.display_past_weather(caen[0], caen[1], yesterday, yesterday)