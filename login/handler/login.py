import datetime

import jwt

from login.driver.user import User
from login.exception.user import MissingUserNameError, ParameterUserPasswordError
from login.handler import base
from login.settings import settings


class LoginHandler(base.BaseHandler):

    def post(self):
        data = self.parse_json_body()
        user_name = data.get("user_name")
        password = data.get("password")

        user = User.find_user_by_name(user_name)
        if user is None:
            raise MissingUserNameError()
        if user.password != password:
            raise ParameterUserPasswordError()

        payload = {
            "name": user.name,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(settings.get("expiration_second", 500))
        }
        token = jwt.encode(payload, settings["secret_key"])
        # self.set_header("Authorization", token)
        self.set_secure_cookie("auth", token)
        self.finish()
