# -*- coding: utf-8 -*-

import settings


def make_db_connect_url():
    url = 'mysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        settings.MYSQL_USER,
        settings.MYSQL_PASSWD,
        settings.MYSQL_HOST,
        settings.MYSQL_PORT,
        settings.MYSQL_DBNAME)
    return url
