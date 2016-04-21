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
        page = params.get('page', 1)
        item_per_page = params.get('item_per_page', 10)
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

    @decorators.render_json
    def put(self):
        """
        修改blog
        """
        params = self.get_raw_params()
        blog_id = params.get('id')
        struct = params.get('struct')
        blog = manage_util.get_one_blog(blog_id)
        if blog:
            manage_util.update_blog(blog, **struct)
        return {}


url_list = [
    url(r'/manage/blog/?', BlogHandler),
]
