import os
import requests
import argparse
from functions_for_downloading_images import download_picture
from functions_for_downloading_images import get_extension


def get_urls(id):
    url = f'https://api.spacexdata.com/v5/launches/{id}'
    response = requests.get(url)
    response.raise_for_status()
    urls = response.json()['links']['flickr']['original']
    if urls:
        return urls
    response = requests.get('https://api.spacexdata.com/v5/launches')
    response.raise_for_status()
    index = -2
    response_json = response.json()[index]['links']['flickr']['original']
    while not response_json:
        index -= 1
    urls = response.json()[index]['links']['flickr']['original']
    print(f'''
    В выбранном запуске отсутствуют фото. Будут загружены
    фотографии запуска с 'id': {response.json()[index]['id']}''')
    return urls


def fetch_spacex_last_launch(id):
    urls = get_urls(id)
    for i, url in enumerate(urls):
        download_picture(str(url), f'images/spacex_{i}{get_extension(url)}')


def main():
    parser = argparse.ArgumentParser(
        description='''Программа скачивает фото с последнего запуска SpaseX'''
    )
    parser.add_argument(
        '--id',
        help='''
                Введите ID запуска, чтобы загрузить фото
                или сразу жмите "Enter", чтобы загрузить
                фото последнего запуска
             ''',
        default='latest'
        )
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id)


if __name__ == '__main__':
    main()
