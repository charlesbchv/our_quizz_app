from os import environ
from Json_utils import JsonBindings, JsonModel, Nullable

# Set debug mode based on environment variable
debug = int(environ.get("FLASK_DEBUG", "0")) != 0
# Initialize JSON bindings with optional indentation
json = JsonBindings(indent=2 if debug else None)

@json.model(error=bool, message=str, code=int)
class APIException(Exception, JsonModel):
    """Custom API exception with JSON model support"""

    def __init__(self, message: str, code: int = 400):
        """Initialize with message and status code"""
        super().__init__(message)
        self.error = True
        self.message = message
        self.code = code

    @staticmethod
    def not_found(resource: str, name):
        """Create a 404 Not Found exception"""
        return APIException(f"{resource} not found: {name}", 404)

    @staticmethod
    def unauthorized(message="You must login to perform this action"):
        """Create a 401 Unauthorized exception"""
        return APIException(message, 401)

    @staticmethod
    def internal_server_error(error: Exception):
        """Create a 500 Internal Server Error exception"""
        return APIException(repr(error) if debug else "An error occurred. Please try again later!", 500)
