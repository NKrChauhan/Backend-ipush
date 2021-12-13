from celery.utils.log import get_task_logger
from push.services.SubscriptionService import SubscriptionService
from push.services.SendWebPushService import SendWebPushService
from push.services.NotificationService import NotificationService
from push.models.notification import COMPLETED, FAILED
from celery import shared_task

logger = get_task_logger(__name__)


@shared_task
def task_send_web_push(notification_id):
    send_web_push = SendWebPushService(notification_id=notification_id)
    active_subscriptions = SubscriptionService.get_active_subscription()
    try:
        for subscription in active_subscriptions:
            send_web_push.send_web_push(
                endpoint=subscription.endpoint,
                public_key=subscription.public_key,
                auth_key=subscription.auth_key,
            )
        NotificationService.set_notification_status(notification_id=notification_id, status=COMPLETED)
    except Exception as e:
        logger.info(e)
        NotificationService.set_notification_status(notification_id=notification_id, status=FAILED)
    finally:
        logger.info(f"{notification_id} processed ")
