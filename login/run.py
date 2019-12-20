#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Basic run script"""

import logging
import tornado
from tornado.options import options
import tornado.ioloop
import tornado.web
import tornado.concurrent

from login.settings import settings
from login.urls import url_patterns


class TornadoApplication(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    tornado.options.parse_command_line()

    app = TornadoApplication()
    app.listen(options.port)
    logging.info("start service at: {}".format(options.port))
    try:
        tornado.ioloop.IOLoop.current().start()
        logging.info("stop service")
    finally:
        logging.info("stop service")
