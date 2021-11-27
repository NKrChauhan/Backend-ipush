from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json


class PushNotificationApiTest(APITestCase):
    def test_subscribe_client_api(self):
        url = reverse('push:subscribe')
        valid_subscriber_request_data = '{"endpoint": "https://some.pushservice.com/something-unique2121000","keys": {' \
                                  '"p256dh": ' \
                                  '"BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=","auth": "FPssNDTKnInHVndSTdbKFw=="}} '
        invalid_subscriber_request_data = '{"endpoint": "some.pushservice.com/something-unique2121000","keys": {' \
                                  '"p256dh": ' \
                                  '"BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=","auth": "FPssNDTKnInHVndSTdbKFw=="}} '
        response_with_valid_data = self.client.post(path=url, data=json.loads(valid_subscriber_request_data), format='json')
        response_with_valid_data_body = json.loads(response_with_valid_data.content)
        response_with_invalid_data = self.client.post(path=url, data=json.loads(invalid_subscriber_request_data), format='json')
        response_with_invalid_data_body = json.loads(response_with_invalid_data.content)
        self.assertEqual(response_with_valid_data.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response_with_valid_data_body['response'], 'Invalid Data')
        self.assertEqual(response_with_invalid_data.status_code, status.HTTP_200_OK)
        self.assertEqual(response_with_invalid_data_body['response'], 'Invalid Data')
