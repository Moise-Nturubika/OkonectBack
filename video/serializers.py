from rest_framework import serializers
from .models import Category, Media

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"
        
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.auteur = validated_data.get('auteur', instance.auteur)
        instance.poster = validated_data.get('poster', instance.poster)
        instance.file = validated_data.get('file', instance.file)
        instance.dateAjout = validated_data.get('dateAjout', instance.dateAjout)
        instance.refCategory = validated_data.get('refCategory', instance.refCategory)
        instance.save()
        return instance

