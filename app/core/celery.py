import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    'sample_task': {
        'task': 'device.tasks.sample_task2',
        'schedule': crontab(hour=0, minute=1),
    }
}

app.conf.timezone = 'UTC'

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')