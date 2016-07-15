# encoding=utf8

import pytest
import mock
from utils import is_jsonable


class TestBlogHandler(object):

    @pytest.mark.gen_test
    def test_get(self, base_url, http_client, monkeypatch, app):
        monkeypatch.setattr('db.dao.get_blog_pagination', mock.Mock(return_value=[]))
        response = yield http_client.fetch('{}{}'.format(
            base_url, app.reverse_url('manage:blog')))
        assert response.code == 200
        assert is_jsonable(response.body)
