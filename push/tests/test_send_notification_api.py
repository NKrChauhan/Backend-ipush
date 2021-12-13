from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SendNotificationApiTest(APITestCase):
    def setUp(self):
        self.url = reverse('push:send_notification')

    def test_send_notification_api_with_valid_notification_information(self):
        valid_notification_request_data = {
            "title": "SALE SALE!",
            "message": "OMG so good to have discounts",
            "action_link": "https://www.google.com"
        }
        response_with_valid_data = self.client.post(
            path=self.url,
            data=valid_notification_request_data,
            format='json'
        )
        self.assertEqual(response_with_valid_data.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response_with_valid_data.data['response'], 'Invalid Data')

    def test_send_notification_api_with_invalid_notification_information(self):
        valid_notification_request_data = {
            "title": "SALE SALE!",
            "message": "OMG so good to have discounts",
            "action_link": "www.google.com"
                                           }
        response_with_invalid_data = self.client.post(
            path=self.url,
            data=valid_notification_request_data,
            format='json'
        )
        self.assertEqual(response_with_invalid_data.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_with_invalid_data.data['action_link'][0], 'Enter a valid URL.')
