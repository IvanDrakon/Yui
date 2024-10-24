import requests
from key import weather_API, lat, long

MY_LAT = lat
MY_LONG = long

PARAMETERS = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": weather_API,
    "units": "metric",
    "cnt": 2,
}


def take_weather() -> str:
    data = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=PARAMETERS)
    data.raise_for_status()
    weather_data = data.json()
    current_weather = weather_data["list"][0]
    current_weather_temp = current_weather["main"]
    current_weather_detail = current_weather["weather"][0]
    current_weather_icon = current_weather_detail["icon"]
    match current_weather_icon:
        case "01d":
            icon = "☀️"
        case "01n":
            icon = "🌙"
        case "02d":
            icon = "🌤"
        case "02n":
            icon = "☁️🌙"
        case "03d":
            icon = "☁️"
        case "03n":
            icon = "☁️"
        case "04d":
            icon = "☁️☁️"
        case "04n":
            icon = "☁️☁️"
        case "09d":
            icon = "🌧"
        case "09n":
            icon = "🌧"
        case "10d":
            icon = "🌦"
        case "10n":
            icon = "🌦"
        case "11d":
            icon = "⛈"
        case "11n":
            icon = "⛈"
        case "13d":
            icon = "❄️"
        case "13n":
            icon = "❄️"
        case "50d":
            icon = "🌫"
        case "50n":
            icon = "🌫"
        case _:
            pass
    if float(current_weather_temp['temp']) > 22.0:
        temp_icon = "🔥"
    elif 14.0 < float(current_weather_temp['temp']) < 22.0:
        temp_icon = "😎"
    elif float(current_weather_temp['temp']) < 14.0:
        temp_icon = "❄️"
    return (f"Now the weather is: {current_weather_detail['description'].title()} {icon}\n"
            f"Temperature is: {current_weather_temp['temp']}C° {temp_icon}\n"
            f"Max: {current_weather_temp['temp_max']}C° | Min: {current_weather_temp['temp_min']}C°\n")


def rain():
    data = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=PARAMETERS)
    data.raise_for_status()
    weather_data = data.json()
    will_rain = False
    for weather in weather_data["list"]:
        weather_id = weather["weather"][0]["id"]
        if weather_id < 700:
            will_rain = True
    if will_rain:
        return "☔️☔️ There is a good chance to rain in the next 6h ☔️☔️"
    else:
        return "🌻🌻 No rain in the next 6h 🌻🌻"
