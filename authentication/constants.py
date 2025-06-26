from enum import Enum


class Status(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "ERROR"
    BAD_REQUEST = "BAD_REQUEST"
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"
    NOT_FOUND = "NOT_FOUND"
    CONFLICT = "CONFLICT"
    SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    TOKEN_EXPIRED = "TOKEN_EXPIRED"
    TOKEN_INVALID = "TOKEN_INVALID"


# Error Messages
ERROR_MESSAGES = {
    "INVALID_GRANT_TYPE": "Please provide a valid grant type.",
    "INVALID_CLIENT_CREDS": "Invalid client credentials.",
    "INVALID_USER_CREDS": "Invalid username or password.",
    "USER_NOT_FOUND": "No user found with the provided credentials.",
    "USER_INACTIVE": "User account is inactive.",
    "MISSING_FIELDS": "Required fields are missing.",
    "TOKEN_EXPIRED": "Your token has expired. Please login again.",
    "TOKEN_INVALID": "The provided token is invalid or malformed.",
    "PERMISSION_DENIED": "You do not have permission to perform this action.",
    "SERVER_ERROR": "An internal server error occurred. Please try again later.",
    "USERNAME_EXISTS": "Username already exists. Please choose another.",
    "EMAIL_EXISTS": "Email address is already registered.",
}


# Success Messages
SUCCESS_MESSAGES = {
    "TOKEN_SSIUED": "Access token successfully issued.",
    "LOGIN_SUCCESS": "Login successful.",
    "LOGOUT_SUCCESS": "User logged out successfully.",
    "USER_REGISTERED": "User registered successfully.",
    "TOKEN_REFRESHED": "Token refreshed successfully.",
    "PASSWORD_CHANGED": "Password changed successfully.",
    "EMAIL_VERIFIED": "Email verified successfully.",
}
