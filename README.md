# Космический телеграм
Загружает изображения с API портала NASA и фото запусков SpaceX, а так же публикует загруженные изображения в телеграм канале.

## Загрузка проекта
   Откройте терминал и перейдите в папку, в которую хотите загрузить файлы.
   Например, если Вы хотите загрузить проект в директорию `D:\python`, введите последовательно команды:
   ```
   d:
   ```
   ```
   cd python
   ```
   Наберите в терминале команду:
       
   ```
   git clone https://github.com/elnarmen/API3
   ```
   В папке API3 создайте файл **```.env```** для хранения переменных окружения
## Установка зависимостей
   Перейдите в папку с проектом командой:
   ```
   cd API3
   ```
   Используйте pip (или pip3 для MacOs) для установки зависимостей:

   ```
   pip install -r requirements.txt
   ```
## Получение ключей и токенов
   Для загрузки фотографий с API портала NASA необходимо получить ключ.<br>
   Перейдите по ссылке: [https://api.nasa.gov/](https://api.nasa.gov/), выберите вкладку 
   **```Generate API Key```** и заполните форму.<br>
   
   На указанный в форме email, будет направлено письмо с ключом примерно следующего вида: **NKOyfV77dhbz4JQIiZrDkiFuUh9wHhyBjWs5N5oL**
   <br>
   
   Сохраните полученный ключ в переменной окружения NASA_API_KEY в файле **```.env```** :
   <br>
   ```
   NASA_API_KEY = 'ВАШ API-КЛЮЧ'
   ```
   Для публикации изображений в Telegram нужно создать телеграм-бота и получить его API-токен.
   <br>
   Инструкция создания телеграм-канала, бота и получения телеграм-токена доступна по ссылке:
   [https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)
   <br>
   
   Сохраните токен в файле  **```.env```** в переменной TELEGRAM_TOKEN
   ```
   TELEGRAM_TOKEN = 'ВАШ ТЕЛЕГРАМ-ТОКЕН'
   ```
   Так же сохраните ссылку на телеграм-канал в переменной CHAT_ID:
   ```
   CHAT_ID = '@имя_канала'
   ```
## Загрузка изображений
Изображения сохраняются в папку "Images"
  ### fetch_apod_images.py
  Cкачивает необходимое количесто изображений космоса с [API портала NASA](https://api.nasa.gov/).<br>
  Для возможности выбора колличества скачиваемых фото, сохраните в файле **```.env```** 
  переменную COUNT_OF_IMAGES и укажите нужное количество.<br>
  Пример для загрузки 20 фото:<br>
  ```
  COUNT_OF_IMAGES = 20
  ```
  Затем введите команду:
  ```
  python fetch_apod_images.py
  ```
  ### fetch_epic_images.py
  Скачивает EPIC-фотографии Земли за последнюю доступную дату.<br>
  Для загрузки введите в терминале:
  ```
  python fetch_epic_images.py
  ```
  ### fetch_spacex_images.py
  Скачивает фотографии запусков компании SpaceX.<br>
  Чтобы загрузить фото с конкретного запуска, введите команду:
  ```
  python fetch_spacex_images.py --id
  ```
  затем, через пробел, id запуска.<br>
  
  Чтобы скачать фотографии с последнего запуска введите команду:
  ```
  python fetch_spacex_images.py
  ```
  ## Публикация фотографий на канале
  ### Ручная публикация фотографий
  Для публикации случайной фотографии введите команду:
  ```
  python telegram_bot.py
  ```
  Для публикации определенного фото введите:
  ```
  python telegram_bot.py --name
  ```
  а затем, через пробел, полное название файла.
  При вводе имени файла, отсутствующего в папке **images**, будет опубликовано
  случайное изображение из папки **images**
### Автоматическая публикация
**telegram_bot_auto_posting.py** публикует загруженные изображения через заданный промежуток времени.
Чтобы интервал публикаций оставался по умолчанию (4 часа), введите команду:
```
python telegram_bot_auto_posting.py
```
Для публикации фотографий каждые 2 часа:
```
python telegram_bot_auto_posting.py --interval 2
```
