import os
from datetime import datetime


TOKEN = '' # ! Токен из @BotFather


# ? Консты для дизайна:
RED = "\033[31m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

ASCII_INTRO = MAGENTA + r"""

         __         _     ___                                        
  ____  / /_  _____(_)___/ (_)___ _____        _______  ______  _____
 / __ \/ __ \/ ___/ / __  / / __ `/ __ \______/ ___/ / / / __ \/ ___/
/ /_/ / /_/ (__  ) / /_/ / / /_/ / / / /_____(__  ) /_/ / / / / /__  
\____/_.___/____/_/\__,_/_/\__,_/_/ /_/     /____/\__, /_/ /_/\___/  
                                                 /____/              

""" + RESET


# ? Пути для архивации:
SOURCE_DIR = "__dirpath__"  # Папка с хранилищем (включительно)
DATE = datetime.now().strftime("%d-%m-%Y")  # Текущая дата в формате день-месяц-год
ARCHIVE_NAME = f"vault_backup_{DATE}.zip"  # Имя архива с датой


# ? Пути для бота:
FOLDER_PATH = os.path.dirname(os.path.abspath(__file__)) # ?  Путь до архива (папка проекта)
ARCHIVE_PATH = os.path.join(FOLDER_PATH, ARCHIVE_NAME)
CHAT_ID = '111111111' # ! ID чата для отправки архива (@userinfobot в TG)