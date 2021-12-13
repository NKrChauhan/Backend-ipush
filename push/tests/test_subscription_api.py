from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from push.models import Subscription


class SubscriptionApiTest(APITestCase):
    def setUp(self):
        self.url = reverse('push:subscribe')
        self.subscription_object = Subscription.objects.create(
            endpoint="https://some.pushservice.com/",
            public_key="BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
            auth_key="FPssNDTKnInHVndSTdbKFw==",
            is_active=False
        )

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

    def test_subscribe_client_api_update_inactive_subscription(self):
        valid_subscriber_request_data = {
            "endpoint": "https://some.pushservice.com/",
            "public_key": "BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
            "auth_key": "FPssNDTKnInHVndSTdbKFw==Tw"
        }
        response_with_valid_data = self.client.post(
            path=self.url,
            data=valid_subscriber_request_data,
            format='json'
        )
        self.subscription_object = Subscription.objects.get(endpoint="https://some.pushservice.com/")
        self.assertEqual(response_with_valid_data.status_code, status.HTTP_200_OK)
        self.assertEqual(self.subscription_object.auth_key, "FPssNDTKnInHVndSTdbKFw==Tw")
        self.assertEqual(self.subscription_object.is_active, True)
