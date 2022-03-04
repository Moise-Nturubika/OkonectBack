from django.forms import Media
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from .serializers import MediaSerializer, CategorySerializer
from .models import Media, Category

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
                    'poster': f'http://127.0.0.1:8000/media/{data.poster}',
                    'file': f'http://127.0.0.1:8000/media/{data.file}',
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
        print(f"id =========> {id}")
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
def fecthAllMedia(request):
    data = []
    medias = Media.objects.all()
    for media in medias:
        categ = CategorySerializer(media.refCategory)
        data.append(
            {
                'id': media.id,
                'title': media.title,
                'auteur': media.auteur,
                'poster': f'http://127.0.0.1:8000/media/{media.poster}',
                'file': f'http://127.0.0.1:8000/media/{media.file}',
                'dateAjout': media.dateAjout,
                'category': categ.data
            }
        )
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def fecthMediaById(request, **kwargs):
    response = {'status':False}
    id = kwargs['id']
    try:
        media = Media.objects.get(pk=id)
        if media: 
            categ = CategorySerializer(media.refCategory)
            response = {
                'status': True,
                'data': {
                    'id': media.id,
                    'title': media.title,
                    'auteur': media.auteur,
                    'poster': f'http://127.0.0.1:8000/media/{media.poster}',
                    'file': f'http://127.0.0.1:8000/media/{media.file}',
                    'dateAjout': media.dateAjout,
                    'category': categ.data
                }
            }
    except Media.DoesNotExist:
        response = {
            'status': False,
            'message': 'File with this id does not exists'
        }
    return JsonResponse(response)
    
    
@api_view(['GET'])
def fecthMediaByCategory(request, **kwargs):
    data = []
    category = kwargs['category']
    cat = Category.objects.get(pk=category)
    medias = Media.objects.filter(refCategory=cat)
    for media in medias:
        categ = CategorySerializer(media.refCategory)
        data.append(
            {
                'id': media.id,
                'title': media.title,
                'auteur': media.auteur,
                'poster': f'http://127.0.0.1:8000/media/{media.poster}',
                'file': f'http://127.0.0.1:8000/media/{media.file}',
                'dateAjout': media.dateAjout,
                'category': categ.data
            }
        )
    return JsonResponse(data, safe=False)

