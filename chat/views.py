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
    data = []
    channel = Canal.objects.get(pk=canal)
    chats = Chat.objects.filter(refCanal=channel).order_by('-dateMsg')
    for chat in chats:
        # categ = CategorySerializer(media.refCategory)
        # client = ClientSerializer(media.refClient)
        data.append(
            {
                'id': chat.id,
                'message': chat.message,
                'dateMsg': chat.dateMsg,
                'isPrivate': chat.isPrivate,
                'canal': {
                    'id': chat.refCanal.id,
                    'designation': chat.refCanal.designation,
                    'description': chat.refCanal.description
                },
                'client': {
                    'id': chat.refClient.id,
                    'fullname': chat.refClient.fullname,
                    'phone': chat.refClient.phone,
                    'image': f"http://192.168.5.29:8000/media/{chat.refClient.image}"
                }
            }
        )
    return JsonResponse(data, safe=False)