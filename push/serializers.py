from rest_framework import serializers
from .models import Subscription


# Will be making the serializer according to the subscription object in the future
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['endpoint', 'subscribe_time', 'public_key', 'auth_key']
