from dotenv import load_dotenv
import os
import requests

load_dotenv()
apikey = os.getenv("API_KEY")
def get_data(place, days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={apikey}"
    response = requests.get(url)
    content = response.json()
    filtered_content = content["list"]
    nr_values = 8 * days
    filtered_content = filtered_content[:nr_values]
    return filtered_content

if __name__ == "__main__":
    print(get_data(place="Tokyo", days=3, kind="Temperature"))