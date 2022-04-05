from asyncio import tasks
import os
from celery import Celery
task = tasks


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings', namespace='CELERYAPP')
app.autodiscover_tasks()