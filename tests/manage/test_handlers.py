# encoding=utf8

import pytest
import mock


class TestBlogHandler(object):

    @pytest.mark.gen_test
    def test_get(self, http_client, monkeypatch, mock_session):
        monkeypatch.setattr('db.models.DBSession', mock_session)
