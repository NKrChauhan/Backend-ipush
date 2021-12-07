from django.urls import path
from .views import subscribe_client, send_notification


app_name = 'push'

urlpatterns = [
    path('subscribe', subscribe_client, name="subscribe"),
    path('send_notification', send_notification, name="send_notification")
]
