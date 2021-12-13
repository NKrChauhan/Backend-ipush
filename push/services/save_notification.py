from push.models import Notification
from push.serializers.notification_serializer import NotificationSerializer


# TODO: correction params (single responsibility principle)
class SaveNotification:
    @staticmethod
    def save_notification(valid_notification_data):
        notification_object = Notification.objects.create(
            title=valid_notification_data['title'],
            message=valid_notification_data['message'],
            action_link=valid_notification_data['action_link']
        )
        saved_notification_serializer = NotificationSerializer(notification_object)
        return saved_notification_serializer
