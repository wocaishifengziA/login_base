from tornado.web import HTTPError


class ServerException(HTTPError):

    error_code = 100
    _message = ""

    @property
    def error_message(self):
        return self._message


class MissingError(ServerException):
    error_code = 300
    _message = "missing parameters!"


class ParameterError(ServerException):
    error_code = 400
    _message = "parameters is wrong!"
