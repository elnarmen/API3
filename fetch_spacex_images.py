import os
import requests
import argparse
from functions_for_downloading_images import download_picture
from functions_for_downloading_images import get_extension


def get_urls(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    urls = response.json()['links']['flickr']['original']
    if urls:
        return urls
    response = requests.get('https://api.spacexdata.com/v5/launches')
    response.raise_for_status()
    index = -2
    while not response.json()[index]['links']['flickr']['original']:
        #нельзя использовать переменную, т.к. на каждой итерации индекс отличается
        index -= 1
    urls = response.json()[index]['links']['flickr']['original']
    print(f'''
    В выбранном запуске отсутствуют фото. Будут загружены
    фотографии запуска с 'id': {response.json()[index]['id']}''')
    return urls


def fetch_spacex_last_launch(launch_id):
    urls = get_urls(launch_id)
    for index, url in enumerate(urls):
        path = os.path.join(os.path.join(os.getcwd(), 'images'),
                            f'spacex_{index}{get_extension(url)}')
        download_picture(str(url), path)


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
