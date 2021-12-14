from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from push.models import Notification
from push.models.notification import COMPLETED, FAILED, IN_PROGRESS


class fetchNotificationStatus(APITestCase):
    def setUp(self):
        self.notification_object = Notification.objects.create(
            title="test Title",
            message="test Message",
            action_link="https://www.google.com"
        )
        self.url = reverse('push:fetch_notification_status', kwargs={"notification_id": self.notification_object.id})

    def test_fetch_notification_status_api_in_progress(self):
        notification_status_response = self.client.get(
            path=self.url,
        )
        self.assertEqual(notification_status_response.status_code, status.HTTP_200_OK)
        self.assertEqual(notification_status_response.data['status'], IN_PROGRESS)

    def test_fetch_notification_status_api_completed(self):
        self.notification_object.status = COMPLETED
        self.notification_object.save()
        notification_status_response = self.client.get(
            path=self.url,
        )
        self.assertEqual(notification_status_response.status_code, status.HTTP_200_OK)
        self.assertEqual(notification_status_response.data['status'], COMPLETED)

    def test_fetch_notification_status_api_failed(self):
        self.notification_object.status = FAILED
        self.notification_object.save()
        notification_status_response = self.client.get(
            path=self.url,
        )
        self.assertEqual(notification_status_response.status_code, status.HTTP_200_OK)
        self.assertEqual(notification_status_response.data['status'], FAILED)

    def test_fetch_notification_status_api_notification_notfound(self):
        self.notification_object.delete()
        notification_status_response = self.client.get(
            path=self.url,
        )
        self.assertEqual(notification_status_response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(notification_status_response.data['status'], "Send Notification Task Not Found" )
