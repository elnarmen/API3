import time
import telegram
import os
import argparse
from random import shuffle
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    parser = argparse.ArgumentParser(
        description='''Скрипт автоматически публикует изображения в 
                           телеграм-канал "КосмоФото" с заданным интервалом''')
    parser.add_argument('--interval',
                        help='''
                        Введите необходимый интервал (целое число) 
                        для публикации изображений илипропустите команду
                        (интервал публикаций по умолчанию - 4 часа)
                                ''',
                        default=4,
                        type=int
                        )
    args = parser.parse_args()
    bot = telegram.Bot(token=token)
    files_in_dir = os.listdir('images')
    while True:
        shuffle(files_in_dir)
        for file_name in files_in_dir:
            bot.send_photo(
                chat_id='@kosmo_photo_api',
                photo=open(f'images/{file_name}', 'rb'),
                timeout=20.)
            time.sleep(args.interval * 3600)


if __name__ == '__main__':
    main()
