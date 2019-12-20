from login.driver.mongo import mongodb
from login.model.user import UserModel


class User(object):

    @classmethod
    def find_user_by_name(cls, name):
        res = mongodb.user.find_one({"name": name})
        if res:
            return UserModel(res)
        return None
