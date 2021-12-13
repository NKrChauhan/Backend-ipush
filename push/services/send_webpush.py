import json
from pywebpush import webpush, WebPushException
from pushNotification.settings import PRIVATE_KEY

BAD_AUTHORIZATION_CODE = 410
SUBSCRIPTION_INACTIVE_ERROR_CODES = [
    BAD_AUTHORIZATION_CODE
]


class SendWebPush:
    def __init__(self, subscription_objects, notification_data):
        self.notification_data = notification_data
        self.subscription_objects = subscription_objects

    def send_web_push_to_all_subscribers(self):
        for subscription_object in self.subscription_objects:
            try:
                webpush(
                    subscription_info={
                        "endpoint": subscription_object.endpoint,
                        "keys": {
                            "p256dh": subscription_object.public_key,
                            "auth": subscription_object.auth_key
                        }},
                    data=json.dumps(self.notification_data),
                    vapid_private_key=PRIVATE_KEY,
                    vapid_claims={
                        "sub": "mailto:nitish@pushowl.com",
                    }
                )
            except WebPushException as ex:
                self.set_subscription_inactive(
                    response_code=ex.response.status_code,
                    subscription_object=subscription_object
                )
                print(f"I'm sorry can't do that: {repr(ex)}")
                if ex.response and ex.response.json():
                    extra = ex.response.json()
                    print(f"Remote service replied with a {extra.code}:{extra.errno}, {extra.message}")

    @staticmethod
    def set_subscription_inactive(response_code, subscription_object):
        if response_code in SUBSCRIPTION_INACTIVE_ERROR_CODES:
            # subscription_object.is_active = False
            subscription_object.save()
