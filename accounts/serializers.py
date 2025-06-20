from rest_framework import serializers
from .models import UserAccount


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone_number",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = UserAccount(**validated_data)
        if password:
            user.set_password(password)

        user.save()
        return user
