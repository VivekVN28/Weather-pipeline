import requests

api_url="http://api.weatherstack.com/current?access_key={API_KEY}&query=New York"
def fetch_data():
    print("Fetching weatherstack API...")
    try:
        response=requests.get(api_url)
        response.raise_for_status()
        print("API response received")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise
data=None
def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-01-20 12:42', 'localtime_epoch': 1768912920, 'utc_offset': '-5.0'}, 'current': {'observation_time': '05:42 PM', 'temperature': -7, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'astro': {'sunrise': '07:16 AM', 'sunset': '04:59 PM', 'moonrise': '08:29 AM', 'moonset': '07:01 PM', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 1}, 'air_quality': {'co': '263.85', 'no2': '25.35', 'o3': '46', 'so2': '6.15', 'pm2_5': '9.65', 'pm10': '9.85', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 23, 'wind_degree': 270, 'wind_dir': 'W', 'pressure': 1027, 'precip': 0, 'humidity': 33, 'cloudcover': 0, 'feelslike': -15, 'uv_index': 2, 'visibility': 16, 'is_day': 'yes'}}