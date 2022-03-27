from chat.serializers import ChatSerializer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
# from .serializers import MediaSerializer, CategorySerializer
from .models import Canal, Chat
from django.db.models import Q
from client.serializers import ClientSerializer


@api_view(['POST'])
def saveChat(request):
    status = { 'status': False }
    chat_serializer = ChatSerializer(data=request.data)
    if chat_serializer.is_valid():
        chat = chat_serializer.save()
        status = {
            'status': True,
            'message': "Chat saved successfully",
            'data': chat.data,
        }
    else:
        status = {
            'status': False,
            'message': "Chat data are not valid"
        }
    return JsonResponse(status)