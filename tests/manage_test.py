# encoding=utf8

import os
import sys
if __name__ == '__main__':
    sys.path.insert(0, os.path.abspath(os.curdir))

import json
from tornado.test.util import unittest
from tornado.web import Application
from tests.base import BaseHTTPTest
from manage.handlers import url_list
from db.models import Blog


class BlogHandlerTest(BaseHTTPTest):

    def get_app(self):
        return Application(url_list)

    def test_create_blog(self):
        blog_struct = {
            'title': u'测试标题1',
            'content': u'测试内容1',
        }
        response = self.fetch('/manage/blog/',
                              method='POST',
                              body=json.dumps(blog_struct))
        self.assertEqual(response.code, 200)
        self.assertIn('"id":', response.body)
        struct = json.loads(response.body)
        self.set_data('blog_id', struct.get('id'))

    def tearDown(self):
        super(BlogHandlerTest, self).tearDown()
        blog_id = self.get_data('blog_id')
        query = Blog.delete().where(Blog.id == blog_id)
        query.execute()


if __name__ == '__main__':
    unittest.main()
