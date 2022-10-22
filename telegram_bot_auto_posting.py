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
    chat_id = os.getenv('TG_CHAT_ID')
    filenames = os.listdir('images')
    directorypath = os.path.join(os.getcwd(), 'images')
    while True:
        shuffle(filenames)
        for filename in filenames:
            filepath = os.path.join(directorypath, filename)
            with open(filepath, 'rb') as photo:
                bot.send_photo(
                    chat_id=chat_id,
                    photo=photo,
                    timeout=20.)
            time.sleep(args.interval * 3600)


if __name__ == '__main__':
    main()
