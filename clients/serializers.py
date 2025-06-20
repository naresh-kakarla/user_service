from rest_framework import serializers
from .models import APPClient


class APPClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = APPClient
        fields = [
            "client_name",
            "description",
            "client_id",
            "client_secret",
            "created_at",
        ]
        read_only_fields = ["client_id", "client_secret", "created_at"]

    def create(self, validated_data):
        return APPClient.objects.create(**validated_data)
