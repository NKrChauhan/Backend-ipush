from push.models import Notification
from push.models.notification import COMPLETED, FAILED


class NotificationService:
    @staticmethod
    def save_notification(title, message, action_link):
        notification_object = Notification.objects.create(
            title=title,
            message=message,
            action_link=action_link
        )
        return notification_object

    @staticmethod
    def get_notification_by_id(notification_id):
        return Notification.objects.filter(id=notification_id).first()

    @staticmethod
    def set_notification_status_complete(notification_id):
        notification_object = Notification.objects.filter(id=notification_id).first()
        notification_object.status = COMPLETED
        notification_object.save()

    @staticmethod
    def set_notification_status_failed(notification_id):
        notification_object = Notification.objects.filter(id=notification_id).first()
        notification_object.status = FAILED
        notification_object.save()

    @staticmethod
    def get_notification_status(notification_id):
        notification_object = Notification.objects.filter(id=notification_id).first()
        if notification_object:
            return notification_object.status
        return None
