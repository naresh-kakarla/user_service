
from enum import Enum

class Status(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    BAD_REQUEST = "BAD_REQUEST"
    UNAUTHORIZED = "UNAUTHORIZED"
    NOT_FOUND = "NOT_FOUND"

# Error Messages
ERROR_MESSAGES = {
    
}

# Success Messages
SUCCESS_MESSAGES = {
    "CLIENT_REGISTERED": "Client registered successfully.",
    "CLIENT_DELETED": "Client deleted successfully.",
}
