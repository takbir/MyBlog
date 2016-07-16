# encoding=utf8

import pytest
import mock
import json
from utils import is_jsonable
from tests import helper
from exc import ExcConst, EXC_CONST_TRANSLATION


class TestBlogHandler(object):

    @pytest.mark.gen_test
    def test_get(self, base_url, http_client, monkeypatch, app):
        monkeypatch.setattr('db.dao.get_blog_pagination', mock.Mock(return_value=[]))
        response = yield http_client.fetch('{}{}'.format(
            base_url, app.reverse_url('manage:blog')))
        assert response.code == 200
        assert is_jsonable(response.body)

    @pytest.mark.gen_test
    def test_post(self, base_url, http_client, monkeypatch, app):
        fake_blog = helper.gen_fake_blog()
        raw_blog = fake_blog.to_dict()
        raw_blog.pop('id')
        raw_blog.pop('created')
        raw_blog.pop('updated')
        blog_id = fake_blog.id
        monkeypatch.setattr('db.dao.create_obj',
                            mock.Mock(return_value=fake_blog))
        response = yield http_client.fetch(
            '{}{}'.format(base_url, app.reverse_url('manage:blog')),
            method='POST', body=json.dumps(raw_blog))
        assert response.code == 200
        assert is_jsonable(response.body)
        data = json.loads(response.body)
        assert data.get('id') == blog_id

    @pytest.mark.gen_test
    def test_put(self, base_url, http_client, monkeypatch, app):
        monkeypatch.setattr('db.dao.get_one_record', mock.Mock(return_value=True))
        monkeypatch.setattr('db.dao.update_obj', mock.Mock())
        response = yield http_client.fetch(
            '{}{}'.format(base_url, app.reverse_url('manage:blog')),
            method='PUT', body=json.dumps({'id': '123', 'struct': {}}))
        assert response.code == 200

    @pytest.mark.gen_test
    def test_put_with_id_not_found(self, base_url, http_client, monkeypatch, app):
        monkeypatch.setattr('db.dao.get_one_record', mock.Mock(return_value=None))
        response = yield http_client.fetch(
            '{}{}'.format(base_url, app.reverse_url('manage:blog')),
            method='PUT', body='{"id": 123}')
        assert response.code == 200
        data = json.loads(response.body)
        assert data.get('status') == 'failed'
        assert data.get('msg') == EXC_CONST_TRANSLATION.get(ExcConst.BLOG_NOT_FOUND)
