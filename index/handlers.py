# encoding=utf8

from base.handlers import BaseHandler
from tornado.web import url
from utils import decorators


class IndexHandler(BaseHandler):

    @decorators.render_to
    def get(self):
        return 'index/index.html', locals()


url_list = [
    url(r'/', IndexHandler),
]
