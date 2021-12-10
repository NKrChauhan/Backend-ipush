from push.models import Subscription


class GetActiveSubscriptions:
    @staticmethod
    def get_active_subscription():
        return Subscription.objects.filter(is_active=True)