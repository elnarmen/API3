import telegram
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    bot = telegram.Bot(token=token)
    print(bot.get_me())


if __name__ == '__main__':
    main()
