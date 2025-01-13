import os
from zipfile import ZipFile, ZIP_DEFLATED
from datetime import datetime
from aiogram import Bot
from aiogram.types import FSInputFile
from config import TOKEN

# ? 1 ЭТАП: РАБОТА С АРХИВАЦИЕЙ
# ?----------------------------------------------------

# ? Указываем пути
SOURCE_DIR = "__dirname__"  # ! Папка с хранилищем (включительно)
DATE = datetime.now().strftime("%d-%m-%Y")  # ? Текущая дата в формате день-месяц-год
ARCHIVE_NAME = f"vault_backup_{DATE}.zip"   # ? Имя архива с датой

# ? Архивация папки
def archive_folder(source_dir, archive_name):
    with ZipFile(archive_name, 'w', ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # ? Сохраняем полную структуру, включая саму папку
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, os.path.dirname(source_dir))
                zipf.write(file_path, arcname)
    print(f"Папка '{source_dir}' заархивирована в '{archive_name}'. Переход к запуску бота...")


# ? 2 ЭТАП: РАБОТА С ТГ-БОТОМ
# ? ----------------------------------------------------

# ? Пути для бота
FOLDER_PATH = os.path.dirname(os.path.abspath(__file__)) # ? Путь до архива (папка проекта)
ARCHIVE_PATH = os.path.join(FOLDER_PATH, ARCHIVE_NAME)
CHAT_ID = 111111111 # ! ID чата для отправки архива (@userinfobot в TG)

async def send_backup():
    bot = Bot(token=TOKEN)

    if os.path.exists(ARCHIVE_PATH):
        try:
            # ? Передача пути к файлу в InputFile
            archive = FSInputFile(ARCHIVE_PATH)
            await bot.send_document(CHAT_ID, archive)
            print(f"Архив '{ARCHIVE_NAME}' отправлен в чат с ID: {CHAT_ID}.")
        except Exception as e:
            print(f"Произошла ошибка при отправке: {e}")
        finally:
            await bot.session.close()
    else:
        print(f"Архив не найден: [{FOLDER_PATH}].")

# ? Архивация папки
archive_folder(SOURCE_DIR, ARCHIVE_NAME)

# ? Функция запуска бота
if __name__ == "__main__":
    import asyncio
    asyncio.run(send_backup())