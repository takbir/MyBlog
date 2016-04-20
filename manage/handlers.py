# encoding=utf8

from manage import util as manage_util
from base.handlers import BaseHandler
from utils import decorators
from tornado.web import url


class BlogHandler(BaseHandler):

    @decorators.render_json
    def get(self):
        """
        获取所有Blog列表, 支持分页
        """
        params = self.get_raw_params()
        page = params.get('page')
        item_per_page = params.get('item_per_page')
        queryset = manage_util.get_blog_pagination(page, item_per_page)
        blogs_dict = [blog.to_dict() for blog in queryset]
        return {'blogs': blogs_dict}

    @decorators.render_json
    def post(self):
        """
        创建Blog
        """
        params = self.get_raw_params()
        blog = manage_util.create_blog(**params)
        return blog.to_dict()


url_list = [
    url(r'/manage/blog/?', BlogHandler),
]
