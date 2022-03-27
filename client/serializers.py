from rest_framework import serializers
from .models import Client
from django.utils import timezone
from django.contrib.auth.hashers import make_password

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

    def create(self, validated_data):
        agent = Client(
            fullname = validated_data['fullname'],
            phone = validated_data['phone'],
            image = validated_data['image'],
            lastConnection = timezone.now(),
            password = make_password(validated_data['password']),
        )
        agent.save()
        return agent