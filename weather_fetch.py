import requests

api_key = "your API key here"  # Replace with your OpenWeatherMap API key
city = "Bahawalnagar"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"Temperature in {city}: {data['main']['temp']}°C")
else:
    print(f"Error: {response.status_code}")