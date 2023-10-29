import requests

API_KEY = "981f4871dff33b756267a9027b45143e"


def get_data(place, forecast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    nr_values = 8 * forecast_days
    filtered_data = data['list'][:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
