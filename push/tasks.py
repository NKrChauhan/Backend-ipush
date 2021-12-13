from celery.utils.log import get_task_logger
from push.services.SubscriptionService import SubscriptionService
from push.services.SendWebPushService import SendWebPushService
from push.services.NotificationService import NotificationService
from celery import shared_task

logger = get_task_logger(__name__)


@shared_task
def task_send_web_push(notification_id):
    send_web_push_service = SendWebPushService(notification_id=notification_id)
    active_subscriptions = SubscriptionService.get_active_subscription()
    try:
        for subscription in active_subscriptions:
            send_web_push_service.send_web_push(
                subscription_object=subscription
            )
        NotificationService.set_notification_status_complete(notification_id=notification_id)
    except Exception as e:
        logger.info(e)
        NotificationService.set_notification_status_failed(notification_id=notification_id)
    finally:
        logger.info(f"{notification_id} processed ")
