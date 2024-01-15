import os
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

# Fetch environment variables
cron_schedule = os.environ.get('CRON_SCHEDULE')
immediate_execution = os.environ.get('IMMEDIATE_EXECUTION', 'False').lower() == 'true'
script_content = os.environ.get('SCRIPT_CONTENT', 'print("SCRIPT_CONTENT env variable not defined")')

def execute_script():
    try:
        start_time = time.time()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] Start execute the script:")
        exec(script_content)
        current_time_finish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time_finish}] Finish execute the script, duration: {(time.time() - start_time):.2f}s")
    except Exception as e:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] An error occurred while executing the script: {e}")

scheduler = BackgroundScheduler()

if immediate_execution:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Immediate execute script!")
    execute_script()
else:
    print("[INFO] IMMEDIATE_EXECUTION not defined, no immediate execution.")

if cron_schedule:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Schedule the script with cron schedule: {cron_schedule}")
    scheduler.add_job(execute_script, CronTrigger.from_crontab(cron_schedule))
    scheduler.start()
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        # Shutdown the scheduler on exit
        scheduler.shutdown()

else:
    print("[INFO] CRON_SCHEDULE not defined, no scheduled execution.")