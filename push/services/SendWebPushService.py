import json
from pywebpush import webpush, WebPushException
from push.models import Notification
from pushNotification.settings import PRIVATE_KEY
from push.services.SubscriptionService import SubscriptionService
from celery.utils.log import get_task_logger

BAD_AUTHORIZATION_CODE = 410
NOT_FOUND = 404
SUBSCRIPTION_INACTIVE_ERROR_CODES = [
    BAD_AUTHORIZATION_CODE,
    NOT_FOUND
]

logger = get_task_logger(__name__)


class SendWebPushService:
    def __init__(self, notification_id):
        self.notification_object = Notification.objects.filter(id=notification_id).first()

    def build_request_subscription_info(self, subscription_object):
        subscription_info = {
            "endpoint": subscription_object.endpoint,
            "keys": {
                "p256dh": subscription_object.public_key,
                "auth": subscription_object.auth_key
            }}
        return subscription_info

    def build_request_notification_info(self):
        notification_info = {
            "id": self.notification_object.id,
            "title": self.notification_object.title,
            "message": self.notification_object.message,
            "action_link": self.notification_object.action_link,
            "status": self.notification_object.status,
        }
        return notification_info

    def send_web_push(self, subscription_object):
        try:
            webpush(
                self.build_request_subscription_info(subscription_object=subscription_object),
                data=json.dumps(self.build_request_notification_info()),
                vapid_private_key=PRIVATE_KEY,
                vapid_claims={
                    "sub": "mailto:nitish@pushowl.com",
                }
            )
        except WebPushException as ex:
            if ex.response.status_code in SUBSCRIPTION_INACTIVE_ERROR_CODES:
                SubscriptionService.set_subscription_inactive(
                    subscription_object=subscription_object
                )
            logger.info(f"I'm sorry can't do that: {repr(ex)}")
