from push.models import Notification
from push.serializers.notification_serializer import NotificationSerializer


class NotificationService:
    @staticmethod
    def save_notification(title, message, action_link):
        notification_object = Notification.objects.create(
            title=title,
            message=message,
            action_link=action_link
        )
        saved_notification_serializer = NotificationSerializer(notification_object)
        return saved_notification_serializer

    @staticmethod
    def get_notification_by_id(notification_id):
        return Notification.objects.filter(id=notification_id).first()

    @staticmethod
    def set_notification_status(notification_id, status):
        notification_object = Notification.objects.filter(id=notification_id).first()
        notification_object.status = status
        notification_object.save()
