from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny])
def subscribe_client(request, *args, **kwargs):
    # api logic to save the data and make client a subscriber goes here
    message = "Test"
    return JsonResponse({"response": message})
