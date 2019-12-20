import functools

import jwt

from login.driver.user import User


def authenticated_async(method):
    @functools.wraps(method)
    async def wrapper(self, *args, **kwargs):
        # auth = self.request.headers.get("Authorization", None)
        auth = self.get_secure_cookie("auth")
        print(auth)
        if auth:
            try:
                send_data = jwt.decode(auth, self.settings["secret_key"])
                user_name = send_data["name"]

                # 从数据库中获取到user并设置给_current_user
                user = User.find_user_by_name(user_name)
                if user:
                    self._current_user = user
                    await method(self, *args, **kwargs)

            except jwt.ExpiredSignatureError as e:
                self.set_status(401)
        else:
            self.set_status(401)
        self.finish()

    return wrapper
