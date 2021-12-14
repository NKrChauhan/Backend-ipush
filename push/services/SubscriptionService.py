from push.models import Subscription


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
        return subscription_object

    @staticmethod
    def set_subscription_inactive(subscription_object):
        subscription_object.is_active = False
        subscription_object.save()

    @staticmethod
    def update_subscription(subscription_endpoint, auth_key, public_key):
        subscription_object = Subscription.objects.filter(
            endpoint=subscription_endpoint
        ).first()
        subscription_object.auth_key = auth_key
        subscription_object.public_key = public_key
        subscription_object.is_active = True
        subscription_object.save()
        return subscription_object

    @staticmethod
    def is_inactive(endpoint):
        return Subscription.objects.filter(is_active=False, endpoint=endpoint).exists()
