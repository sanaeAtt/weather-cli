import requests
from dotenv import load_dotenv
import os
from colorama import Fore, Style, init


init(autoreset=True)


load_dotenv()

weather_emojis = {
    "clear sky": "☀️",
    "few clouds": "🌤️",
    "scattered clouds": "🌥️",
    "broken clouds": "☁️",
    "overcast clouds": "☁️",
    "light rain": "🌦️",
    "moderate rain": "🌧️",
    "heavy intensity rain": "🌧️",
    "thunderstorm": "⛈️",
    "snow": "❄️",
    "mist": "🌫️",
    "fog": "🌫️",
    "haze": "🌁",
    "smoke": "💨",
    "dust": "🌪️",
    "sand": "🏜️",
    "ash": "🌋",
    "squalls": "🌬️",
    "tornado": "🌪️"
}

def get_current_weather():
    # print(Fore.CYAN + Style.BRIGHT + "\n***** Get Current Weather *****\n")

    city = input(Fore.YELLOW + "Name the city: ")

    request_URL = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    print(Fore.BLUE + request_URL)

    res = requests.get(request_URL)
    weather_data = res.json()

    if res.status_code == 200 and weather_data.get('cod') == 200:
        name = weather_data['name']
        country = weather_data['sys']['country']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']
        description_cap = description.capitalize()

        emoji = weather_emojis.get(description.lower(), "🌈")  

        print(f"\n{Fore.GREEN + Style.BRIGHT}Weather in {name}, {country} {emoji}")
        print(f"{Fore.MAGENTA}Temperature: {temp}°C (feels like {feels_like}°C)")
        print(f"{Fore.RED}Sky: {description_cap}")
        print(f"{Fore.CYAN}Humidity: {humidity}%")
        print(f"{Fore.YELLOW}Wind Speed: {wind_speed} m/s")

    else:
        error_msg = weather_data.get("message", "Unknown error")
        print(Fore.RED + f"Error: Unable to fetch weather data. Reason: {error_msg}")

if __name__ == "__main__":
    get_current_weather()
