from rest_framework import serializers
from video.models import Media
from .models import Canal, Chat

class CanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canal
        fields = "__all__"
        
        
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"
        
    # def create(self, validated_data):
    #     media = validated_data['refMedia']
    #     media = Media.objects.get(file__contains=media)
    #     chat = Chat(
    #         message = validated_data['message'],
    #         isPrivate = validated_data['phoisPrivatene'],
    #         refCanal = validated_data['refCanal'],
    #         refClient = validated_data['refClient'],
    #         refMedia = media,
    #     )
    #     chat.save()
    #     return chat
        
