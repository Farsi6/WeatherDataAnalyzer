import requests
import csv

api_key = "a345bdfd49b8ae9c60b5acdc7ac7f5f4"  # Replace with your OpenWeatherMap API key
city = input("Enter City Name to check temperature: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    print (f"city: {city}")
    print (f"Temperature: {temperature}°C")
    print (f"Feels Like: {feels_like}°C")
    print (f"Humidity: {humidity}%")
    print (f"Weather Desciption: {description}")
    # Save to CSV
    with open('weather_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write header if file is empty (optional, for the first run)
        if file.tell() == 0:
            writer.writerow(['City', 'Temperature (°C)','Feels like (°C)' 'Humidity (%)', 'Weather Description'])
        # Write data
        writer.writerow([city, temperature, feels_like, humidity, description])
else:
    print(f"Error: {response.status_code}")