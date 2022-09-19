import os
import requests
import argparse
from spase_images_api import get_extension
from spase_images_api import download_picture
from dotenv import load_dotenv


def fetch_nasa_apod(api_key):
    url = f'https://api.nasa.gov/planetary/apod'
    payload = {
        'count': 20,
        'api_key': api_key
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for i, item in enumerate(response.json()):
        extention = get_extension(item["url"])
        if extention:
            download_picture(item['url'], f'images/nasa_apod_{i}{extention}')


def main():
    load_dotenv()
    api_key = os.getenv('API_KEY')
    fetch_nasa_apod(api_key)


if __name__ == '__main__':
    main()
