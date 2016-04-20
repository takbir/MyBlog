# encoding=utf8

from base.handlers import BaseHandler
from tornado.web import url


class IndexHandler(BaseHandler):

    def get(self):
        self.write('Hello world! -- from Tornado')


url_list = [
    url(r'/', IndexHandler),
]
