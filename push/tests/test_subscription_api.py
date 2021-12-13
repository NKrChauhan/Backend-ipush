from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SubscriptionApiTest(APITestCase):
    def setUp(self):
        self.url = reverse('push:subscribe')

    def test_subscribe_client_api_with_valid_data(self):
        valid_subscriber_request_data = {
            "endpoint": "https://some.pushservice.com/something-unique2121000",
            "public_key": "BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
            "auth_key": "FPssNDTKnInHVndSTdbKFw=="
        }
        response_with_valid_data = self.client.post(
            path=self.url,
            data=valid_subscriber_request_data,
            format='json'
        )
        self.assertEqual(response_with_valid_data.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response_with_valid_data.data['response'], 'Invalid Data')

    def test_subscribe_client_api_with_invalid_data(self):
        invalid_subscriber_request_data = {
            "endpoint": "some.pushservice.com/something-unique2121000",
            "public_key": "BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
            "auth_key": "FPssNDTKnInHVndSTdbKFw=="
        }
        response_with_invalid_data = self.client.post(
            path=self.url,
            data=invalid_subscriber_request_data,
            format='json'
        )
        self.assertEqual(response_with_invalid_data.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_with_invalid_data.data['endpoint'][0], 'Enter a valid URL.')
