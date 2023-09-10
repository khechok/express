import requests
# API endpoint and parameters
city = input('Enter your city: ')
url = "https://goweather.herokuapp.com/weather" + city
api_key = "YOUR_API_KEY"
city = "London"
# Build API request
params = {
"q": city,
"appid": api_key,
"units": "metric"
}
# Send GET request
response = requests.get(url, params=params)
# Check if the request was successful
if response.status_code == 200:
   # Extract weather data from the response
   data = response.json()~
   temperature = data["main"]["temp"]
   weather_description = data["weather"][0]["description"] 
   # Print the retrieved data
   print(f"Current weather in {city}:")
   print(f"Temperature: {temperature}°C")
   print(f"Description: {weather_description}")
else:
    print("Error: Failed to retrieve weather data")

