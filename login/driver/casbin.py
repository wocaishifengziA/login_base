import casbin

from login.settings import settings


class AccessBase(object):

    def __init__(self):
        self.e = casbin.Enforcer(settings["casbin"]["model"], settings["casbin"]["policy"])

    def enforce(self, sub, obj, act):
        return self.e.enforce(sub, obj, act)


access_driver = AccessBase()
