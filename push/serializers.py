from rest_framework import serializers
from .models import Subscriptions


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ['endpoint', 'auth_key', 'public_key', 'subscribe_time']
