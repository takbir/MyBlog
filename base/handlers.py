# encoding=utf8

from tornado.web import RequestHandler
import json


class BaseHandler(RequestHandler):

    def get_raw_params(self):
        if self.request.body:
            return json.loads(self.request.body)
        return {}
