from django.urls import path
from .views import subscribe_client


app_name = 'push'

urlpatterns = {
    path('subscribe/', subscribe_client, name="subscribe"),
}
