import os

from tornado.options import define

define("port", default=8000, help="run on the default port", type=int)
__BASE_DIR__ = os.path.dirname(os.path.abspath(__file__))


settings = {
    "casbin": {
        "model": os.path.join(__BASE_DIR__, "conf/model.conf"),
        "policy": os.path.join(__BASE_DIR__, "conf/policy.csv")
    },
    "secret_key": "secret",
    "mongodb": {
        "addr": "mongodb://127.0.0.1:27017",
        "db": "tornado"
    },
    "expiration_second": 10,
    "cookie_secret": "yes"
}
