

class ApiClientError(Exception):
    """Base class for API client errors."""
    pass



class TimeoutError(ApiClientError):
    """Raised when a request times out."""
    pass



class ApiStatusError(ApiClientError):
    pass


class ApiInvalidResponseError(ApiClientError):
    pass
