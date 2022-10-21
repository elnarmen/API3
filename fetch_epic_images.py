import os
import requests
from dotenv import load_dotenv
from spase_images_api import download_picture


def fetch_epic(api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    date = '/'.join(response.json()[0]['date'][:10].split('-'))
    for i, response_element in enumerate(response.json()):
        download_url = \
            f'https://api.nasa.gov/EPIC/archive/natural/{date}/' \
            f'png/{response_element["image"]}.png'
        payload = {'api_key': api_key}
        download_picture(download_url, f'images/nasa_epic_{i}.png',  payload=payload)


def main():
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    fetch_epic(api_key)


if __name__ == '__main__':
    main()
