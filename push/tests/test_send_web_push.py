from collections import namedtuple
from unittest import TestCase
from unittest.mock import patch
from pywebpush import WebPushException
from push.services.SendWebPushService import SendWebPushService
from push.models import Notification, Subscription

mock_response = namedtuple('response', ['status_code', 'text'])
exc_response = mock_response(status_code=410, text="")


class SendWebPushServiceTest(TestCase):
    def setUp(self):
        self.subscription_object = Subscription.objects.create(
            endpoint="https://some.pushservice.com/something-unique2121000",
            public_key="BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
            auth_key="FPssNDTKnInHVndSTdbKFw=="
        )
        self.notification_object = Notification.objects.create(
            title="testing",
            message="mocking testing",
            action_link="https://www.google.com"
        )
        self.notification_id = self.notification_object.id

    @patch('push.services.SendWebPushService.SendWebPushService.send_web_push',
           side_effect=[WebPushException(message="", response=exc_response)])
    def test_send_web_push(self, mock_webpush):
        with self.assertRaises(WebPushException):
            SendWebPushService(
                notification_id=self.notification_id,
            ).send_web_push(subscription_object=self.subscription_object)
