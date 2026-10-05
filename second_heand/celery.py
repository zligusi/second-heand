import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_heand.settings')

app = Celery('second_heand')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()