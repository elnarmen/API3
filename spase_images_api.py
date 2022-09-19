import os
import requests
import pathlib
from urllib.parse import urlparse


def get_extension(url):
    path = urlparse(url).path
    extension = os.path.splitext(path)[1]
    return extension


def download_picture(url, path):
    path = pathlib.Path(path)
    path.parent.mkdir(exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)
