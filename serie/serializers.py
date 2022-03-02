from rest_framework import serializers
from .models import Serie, Saison, Episode

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = "__all__"
        
class SaisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saison
        fields = "__all__"
        
class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = "__all__"