# encoding=utf8

from tornado.web import RequestHandler
import json


class BaseHandler(RequestHandler):

    def get_raw_params(self):
        return json.loads(self.request.body)
