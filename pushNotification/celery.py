import os
from celery import Celery
from pushNotification.settings import INSTALLED_APPS
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pushNotification.settings')

app = Celery('push', broker='amqp://guest:guest@127.0.0.1:5672/')

app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django apps.
app.autodiscover_tasks(lambda: INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
