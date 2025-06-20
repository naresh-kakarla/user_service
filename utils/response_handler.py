from rest_framework import status
from rest_framework.response import Response
from config import constants
from .errors import APIError


class APIResponse:
    @staticmethod
    def success(
        message=None, data=None, status_code=status.HTTP_200_OK
    ):
        return Response(
            {
                "status": constants.Status.SUCCESS,
                "message": message,
                "data": data or {},
                "status_code": status_code,
            },
            status=status_code,
        )

    @staticmethod
    def fail(
        message=constants.Status.FAILURE,
        data=None,
        status_code=status.HTTP_400_BAD_REQUEST,
    ):
        return Response(
            {
                "status": constants.Status.FAILURE,
                "message": message,
                "data": data or {},
                "status_code": status_code,
            },
            status=status_code,
        )

    @staticmethod
    def error(error, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR):
        if isinstance(error, APIError):
            return Response(APIError.to_dict(), error.status_code)

        # fallback for unexpected exceptions
        return Response(
            {
                "status": constants.Status.FAILURE,
                "message": str(error),
                "status_code": status_code,
            },
            status=status_code,
        )
