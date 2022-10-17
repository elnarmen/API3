import os
import requests
import argparse
from spase_images_api import download_picture
from spase_images_api import get_extension


def fetch_spacex_last_launch(id):
    url = f'https://api.spacexdata.com/v5/launches/{id}'
    response = requests.get(url)
    response.raise_for_status()
    urls = response.json()['links']['flickr']['original']
    if not urls:
        response = requests.get('https://api.spacexdata.com/v5/launches')
        response.raise_for_status()
        i = -2
        while not response.json()[i]['links']['flickr']['original']:
            i -= 1
        urls = response.json()[i]['links']['flickr']['original']
        print(f'''
        В выбранном запуске отсутствуют фото. Будут загружены
        фотографии запуска с 'id': {response.json()[i]['id']}''')
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
            '''
        )
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id)


if __name__ == '__main__':
    main()
