from rest_framework import serializers
from push.models import Subscription


# TODO: Will be making the serializer according to the subscription object in the future
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['endpoint', 'public_key', 'auth_key']
