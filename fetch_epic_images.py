import os
import requests
from dotenv import load_dotenv
from spase_images_api import download_picture


def fetch_epic(api_key):
    url = 'https://epic.gsfc.nasa.gov/api/natural'
    payload = {'api_key': api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for i, item in enumerate(response.json()):
        download_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/' \
                       f'png/{item["image"]}.' \
                       f'png?api_key={api_key}'
        download_picture(download_url, f'images/nasa_epic_{i}.png')



def main():
    load_dotenv()
    api_key = os.getenv('API_KEY')
    fetch_epic(api_key)


if __name__ == '__main__':
    main()
