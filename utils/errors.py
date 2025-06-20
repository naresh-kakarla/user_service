from rest_framework import status
from config import constants


class APIError(Exception):
    def __init__(self, message, data=None, status_code=status.HTTP_400_BAD_REQUEST):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.data = data or {}

    def to_dict(self):
        return {
            "status": constants.Status.FAILURE,
            "status_code": self.status_code,
            "message": self.message,
            "data": self.data,
        }
