# -*- coding: utf-8 -*-

import os
import sys
if __name__ == '__main__':
    sys.path.insert(0, os.path.abspath(os.curdir))
    sys.path.insert(0, os.path.abspath(os.path.join(os.curdir, 'packages')))

from db import dao


def init():
    name_list = (
        u'社会',
        u'娱乐',
        u'游戏',
        u'综合',
        u'开发者',
        u'时事')
    for name in name_list:
        dao.create_tag(name=name)
