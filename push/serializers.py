from rest_framework import serializers
from .models import Subscription, Notification


# TODO: Will be making the serializer according to the subscription object in the future
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['endpoint', 'public_key', 'auth_key']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'title', 'message', 'action_link', 'status']
