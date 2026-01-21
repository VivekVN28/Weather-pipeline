import requests

api_url="http://api.weatherstack.com/current?access_key={API_KEY}&query=New York"
def fetch_data():
    print("Fetching weatherstack API...")
    try:
        response=requests.get(api_url)
        response.raise_for_status()
        print("API response received")
        print(response.json)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise
data=fetch_data()
def mock_fetch_data():
    return data