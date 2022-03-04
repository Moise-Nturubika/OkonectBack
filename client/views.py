from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from django.db.models import Q
from .serializers import ClientSerializer
from .models import Client

@api_view(['POST'])
def saveClient(request):
    response = { 'status': False }
    client_serializer = ClientSerializer(data=request.data)
    if client_serializer.is_valid():
        client = Client.objects.filter(
            Q(fullname=client_serializer.validated_data['fullname']) |
            Q(phone=client_serializer.validated_data['phone'])
        )
        if client:
            response = {
                'status': False,
                'message': 'User with this name and number already exists'
            }
        else:
            cl = client_serializer.save()
            cl_serializer = ClientSerializer(cl)
            response = {
                'status': True,
                'message': 'Client account created successfully',
                'data': cl_serializer.data
            }
    else:
        response = {
            'status': False,
            'message': 'Client data are not valid'
        }
    return JsonResponse(response)

@api_view(['GET'])
def fetchClientById(request, **kwargs):
    response = {'status':False}
    id = kwargs['id']
    try:
        client = Client.objects.get(pk=id)
        cl = ClientSerializer(client)
        print(f"Client ------> {cl.data}")
        if client: 
            response = {
                'status': True,
                'data': cl.data
            }
    except Client.DoesNotExist:
        response = {
            'status': False,
            'message': 'Client with this id does not exists'
        }
    return JsonResponse(response)

@api_view(['GET'])
def fetchClientByPhone(request, **kwargs):
    response = {'status':False}
    phone = kwargs['phone']
    try:
        clients = Client.objects.filter(phone=phone)
        for client in clients:
            cl = ClientSerializer(client)
            response = {
                'status': True,
                'data': cl.data
            }
    except Client.DoesNotExist:
        response = {
            'status': False,
            'message': 'Client with this id does not exists'
        }
    return JsonResponse(response)