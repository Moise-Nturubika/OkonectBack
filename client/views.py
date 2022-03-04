from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .serializers import ClientSerializer
from .models import Client

@api_view(['POST'])
def saveClient(request):
    print("salut")