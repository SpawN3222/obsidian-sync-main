from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess


def run_script():
    try:
        subprocess.run(["python", "syncing.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Произошла ошибка при выполнении скрипта: {e}")
        
        
scheduler = BlockingScheduler()
scheduler.add_job(run_script, "cron", day_of_week="sun", hout=18, minute=0)

print("Планировщик запущен. Скрипт будет выполняться раз в неделю по воскресеньям в 18:00.")
scheduler.start()