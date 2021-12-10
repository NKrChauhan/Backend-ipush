from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import SubscriptionSerializer, NotificationSerializer
from .models import Subscription, Notification
from .utils import send_web_push, get_notification_by_id


@api_view(['POST'])
@parser_classes([JSONParser])
@permission_classes([AllowAny])
def subscribe_client(request, *args, **kwargs):
    subscription_serializer = SubscriptionSerializer(data=request.data)
    if subscription_serializer.is_valid():
        subscription_serializer.save()
        return Response({"response": subscription_serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"response": "Invalid Data", "error": subscription_serializer.errors}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def send_notification(request, *args, **kwargs):
    notification_serializer = NotificationSerializer(data=request.data)
    active_subscriptions = Subscription.objects.filter(is_active=True)
    if notification_serializer.is_valid():
        notification_serializer.save()
        for active_subscription in active_subscriptions:
            send_web_push(subscription_object=active_subscription, notification_data=notification_serializer.validated_data)
        return Response({"response": notification_serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"response": "Invalid Data", "error": notification_serializer.errors}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def fetch_notification_status(request, notification_id=None, *args, **kwargs):
    notification_obj = get_notification_by_id(notification_id=notification_id)
    if notification_obj:
        return Response({"response": notification_obj.status}, status=status.HTTP_200_OK)
    return Response({"response": "Send Notification Task Not Found"}, status=status.HTTP_404_NOT_FOUND)
