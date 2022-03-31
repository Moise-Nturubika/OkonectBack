from django.forms import Media
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from .serializers import MediaSerializer, CategorySerializer
from .models import Media, Category
from django.db.models import Q
from client.serializers import ClientSerializer
from client.models import Client

@api_view(['POST'])
def saveMedia(request):
    response = { 'status': False }
    media_serializer = MediaSerializer(data=request.data)
    if media_serializer.is_valid():
        title = media_serializer.validated_data['title']
        medias = Media.objects.filter(title=title)
        if not medias:
            data = media_serializer.save()
            print(f"{data}")
            response = {
                'status': True,
                'message': 'Media saved succefully',
                'data': {
                    'id': data.id,
                    'title': data.title,
                    'auteur': data.auteur,
                    'poster': None if data.poster == None or len(data.poster) == 0 else f'http://192.168.5.29:8000/media/{data.poster}',
                    'file': f'http://192.168.5.29:8000/media/{data.file}' if data.file != None or len(data.file) == 0  else None,
                    'dateAjout': data.dateAjout,
                    'category': {
                        'id': data.refCategory.id,
                        'designation': data.refCategory.designation
                    }
                }
            }
        else:
            response = {
                'status': False,
                'message': 'Media with this title already exist'
            }
    else:
        response = {
            'status': False,
            'message': 'Media data are not valid'
        }
    return JsonResponse(response)


@api_view(['POST'])
def updateMedia(request):
    response = { 'status': False }
    try:
        id = request.POST.get('id')
        media = Media.objects.get(pk=id)
        media_serialiser = MediaSerializer(instance=media, data=request.data, partial=True)
        if media_serialiser.is_valid():
            media_serialiser.update()
            response = {
                'status': True,
                'message': 'Media updated succefully'
            }
        else:
            response = {
                'status': False,
                'message': 'Media data are not valid'
            }
    except Media.DoesNotExist:
        response = {
            'status': False,
            'message': 'Media with this id does not exists'
        }
    return JsonResponse(response)

@api_view(['POST'])
def deleteMedia(request):
    response = { 'status': False }
    try:
        id = request.data.get('id')
        media = Media.objects.get(pk=id)
        media.delete()
        response = {
            'status': True,
            'message': 'Media deleted succefully'
        }
    except Exception as exc:
        response = {
            'status': False,
            'message': 'Error occured when attempting to delete media'
        }
    return JsonResponse(response)

@api_view(['GET'])
def fetchAllMedia(request):
    data = []
    medias = Media.objects.all()
    for media in medias:
        categ = CategorySerializer(media.refCategory)
        client = ClientSerializer(media.refClient)
        data.append(
            {
                'id': media.id,
                'title': media.title,
                'auteur': media.auteur,
                'poster': None if media.poster == None or len(media.poster) == 0 else f'http://192.168.5.29:8000/media/{media.poster}',
                'file': f'http://192.168.5.29:8000/media/{media.file}' if media.file != None or len(media.file) == 0  else None,
                'dateAjout': media.dateAjout,
                'category': categ.data,
                'client': client.data
            }
        )
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def fetchMediaById(request, **kwargs):
    response = { 'status':False }
    id = kwargs['id']
    try:
        media = Media.objects.get(pk=id)
        if media: 
            categ = CategorySerializer(media.refCategory)
            client = ClientSerializer(media.refClient)
            response = {
                'status': True,
                'data': {
                    'id': media.id,
                    'title': media.title,
                    'auteur': media.auteur,
                    'poster': None if media.poster == None or len(media.poster) == 0 else f'http://192.168.5.29:8000/media/{media.poster}',
                    'file': f'http://192.168.5.29:8000/media/{media.file}' if media.file != None or len(media.file) == 0  else None,
                    'dateAjout': media.dateAjout,
                    'category': categ.data,
                    'client': client.data
                }
            }
    except Media.DoesNotExist:
        response = {
            'status': False,
            'message': 'File with this id does not exists'
        }
    return JsonResponse(response)
    
    
@api_view(['GET'])
def fetchMediaByCategory(request, **kwargs):
    data = []
    category = kwargs['category']
    cat = Category.objects.get(pk=category)
    medias = Media.objects.filter(refCategory=cat)
    for media in medias:
        categ = CategorySerializer(media.refCategory)
        client = ClientSerializer(media.refClient)
        data.append(
            {
                'id': media.id,
                'title': media.title,
                'auteur': media.auteur,
                'poster': None if media.poster == None or len(media.poster) == 0 else f'http://192.168.5.29:8000/media/{media.poster}',
                'file': f'http://192.168.5.29:8000/media/{media.file}' if media.file != None or len(media.file) == 0  else None,
                'dateAjout': media.dateAjout,
                'category': categ.data,
                'client': client.data
            }
        )
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def fetchTopMedia(request):
    data = []
    medias = Media.objects.filter(Q(refCategory=1) | Q(refCategory=2))
    for media in medias:
        categ = CategorySerializer(media.refCategory)
        client = ClientSerializer(media.refClient)
        data.append(
            {
                'id': media.id,
                'title': media.title,
                'auteur': media.auteur,
                'poster': None if media.poster == None or len(media.poster) == 0 else f'http://192.168.5.29:8000/media/{media.poster}',
                'file': f'http://192.168.5.29:8000/media/{media.file}' if media.file != None or len(media.file) == 0  else None,
                'dateAjout': media.dateAjout,
                'category': categ.data,
                'client': client.data
            }
        )
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def fetchAllCategory(request):
    categories = Category.objects.all()
    category_serializer = CategorySerializer(categories, many=True)
    return JsonResponse(category_serializer.data, safe=False)


@api_view(['GET'])
def fetchRecentMedia(request):
    data = []
    recents = Media.objects.all().order_by('-dateAjout')[:6]
    for media in recents:
        categ = CategorySerializer(media.refCategory)
        client = ClientSerializer(media.refClient)
        data.append(
            {
                'id': media.id,
                'title': media.title,
                'auteur': media.auteur,
                'poster': None if media.poster == None or len(media.poster) == 0 else f'http://192.168.5.29:8000/media/{media.poster}',
                'file': f'http://192.168.5.29:8000/media/{media.file}' if media.file != None or len(media.file) == 0  else None,
                'dateAjout': media.dateAjout,
                'category': categ.data,
                'client': client.data
            }
        )
    return JsonResponse(data, safe=False)


@api_view(['GET'])
def fetchMediaClient(request, pk):
    id = pk
    data = []
    cl = Client.objects.get(pk=id)
    recents = Media.objects.filter(refClient=cl).order_by('-dateAjout')[:6]
    for media in recents:
        categ = CategorySerializer(media.refCategory)
        client = ClientSerializer(media.refClient)
        data.append(
            {
                'id': media.id,
                'title': media.title,
                'auteur': media.auteur,
                'poster': None if media.poster == None or len(media.poster) == 0 else f'http://192.168.5.29:8000/media/{media.poster}',
                'file': f'http://192.168.5.29:8000/media/{media.file}' if media.file != None or len(media.file) == 0  else None,
                'dateAjout': media.dateAjout,
                'category': categ.data,
                'client': client.data
            }
        )
    return JsonResponse(data, safe=False)

