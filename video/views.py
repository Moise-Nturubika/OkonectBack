from django.forms import Media
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from .serializers import MediaSerializer, CategorySerializer
from .models import Media, Category

@api_view(['POST'])
def saveMedia(request):
    status = { 'status': False }
    media_serializer = MediaSerializer(data=request.data)
    if media_serializer.is_valid():
        title = media_serializer.validated_data['title']
        medias = Media.objects.filter(title=title)
        if not medias:
            data = media_serializer.save()
            status = {
                'status': True,
                'message': 'Media saved succefully',
                'data': data
            }
        else:
            status = {
                'status': False,
                'message': 'Media with this title already exist'
            }
    else:
        status = {
            'status': False,
            'message': 'Media data are not valid'
        }
    return JsonResponse(status)


@api_view(['GET'])
def fecthAllMedia(request):
    print("Media")
    