import requests

def main() -> None:
	city = input("City name: ").strip()
	if not city:
		print("Please enter a city name.")
		return

	# 1) Geocode city to lat/lon
	geo_resp = requests.get(
		"https://geocoding-api.open-meteo.com/v1/search",
		params={"name": city, "count": 1, "language": "en", "format": "json"},
		timeout=10,
	)
	geo_resp.raise_for_status()
	geo_data = geo_resp.json()
	if not geo_data.get("results"):
		print("City not found.")
		return

	lat = geo_data["results"][0]["latitude"]
	lon = geo_data["results"][0]["longitude"]

	# 2) Get current weather
	weather_resp = requests.get(
		"https://api.open-meteo.com/v1/forecast",
		params={"latitude": lat, "longitude": lon, "current_weather": True},
		timeout=10,
	)
	weather_resp.raise_for_status()
	weather = weather_resp.json().get("current_weather")

	if not weather:
		print("No weather data.")
		return

	print(f"City: {city}")
	print(f"Temperature: {weather['temperature']} °C")
	print(f"Wind: {weather['windspeed']} km/h")


if __name__ == "__main__":
	main()
