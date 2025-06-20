from enum import Enum

# Generic Status
class Status(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "ERROR"

# Error Messages
ERROR_MESSAGES = {
    "INVALID_CREDS": "Invalid username or password.",
    "UNAUTHORIZED": "You are not authorized to perform this action.",
    "NOT_FOUND": "The requested resource was not found.",
    "INTERNAL_ERROR": "An unexpected error occurred. Please try again later.",
    "VALIDATION_FAILED": "Validation Failed."
}

# Success Messages
SUCCESS_MESSAGES = {
    "USER_CREATED": "User account has been successfully created.",
    "LOGOUT_SUCCESS": "You have been logged out successfully.",
}
