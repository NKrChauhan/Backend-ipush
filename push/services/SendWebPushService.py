import json
from pywebpush import webpush, WebPushException
from push.models import Notification
from pushNotification.settings import PRIVATE_KEY
from push.services.SubscriptionService import SubscriptionService


class SendWebPushService:
    def __init__(self, notification_id):
        self.notification_object = Notification.objects.filter(id=notification_id).first()

    @staticmethod
    def make_request_subscription_info(endpoint, public_key, auth_key):
        subscription_info = {
            "endpoint": endpoint,
            "keys": {
                "p256dh": public_key,
                "auth": auth_key
            }}
        return subscription_info

    def make_request_notification_info(self):
        notification_info = {
            "id": self.notification_object.id,
            "title": self.notification_object.title,
            "message": self.notification_object.message,
            "action_link": self.notification_object.action_link,
            "status": self.notification_object.status,
        }
        return notification_info

    def send_web_push(self, endpoint, public_key, auth_key):
        try:
            webpush(
                self.make_request_subscription_info(endpoint, public_key, auth_key),
                data=json.dumps(self.make_request_notification_info()),
                vapid_private_key=PRIVATE_KEY,
                vapid_claims={
                    "sub": "mailto:nitish@pushowl.com",
                }
            )
        except WebPushException as ex:
            SubscriptionService.set_subscription_inactive(
                response_code=ex.response.status_code,
                subscription_endpoint=endpoint
            )
            print(f"I'm sorry can't do that: {repr(ex)}")
