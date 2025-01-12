# obsidian-sync-main
A lightweight tool to automate manual synchronization of Obsidian.md vaults between devices. The script creates a zip archive of your vault, names it with the current date, and enables easy transfer to other devices or platforms. Easy to tune with FTP or TG Bot.

## Installation and launch
1. Set the settings:
   ```bash
   pip install aiogram
   ```
2. Download [Token for your Telegram bot](https://core.telegram.org/bots#botfather).
3. Specify the settings in `config.py ` (TOKEN = '').
4. Run the script:
   ```bash
   py syncing.py
   ```

## Project structure
- `config.py`: Configuration parameters.
- `syncing.py`: The main script for working with the archive and Telegram afterwards.

---

Легкий инструмент для автоматизации ручной синхронизации Obsidian.md хранилища между устройствами. Скрипт создает zip-архив вашего хранилища, присваивает ему название с текущей датой и позволяет легко переносить его на другие устройства или платформы. Легко настраивается с помощью FTP или TG ботов.

## Установка и запуск
1. Установите настройки:
   ```bash
   pip install aiogram
   ```
2. Скачайте [Токен для вашего Telegram-бота](https://core.telegram.org/bots#botfather).
3. Укажите настройки в `config.py ` (TOKEN = '').
4. Запустите скрипт:
   ```bash
    py syncing.py
   ```

## Структура проекта
- `config.py`: Конфигурационные параметры.
- `syncing.py`: Основной скрипт для работы с архивом и Telegram-ботом.

## License
[MIT License](https://mit-license.org)
