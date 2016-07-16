# encoding=utf8

import os
import sys
import pytest
from tornado.web import Application

packages_path = os.path.join('.', 'packages')
sys.path.insert(0, packages_path)

from urls import url_mapping


@pytest.fixture
def app():
    return Application(url_mapping, debug=False)
