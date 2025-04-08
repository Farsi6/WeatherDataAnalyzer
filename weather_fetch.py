import requests

api_key = "a345bdfd49b8ae9c60b5acdc7ac7f5f4"  # Replace with your OpenWeatherMap API key
city = "Bahawalnagar"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    desciption = data["weather"][0]["description"]
    print (f"city: {city}")
    print (f"Temperature: {temperature}°C")
    print (f"Feels Like: {feels_like}")
    print (f"Humidity: {humidity}%")
    print (f"Desciption: {desciption}")
else:
    print(f"Error: {response.status_code}")