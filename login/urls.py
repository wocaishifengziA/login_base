from login.handler import base, login

url_patterns = [
    (r"/", base.BaseHandler),
    (r"/test", base.TestHandler),
    (r"/login", login.LoginHandler)
]
