# encoding=utf8

from api import util as api_utils
from base.handlers import BaseHandler
from utils import decorators
from tornado.web import url
from exc import ExcConst, EXC_CONST_TRANSLATION


class BlogHandler(BaseHandler):

    @decorators.render_json
    def get(self):
        """
        获取所有Blog列表, 支持分页
        """
        params = self.get_raw_params()
        page = params.get('page', 1)
        item_per_page = params.get('item_per_page', 10)
        queryset = api_utils.get_blog_pagination(page, item_per_page)
        blogs_dict = [blog.to_dict() for blog in queryset]
        return {'blogs': blogs_dict}

    @decorators.render_json
    def post(self):
        """
        创建Blog
        """
        params = self.get_raw_params()
        blog = api_utils.create_blog(**params)
        return {'id': blog.id}

    @decorators.render_json
    def put(self):
        """
        修改blog
        """
        params = self.get_raw_params()
        blog_id = params.get('id')
        struct = params.get('struct')
        blog = api_utils.get_one_blog(blog_id)
        if not blog:
            return {'status': 'failed',
                    'msg': EXC_CONST_TRANSLATION.get(ExcConst.BLOG_NOT_FOUND)}
        api_utils.update_blog(blog, **struct)
        return {}


url_list = [
    url(r'/api/blog/?', BlogHandler, name='api:blog'),
]
