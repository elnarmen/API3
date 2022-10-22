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
    files_in_dir = os.listdir('images')
    path_to_dir = os.path.join(os.getcwd(), 'images')
    while True:
        shuffle(files_in_dir)
        for file_name in files_in_dir:
            path_to_file = os.path.join(path_to_dir, file_name)
            with open(path_to_file, 'rb') as photo:
                bot.send_photo(
                    chat_id=chat_id,
                    photo=photo,
                    timeout=20.)
            time.sleep(args.interval * 3600)


if __name__ == '__main__':
    main()
