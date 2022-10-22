import telegram
import os
import argparse
from random import choice
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')
    parser = argparse.ArgumentParser(
        description='''Скрипт публикует изображение в телеграм-канал "КосмоФото"'''
    )
    parser.add_argument(
        '--name',
        help='''Введите название изображения, которое необходимо опубликовать 
                или не вводите ничего для публикации случайного изображения''')
    args = parser.parse_args()
    bot = telegram.Bot(token=token)
    files_in_dir = os.listdir('images')
    path_to_dir = os.path.join(os.getcwd(), 'images')
    if args.name in files_in_dir:
        path_to_file = os.path.join(path_to_dir, arg.name)
    else:
        file_name = choice(files_in_dir)
        path_to_file = os.path.join(path_to_dir, file_name)
    with open(path_to_file, 'rb') as photo:
        bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            timeout=20.
        )


if __name__ == '__main__':
    main()
