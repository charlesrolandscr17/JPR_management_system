from django_cron import CronJobBase, Schedule
from .models import Employee


class UpdateDue(CronJobBase):
    schedule = Schedule(run_every_mins=1)
    code = 'main_app.cron'

    def do(self):
        print("hello")
