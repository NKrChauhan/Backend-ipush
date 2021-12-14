from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from push.serializers.notification_serializer import NotificationSerializer
from push.serializers.subscription_serializer import SubscriptionSerializer
from push.services.NotificationService import NotificationService
from push.services.SubscriptionService import SubscriptionService
from push.tasks import task_send_web_push
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


@api_view(['POST'])
@permission_classes([AllowAny])
def subscribe_client(request, *args, **kwargs):
    subscription_serializer = SubscriptionSerializer(data=request.data)
    if SubscriptionService.is_inactive(endpoint=subscription_serializer.initial_data['endpoint']):
        updated_subscription_object = SubscriptionService.update_subscription(
            subscription_endpoint=subscription_serializer.initial_data['endpoint'],
            auth_key=subscription_serializer.initial_data['auth_key'],
            public_key=subscription_serializer.initial_data['public_key']
        )
        updated_subscription_serializer = SubscriptionSerializer(instance=updated_subscription_object)
        return Response({
            "response": updated_subscription_serializer.data,
        },
            status=status.HTTP_200_OK
        )
    else:
        subscription_serializer.is_valid(raise_exception=True)
        saved_subscription_object = SubscriptionService.save_subscription(
            endpoint=subscription_serializer.validated_data['endpoint'],
            auth_key=subscription_serializer.validated_data['auth_key'],
            public_key=subscription_serializer.validated_data['public_key']
        )
        saved_subscription_serializer = SubscriptionSerializer(saved_subscription_object)
        return Response({
            "response": saved_subscription_serializer.data
        },
            status=status.HTTP_201_CREATED
        )


@api_view(['POST'])
@permission_classes([AllowAny])
def send_notification(request, *args, **kwargs):
    notification_serializer = NotificationSerializer(data=request.data)
    notification_serializer.is_valid(raise_exception=True)
    saved_notification_object = NotificationService.save_notification(
        title=notification_serializer.validated_data['title'],
        message=notification_serializer.validated_data['message'],
        action_link=notification_serializer.validated_data['action_link']
    )
    saved_notification_serializer = NotificationSerializer(saved_notification_object)
    logger.info('RabbitMQ enqueued task created for CELERY:')
    task_send_web_push.delay(notification_id=saved_notification_serializer.data['id'])
    return Response({
        "response": saved_notification_serializer.data
    },
        status=status.HTTP_201_CREATED
    )


@api_view(['GET'])
@permission_classes([AllowAny])
def fetch_notification_status(request, notification_id=None, *args, **kwargs):
    notification_status = NotificationService.get_notification_status(notification_id=notification_id)
    if notification_status:
        return Response({
            "status": notification_status
        },
            status=status.HTTP_200_OK
        )
    return Response({
        "status": "Send Notification Task Not Found"
    },
        status=status.HTTP_404_NOT_FOUND
    )
