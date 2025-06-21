from enum import Enum


class Status(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "ERROR"
    BAD_REQUEST = "BAD_REQUEST"
    UNAUTHORIZED = "UNAUTHORIZED"
    NOT_FOUND = "NOT_FOUND"


# Error Messages
ERROR_MESSAGES = {
    "USER_EMAIL_REQUIRED": "User must have an email.",
    "USER_PASSWORD_REQUIRED": "Password is required.",
    "USER_ALREADY_EXISTS": "A user with this email already exists.",
    "PASSWORD_TOO_SHORT": "Password must be at least 8 characters long.",
    "INVALID_EMAIL_FORMAT": "Enter a valid email address.",
    "PASSWORD_MISMATCH": "Passwords do not match.",
}

# Success Messages
SUCCESS_MESSAGES = {
    "USER_REGISTERED": "User registered successfully.",
    "USER_UPDATED": "User information updated successfully.",
    "USER_DELETED": "User account deleted successfully.",
}
