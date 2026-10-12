import os 
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_hand.settings')
app = Celery('second_heand')
app.config_from_objects('django.conf:settings', namespace='CELERY')
app.autodiscover_tacks()