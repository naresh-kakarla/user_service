from rest_framework import serializers


class ClientCredentialsSerializer(serializers.Serializer):
    client_id = serializers.CharField()
    client_secret = serializers.CharField(write_only=True)


class ClientCredentialsGrantSerializer(ClientCredentialsSerializer):
    grant_type = serializers.ChoiceField(choices=["client_credentials"])


class PasswordGrantSerializer(ClientCredentialsSerializer):
    grant_type = serializers.ChoiceField(choices=["password"])
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(write_only=True)
