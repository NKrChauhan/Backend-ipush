import json
from pywebpush import webpush, WebPushException
from pushNotification.settings import PRIVATE_KEY


def send_web_push(subscription_object, notification_data):
    try:
        webpush(
            subscription_info={
                "endpoint": subscription_object.endpoint,
                "keys": {
                    "p256dh": subscription_object.public_key,
                    "auth": subscription_object.auth_key
                }},
            data=json.dumps(notification_data),
            vapid_private_key=PRIVATE_KEY,
            vapid_claims={
                "sub": "mailto:nitish@pushowl.com",
            }
        )
    except WebPushException as ex:
        if ex.response.status_code == 410:
            subscription_object.is_active = False
            subscription_object.save()
        print(f"I'm sorry can't do that: {repr(ex)}")
        if ex.response and ex.response.json():
            extra = ex.response.json()
            print(f"Remote service replied with a {extra.code}:{extra.errno}, {extra.message}")
