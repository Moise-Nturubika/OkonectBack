from chat.serializers import CanalSerializer, ChatSerializer
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
        chatSaved = chat_serializer.save()
        chat = ChatSerializer(chatSaved)
        status = {
            'status': True,
            'message': "Chat saved successfully",
            'data': chat.data,
        }
    else:
        status = {
            'status': False,
            'message': f"Chat data are not valid {chat_serializer.errors}"
        }
    return JsonResponse(status)

@api_view(['GET'])
def fetchAllChannels(request):
    canals = Canal.objects.all()
    canal_serializer = CanalSerializer(canals, many=True)
    return JsonResponse(canal_serializer.data, safe=False)

@api_view(['GET'])
def fetchCanalChat(request, canal):
    canals = Canal.objects.all()
    canal_serializer = CanalSerializer(canals, many=True)
    return JsonResponse(canal_serializer.data, safe=False)