from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json


class PushNotificationApiTest(APITestCase):
    def test_subscribe_client_api_with_valid_data(self):
        url = reverse('push:subscribe')
        valid_subscriber_request_data = {"endpoint": "https://some.pushservice.com/something-unique2121000",
                                         "public_key": "BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
                                         "auth_key": "FPssNDTKnInHVndSTdbKFw=="
                                         }
        response_with_valid_data = self.client.post(path=url, data=valid_subscriber_request_data, format='json')
        response_with_valid_data_body = json.loads(response_with_valid_data.content)
        self.assertEqual(response_with_valid_data.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response_with_valid_data_body['response'], 'Invalid Data')

    def test_subscribe_client_api_with_invalid_data(self):
        url = reverse('push:subscribe')
        invalid_subscriber_request_data = {"endpoint": "some.pushservice.com/something-unique2121000",
                                           "public_key": "BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
                                           "auth_key": "FPssNDTKnInHVndSTdbKFw=="
                                        }
        response_with_invalid_data = self.client.post(path=url, data=invalid_subscriber_request_data,format='json')
        response_with_invalid_data_body = json.loads(response_with_invalid_data.content)
        self.assertEqual(response_with_invalid_data.status_code, status.HTTP_200_OK)
        self.assertEqual(response_with_invalid_data_body['response'], 'Invalid Data')
