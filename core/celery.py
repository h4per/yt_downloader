import os
from celery import Celery
from django.conf import settings

# Устанавливаем связь с настройками джанго
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Создаем объект 
app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
