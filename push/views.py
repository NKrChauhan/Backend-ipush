from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from push.serializers.notification_serializer import NotificationSerializer
from push.serializers.subscription_serializer import SubscriptionSerializer
from push.services.get_active_subscriptions import GetActiveSubscriptions
from push.services.save_notification import SaveNotification
from push.services.send_webpush import SendWebPush
from push.services.get_notification import GetNotification
from push.services.save_subscription import SaveSubscription


@api_view(['POST'])
@permission_classes([AllowAny])
def subscribe_client(request, *args, **kwargs):
    subscription_serializer = SubscriptionSerializer(data=request.data)
    if subscription_serializer.is_valid():
        saved_subscription_serializer = SaveSubscription.save_subscription(
            valid_subscription_data=subscription_serializer.validated_data
        )
        return Response({
            "response": saved_subscription_serializer.data
        },
            status=status.HTTP_201_CREATED
        )
    return Response(
        {
            "response": "Invalid Data",
            "error": subscription_serializer.errors
         },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def send_notification(request, *args, **kwargs):
    notification_serializer = NotificationSerializer(data=request.data)
    active_subscriptions = GetActiveSubscriptions.get_active_subscription()
    if notification_serializer.is_valid():
        saved_notification_serializer = SaveNotification.save_notification(
            valid_notification_data=notification_serializer.validated_data
        )
        SendWebPush(
            subscription_objects=active_subscriptions,
            notification_data=notification_serializer.validated_data
        ).send_web_push_to_all()
        return Response({
            "response": saved_notification_serializer.data
        },
            status=status.HTTP_201_CREATED
        )
    return Response({
        "response": "Invalid Data",
        "error": notification_serializer.errors
    },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@permission_classes([AllowAny])
def fetch_notification_status(request, notification_id=None, *args, **kwargs):
    notification_obj = GetNotification.get_notification_by_id(notification_id=notification_id)
    if notification_obj:
        return Response({
            "response": notification_obj.status
        },
            status=status.HTTP_200_OK
        )
    return Response({
        "response": "Send Notification Task Not Found"
    },
        status=status.HTTP_404_NOT_FOUND
    )
