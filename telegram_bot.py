import telegram
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id='@kosmo_photo_api', text="I'm sorry Dave I'm afraid I can't do that.")


if __name__ == '__main__':
    main()
