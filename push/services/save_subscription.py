from push.models import Subscription
from push.serializers.subscription_serializer import SubscriptionSerializer


class SaveSubscription:
    @staticmethod
    def save_subscription(valid_subscription_data):
        subscription_object = Subscription.objects.create(
            endpoint=valid_subscription_data['endpoint'],
            auth_key=valid_subscription_data['auth_key'],
            public_key=valid_subscription_data['public_key']
        )
        saved_subscription_serializer = SubscriptionSerializer(instance=subscription_object)
        return saved_subscription_serializer
