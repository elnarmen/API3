import os
import requests
from functions_for_downloading_images import get_extension
from functions_for_downloading_images import download_picture
from dotenv import load_dotenv


def fetch_nasa_apod(api_key, count):
    url = f'https://api.nasa.gov/planetary/apod'
    payload = {
        'count': count,
        'api_key': api_key
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for index, response_element in enumerate(response.json()):
        extention = get_extension(response_element['url'])
        os.path.join(os.path.join(os.getcwd(), 'images'), f'nasa_apod_{index}{extention}')
        if extention:
            path = os.path.join(
                os.path.join(os.getcwd(), 'images'),
                f'nasa_apod_{index}{extention}'
            )
            download_picture(response_element['url'], path)


def main():
    load_dotenv()
    count_of_images = os.getenv('COUNT_OF_IMAGES')
    api_key = os.getenv('NASA_API_KEY')
    fetch_nasa_apod(api_key, count_of_images)


if __name__ == '__main__':
    main()
