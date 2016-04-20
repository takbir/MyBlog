# encoding=utf8

from tornado.testing import AsyncHTTPTestCase


class BaseHTTPTest(AsyncHTTPTestCase):

    def __init__(self, *args, **kwargs):
        super(BaseHTTPTest, self).__init__(*args, **kwargs)
        self._tmp_data = {}

    def set_data(self, k, v):
        self._tmp_data[k] = v

    def get_data(self, k):
        return self._tmp_data.get(k)
