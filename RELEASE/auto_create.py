import os, sys, subprocess

TASK_NAME = 'ObsidianSyncScheduler'

def create_scheduled_task():
    python_exe = sys.executable
    script_path = os.path.abspath('scheduler.py')
    
    cmd = (
        f'schtasks /create /tn "{TASK_NAME}" /tr "{python_exe} {script_path}" '
        f'/sc onlogon /rl highest /f'
    )
    
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f'Задача {TASK_NAME} успешно создана и будет запускаться при входе в систему.')
    except subprocess.CalledProcessError as e:
        print(f'Произошла ошибка при создании задачи: {e}')
        
if __name__ == '__main__':
    create_scheduled_task()