import schedule
import time

class Scheduler:
    def __init__(self):
        self.jobs = []

    def schedule_task(self, task, schedule_time):
        job = schedule.every().day.at(schedule_time).do(task)
        self.jobs.append(job)

    def run_pending(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
