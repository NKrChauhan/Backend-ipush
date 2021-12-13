from push.models import Subscription
from push.serializers.subscription_serializer import SubscriptionSerializer

BAD_AUTHORIZATION_CODE = 410
NOT_FOUND = 410
SUBSCRIPTION_INACTIVE_ERROR_CODES = [
    BAD_AUTHORIZATION_CODE,
    NOT_FOUND
]


class SubscriptionService:
    @staticmethod
    def get_active_subscription():
        return Subscription.objects.filter(is_active=True)

    @staticmethod
    def save_subscription(endpoint, auth_key, public_key):
        subscription_object = Subscription.objects.create(
            endpoint=endpoint,
            auth_key=auth_key,
            public_key=public_key
        )
        saved_subscription_serializer = SubscriptionSerializer(instance=subscription_object)
        return saved_subscription_serializer

    @staticmethod
    def set_subscription_inactive(response_code, subscription_endpoint):
        subscription_object = Subscription.objects.filter(endpoint=subscription_endpoint).first()
        if response_code in SUBSCRIPTION_INACTIVE_ERROR_CODES:
            # subscription_object.is_active = False
            subscription_object.save()
