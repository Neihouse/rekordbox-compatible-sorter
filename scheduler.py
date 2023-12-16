import schedule
import time

# Scheduler for periodic tasks

class Scheduler:
    def __init__(self):
        self.jobs = []

    def schedule_task(self, task, schedule_time):
        """Schedules a task to be run at a specific time.

        Args:
            task (function): The task function to schedule.
            schedule_time (str): The time when the task should run.
        """
        job = schedule.every().day.at(schedule_time).do(task)
        self.jobs.append(job)

    def run_pending(self):
        """Runs all pending scheduled tasks.
        """
        while True:
            schedule.run_pending()
            time.sleep(1)
