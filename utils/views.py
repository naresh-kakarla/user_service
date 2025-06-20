from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.http import Http404
from config import constants
from .errors import APIError
from .response_handler import APIResponse
import logging

logger = logging.getLogger(__name__)


class SafeAPIView(APIView):
    def handle_exception(self, exc):

        # custom APIError
        if isinstance(exc, APIError):
            return APIResponse.error(
                exec,
                status_code=getattr(exec, "status_code", status.HTTP_400_BAD_REQUEST),
            )

        # DRF Validation error
        if isinstance(exc, ValidationError):
            return APIResponse.fail(
                message=constants.ERROR_MESSAGES.VALIDATION_FAILED,
                data=exc.detail,
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        # 404 errors
        if isinstance(exc, Http404):
            return APIResponse.fail(
                message=constants.ERROR_MESSAGES.NOT_FOUND,
                status_code=status.HTTP_404_NOT_FOUND,
            )
        
        logger.exception("Unhandled exception in API View", exc_info=exc)

        # fallback for unhandled exceptions
        return APIResponse.error(
            error=exc, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
