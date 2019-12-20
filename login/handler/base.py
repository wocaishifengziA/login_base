import base64
import json

import tornado.web

from login.driver.casbin import access_driver
from login.utils.auth import authenticated_async


class BaseHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")

    def failed(self, status_code, result):
        self.set_status(status_code)
        self.finish(result)

    def parse_query_arguments(self):
        ret = {}
        for k, v in self.request.query_arguments.items():
            if isinstance(v, list) and len(v) != 0:
                if isinstance(v[0], bytes):
                    ret[k] = str(v[0], encoding='utf-8')
                else:
                    ret[k] = v[0]
            else:
                ret[k] = v
        return ret

    @classmethod
    def parse_json(cls, raw_data):
        if raw_data == b"":
            return {}
        if isinstance(raw_data, bytes):
            try:
                data = str(raw_data, encoding='utf-8')
            except Exception as e:
                return {"data": str(base64.b64encode(raw_data), encoding='utf-8')}
        else:
            data = raw_data
        data = json.loads(data)
        return data

    def parse_json_body(self):
        try:
            request_data = self.parse_json(self.request.body)
        except (KeyError, ValueError) as e:
            self.write_error(500)
            request_data = None
        return request_data


class TestHandler(BaseHandler):

    @authenticated_async
    async def get(self):
        RES = access_driver.enforce("viewer", self.request.path, self.request.method)
        print(RES)
        self.write("test!")
