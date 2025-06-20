from django.shortcuts import render
from rest_framework import status
from utils.views import SafeAPIView
from .serializers import RegisterSerializer
from utils.response_handler import APIResponse
from . import constants


# Create your views here.
class RegisterView(SafeAPIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return APIResponse.fail(
                message=constants.Status.BAD_REQUEST,
                data=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        user = serializer.save()
        return APIResponse.success(
            message=constants.SUCCESS_MESSAGES["USER_REGISTERED"],
            data=RegisterSerializer(user).data,
            status_code=status.HTTP_201_CREATED,
        )
