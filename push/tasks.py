from celery.utils.log import get_task_logger
from push.services.get_active_subscriptions import GetActiveSubscriptions
from push.services.send_webpush import SendWebPush
from push.services.get_notification import GetNotification
from push.models.notification import COMPLETED, FAILED
from celery import shared_task

logger = get_task_logger(__name__)


@shared_task
def task_send_web_push(notification_id):
    active_subscriptions = GetActiveSubscriptions.get_active_subscription()
    notification_object = GetNotification.get_notification_by_id(notification_id=notification_id)
    try:
        SendWebPush(
            subscription_objects=active_subscriptions,
            notification_data=notification_object
        ).send_web_push_to_all_subscribers()
        notification_object.status = COMPLETED
    except Exception as e:
        logger.info(e)
        notification_object.status = FAILED
    finally:
        logger.info(f"{notification_object.id} || {notification_object.status}")
        notification_object.save()
