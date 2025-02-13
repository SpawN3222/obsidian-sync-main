# obsidian-sync-main
A lightweight tool to automate manual synchronization of Obsidian.md vaults between devices. The script creates a zip archive of your vault, names it with the current date, and enables easy transfer to other devices or platforms. Easy to tune with FTP or TG Bot.

## Installation and launch (TG Bot for example)
1. Set the settings:
   ```bash
   pip install tqdm aiogram
   ```
2. Download [Token for your Telegram bot](https://core.telegram.org/bots#botfather).
3. Specify the settings in `config.py ` (TOKEN = ' ').
4. Run the script:
   ```bash
   py syncing.py
   ```

## Project structure
- `config.py`: Configuration parameters.
- `syncing.py`: The main script for working with the archive and Telegram afterwards.

## License
[MIT License](https://mit-license.org)
