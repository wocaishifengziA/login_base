class UserModel(object):
    def __init__(self, data):
        self._data = data

    @property
    def id(self):
        return str(self._data["_id"])

    @property
    def name(self):
        return self._data["name"]

    @property
    def password(self):
        return self._data["password"]
