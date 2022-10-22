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
    if args.name in files_in_dir:
        with open(f'images/{args.name}', 'rb') as photo:
            bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                timeout=20.
            )
    else:
        file_name = choice(files_in_dir)
        bot.send_photo(
            chat_id=chat_id,
            photo=open(f'images/{file_name}', 'rb'),
            timeout=20.
        )


if __name__ == '__main__':
    main()
