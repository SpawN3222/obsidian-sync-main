import os
import zipfile
import requests
from datetime import datetime

# Указываем пути
SOURCE_DIR = "..dirname.."  # Папка с хранилищем
VAULT_NAME = os.path.basename(SOURCE_DIR)  # Имя папки с хранилищем
DATE = datetime.now().strftime("%d-%m-%Y")  # Текущая дата в формате день-месяц-год
ARCHIVE_NAME = f"vault_backup_{DATE}.zip"  # Имя архива с датой
UPLOAD_URL = "https://example.com/upload"  # Ссылка на API для загрузки

# Архивация папки
def archive_folder(source_dir, archive_name):
    with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # Сохраняем полную структуру, включая саму папку
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, os.path.dirname(source_dir))
                zipf.write(file_path, arcname)
    print(f"Папка '{source_dir}' заархивирована в '{archive_name}'")

# Загрузка архива на сервер
def upload_archive(file_path, upload_url):
    with open(file_path, 'rb') as f:
        response = requests.post(upload_url, files={"file": f})
        if response.status_code == 200:
            print("Файл успешно загружен!")
        else:
            print(f"Ошибка загрузки: {response.status_code}")

# Распаковка архива
def extract_archive(archive_name, target_dir):
    with zipfile.ZipFile(archive_name, 'r') as zip_ref:
        zip_ref.extractall(target_dir)
        print(f"Архив '{archive_name}' распакован в '{target_dir}'")

# Основная логика
archive_folder(SOURCE_DIR, ARCHIVE_NAME)
upload_archive(ARCHIVE_NAME, UPLOAD_URL)
