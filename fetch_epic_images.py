import os
import requests
from dotenv import load_dotenv
from functions_for_downloading_images import download_picture


def fetch_epic(api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    date = '/'.join(response.json()[0]['date'][:10].split('-'))
    response_json = response.json()
    for index, response_element in enumerate(response_json):
        download_url = \
            f'https://api.nasa.gov/EPIC/archive/natural/{date}/' \
            f'png/{response_element["image"]}.png'
        payload = {'api_key': api_key}
        path = os.path.join(
            os.path.join(os.getcwd(), 'images'),
            f'nasa_epic_{index}.png'
        )
        download_picture(download_url, path,  payload=payload)


def main():
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    fetch_epic(api_key)


if __name__ == '__main__':
    main()
