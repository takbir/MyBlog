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
from manage import util as manage_util


class BlogHandlerTest(BaseHTTPTest):

    def get_app(self):
        return Application(url_list)

    def test_create_blog(self):
        """
        POST Testing
        """
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

    def test_get_blog_list(self):
        """
        GET Testing
        """
        response = self.fetch('/manage/blog/', method='GET')
        self.assertRegexpMatches(response.body, '^\{.*\}$')

    def test_update_blog(self):
        blog = manage_util.create_blog(title=u'测试标题2', content=u'测试内容2')
        self.set_data('blog_id', blog.id)
        body = json.dumps({
            'id': blog.id,
            'struct': {
                'title': 'aaaaaaaa'
            }
        })
        response = self.fetch('/manage/blog/', method='PUT', body=body)
        self.assertEqual(response.body, '{"status": "200"}')

    def tearDown(self):
        super(BlogHandlerTest, self).tearDown()
        blog_id = self.get_data('blog_id')
        query = Blog.delete().where(Blog.id == blog_id)
        query.execute()


if __name__ == '__main__':
    unittest.main()
