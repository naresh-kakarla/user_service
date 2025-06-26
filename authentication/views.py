from django.contrib.auth import authenticate
from rest_framework import status
from clients.models import APPClient
from utils.response_handler import APIResponse
from utils.views import SafeAPIView

from . import constants
from .serializers import ClientCredentialsGrantSerializer, PasswordGrantSerializer, RefreshTokenSerializer
from .utils import TokenManager


class TokenView(SafeAPIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.token_manager = TokenManager()

    def post(self, request):
        grant_type = request.data.get("grant_type")

        if grant_type == "client_credentials":
            return self._handle_client_credentials_grant(request)
        elif grant_type == "password":
            return self._handle_password_grant(request)
        else:
            return APIResponse.fail(
                message=constants.ERROR_MESSAGES["INVALID_GRANT_TYPE"],
                data=None,
                status_code=status.HTTP_400_BAD_REQUEST,
            )

    def _handle_password_grant(self, request):
        serializer = PasswordGrantSerializer(data=request.data)

        if not serializer.is_valid():
            return APIResponse.fail(
                message=constants.Status.BAD_REQUEST,
                data=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        data = serializer.validated_data

        try:
            APPClient.objects.get(
                client_id=data["client_id"], client_secret=data["client_secret"]
            )
        except APPClient.DoesNotExist:
            return APIResponse.fail(
                message=constants.ERROR_MESSAGES["INVALID_CLIENT_CREDS"],
                data={"error": constants.ERROR_MESSAGES["INVALID_CLIENT_CREDS"]},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            return APIResponse.fail(
                message=constants.ERROR_MESSAGES["INVALID_USER_CREDS"],
                data={"error": constants.ERROR_MESSAGES["INVALID_USER_CREDS"]},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        access_token = self.token_manager.generate_access_token(
            user.username, is_client=False
        )
        refresh_token = self.token_manager.generate_refresh_token(user.username)

        return APIResponse.success(
            message=constants.SUCCESS_MESSAGES["TOKEN_SSIUED"],
            data={
                "access_token": access_token,
                "refresh_token": refresh_token,
                "expires_in": self.token_manager.access_token_expiry_seconds,
            },
            status_code=status.HTTP_200_OK,
        )

    def _handle_client_credentials_grant(self, request):
        serializer = ClientCredentialsGrantSerializer(data=request.data)

        if not serializer.is_valid():
            return APIResponse.fail(
                message=constants.Status.BAD_REQUEST,
                data=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        data = serializer.validated_data

        try:
            client = APPClient.objects.get(
                client_id=data["client_id"], client_secret=data["client_secret"]
            )
        except APPClient.DoesNotExist:
            return APIResponse.fail(
                message=constants.ERROR_MESSAGES["INVALID_CLIENT_CREDS"],
                data={"error": constants.ERROR_MESSAGES["INVALID_CLIENT_CREDS"]},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        access_token = self.token_manager.generate_access_token(
            client.client_id, is_client=True
        )

        return APIResponse.success(
            message=constants.SUCCESS_MESSAGES["TOKEN_SSIUED"],
            data={
                "access_token": access_token,
                "expires_in": self.token_manager.access_token_expiry_seconds,
            },
            status_code=status.HTTP_200_OK,
        )

class RefreshTokenView(SafeAPIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.token_manager = TokenManager()

    def post(self, request):
        serializer = RefreshTokenSerializer(data=request.data)

        if not serializer.is_valid():
            return APIResponse.fail(
                message=constants.Status.BAD_REQUEST,
                data=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        
        refresh_token = serializer.validated_data["refresh_token"]
        decoded_token = self.token_manager.decode_token(refresh_token)

        if not decoded_token or "error" in decoded_token:
            return APIResponse.fail(
                message=constants.Status.UNAUTHORIZED,
                data={"error": decoded_token.get("error", "Invalid refresh token")},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        if decoded_token.get("type") != "refresh":
            return APIResponse.fail(
                message=constants.Status.UNAUTHORIZED,
                data={"error": "Token is not a refresh token"},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        
        username = decoded_token.get("sub")

        if not username:
            return APIResponse.fail(
                message=constants.Status.UNAUTHORIZED,
                data={"error": "Invalid token payload"},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        # TODO: verify the refresh token against a DB or blacklist here

        access_token = self.token_manager.generate_access_token(username, is_client=False)
        refresh_token = self.token_manager.generate_refresh_token(username)

        return APIResponse.success(
            message=constants.SUCCESS_MESSAGES.get("TOKEN_SSIUED", "Token issued"),
            data={
                "access_token": access_token,
                "refresh_token": refresh_token,
                "expires_in": self.token_manager.access_token_expiry_seconds,
            },
            status_code=status.HTTP_200_OK,
        )


