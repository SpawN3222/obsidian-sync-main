import subprocess

TASK_NAME = 'ObsidianSyncScheduler'

def delete_scheduled_task():
    cmd = f'schtasks /delete /tn "{TASK_NAME}" /f'
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"Задача '{TASK_NAME}' успешно удалена.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при удалении задачи: {e}")

if __name__ == "__main__":
    delete_scheduled_task()