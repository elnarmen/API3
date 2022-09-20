import telegram
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id='@kosmo_photo_api', photo=open('images/nasa_epic_0.png', 'rb'), timeout=20.)

if __name__ == '__main__':
    main()
