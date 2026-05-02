


class ApiClientError(Exception):
    pass


class ApiTimeoutError(ApiClientError):
    pass


class ApiStatusError(ApiClientError):
    pass


class ApiInvalidResponseError(ApiClientError):
    pass

