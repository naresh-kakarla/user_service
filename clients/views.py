
from django.shortcuts import get_object_or_404

from rest_framework import status
from utils.views import SafeAPIView
from .serializers import APPClientSerializer
from utils.response_handler import APIResponse
from .models import APPClient
from . import constants

# Create your views here.

class RegisterAppClientView(SafeAPIView):
    def post(self, request):
        serializer = APPClientSerializer(data=request.data)

        if not serializer.is_valid():
            return APIResponse.fail(
                message=constants.Status.BAD_REQUEST,
                data=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        
        client = serializer.save()

        return APIResponse.success(
            message=constants.SUCCESS_MESSAGES["CLIENT_REGISTERED"],
            data=APPClientSerializer(client).data,
            status_code=status.HTTP_201_CREATED,
        )

class DeleteAPPClientView(SafeAPIView):
    def delete(self, request, client_name):
        client = get_object_or_404(APPClient, client_name=client_name)
        client.delete()

        return APIResponse.success(
            message=constants.SUCCESS_MESSAGES["CLIENT_DELETED"],
            data={},
            status_code=status.HTTP_204_NO_CONTENT,
        )
