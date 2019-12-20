from login.exception.base import MissingError, ParameterError


class MissingUserNameError(MissingError):

    error_code = 301
    _message = "missing user name!"


class ParameterUserPasswordError(ParameterError):

    error_code = 301
    _message = "parameter user password is wrong!"
