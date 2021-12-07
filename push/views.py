from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import SubscriptionSerializer, NotificationSerializer
from .models import Subscription


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
        return Response({"response": notification_serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"response": "Invalid Data", "error": notification_serializer.errors}, status=status.HTTP_200_OK)
