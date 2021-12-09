from django.urls import path
from .views import subscribe_client, send_notification, fetch_notification_status


app_name = 'push'

urlpatterns = [
    path('subscribe', subscribe_client, name="subscribe"),
    path('send_notification', send_notification, name="send_notification"),
    path('fetch_notification_status/<int:notification_id>', fetch_notification_status, name="fetch_notification_status")
]
