from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import SubscriptionSerializer


def rearrange_subscription_data(subscription_data) -> dict:
    rearranged_subscription_data = dict()
    rearranged_subscription_data["endpoint"] = subscription_data["endpoint"]
    rearranged_subscription_data["public_key"] = subscription_data["keys"]["p256dh"]
    rearranged_subscription_data["auth_key"] = subscription_data["keys"]["auth"]
    return rearranged_subscription_data


@api_view(['POST'])
@parser_classes([JSONParser])
@permission_classes([AllowAny])
def subscribe_client(request, *args, **kwargs):
    subscription_data = rearrange_subscription_data(request.data)
    subscription_serializer = SubscriptionSerializer(data=subscription_data)
    if subscription_serializer.is_valid():
        subscription_serializer.save()
        return Response({"response": subscription_serializer.data}, status=status.HTTP_200_OK)
    return Response({"response": "Invalid Data"}, status=status.HTTP_200_OK)
