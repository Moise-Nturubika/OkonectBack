from rest_framework import serializers
from .models import Canal, Chat

class CanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canal
        fields = "__all__"
        
        
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"