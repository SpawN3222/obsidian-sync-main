import os
import logging
import asyncio

from time import sleep
from zipfile import ZipFile, ZIP_DEFLATED
from tqdm.asyncio import tqdm
from aiogram import Bot
from aiogram.types import FSInputFile
from aiohttp import ClientSession, FormData

from config import *


# ? ASCII-интро
print(ASCII_INTRO)


# ? 1 ЭТАП: РАБОТА С АРХИВАЦИЕЙ
# ? ----------------------------------------------------
# ?  Архивация папки


def archive_folder(source_dir, archive_name):
    print(f"Архивация папки {source_dir}...")
    try:
        with ZipFile(archive_name, 'w', ZIP_DEFLATED) as zipf:
            files = [
                os.path.join(root, file)
                for root, _, files in os.walk(source_dir)
                for file in files
            ]
            for file_path in tqdm(files, desc="Архивация файлов", ascii="1234567890=", colour="magenta"):
                arcname = os.path.relpath(file_path, os.path.dirname(source_dir))
                zipf.write(file_path, arcname)
        print(f"Папка [{source_dir}] {GREEN}успешно{RESET} заархивирована в [{archive_name}]")
        return True
    except Exception as e:
        print(f"{RED}Произошла ошибка при архивации{RESET}: {e}")
        return False



# ? 2 ЭТАП: РАБОТА С ТГ-БОТОМ
# ? ----------------------------------------------------

logging.basicConfig(level=logging.DEBUG)


async def send_backup_with_progress():

    file_size = os.path.getsize(ARCHIVE_PATH)
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"

    async with ClientSession() as session:
        with open(ARCHIVE_PATH, "rb") as file:
            # ? Создаём прогресс-бар
            form = FormData()
            progress_bar = tqdm(total=file_size, unit="B", unit_scale=True, desc="Загрузка", ascii="1234567890=", colour="magenta")

            # ? Передача файла с отслеживанием прогресса
            async def file_gen():
                while chunk := file.read(4096): # Размер буфера 4KB
                    yield chunk
                    progress_bar.update(len(chunk))

            form.add_field("chat_id", CHAT_ID)
            form.add_field("document", 
                           file_gen(), 
                           filename=os.path.basename(ARCHIVE_NAME), 
                           content_type="application/zip"
                           )

            # ? Отправляем запрос
            response = await session.post(url, data=form)
            progress_bar.close()

        if response.status == 200:
            print(f"Архив [{ARCHIVE_NAME}] {GREEN}успешно{RESET} отправлен в чат с ID: {CHAT_ID}.")
        else:
            print(f"{RED}Ошибка при отправке{RESET}: {response.status}")


async def send_backup():

    bot = Bot(token=TOKEN, timeout=180)

    if os.path.exists(ARCHIVE_PATH):
        try:
            # ?  Передача пути к файлу в InputFile
            archive = FSInputFile(ARCHIVE_PATH)
            if os.path.getsize(ARCHIVE_PATH) > 50 * 1024 * 1024:  # 50 MB
                print(f"{RED}Ошибка{RESET}: Архив превышает 50 МБ. Отправка отменена.")
                exit()
            await bot.send_document(CHAT_ID, archive)
            print(f"Архив '{ARCHIVE_NAME}' отправлен в чат с ID: {CHAT_ID}.")
        except Exception as e:
            print(f"{RED}Произошла ошибка при отправке{RESET}: {e}")
        finally:
            await bot.session.close()
    else:
        print(f"{RED}Архив не найден{RESET}: [{FOLDER_PATH}].")


# ? Функция архивации и запуска бота
if archive_folder(SOURCE_DIR, ARCHIVE_NAME):
    if __name__ == "__main__":
        print("\nЗапуск бота, отправка архива...")
        
        asyncio.run(send_backup_with_progress()) # ? send_backup_with_progress()  ||  send_backup()
        
        sleep(5)
else:
    print(f"Архивация {RED}не удалась{RESET}. Отправка архива отменена.")
    
    sleep(3)
    
