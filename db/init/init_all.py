# -*- coding: utf-8 -*-

import os
import sys
if __name__ == '__main__':
    sys.path.insert(0, os.path.abspath(os.curdir))
    sys.path.insert(0, os.path.abspath(os.path.join(os.curdir, 'packages')))


import settings
import importlib


def _init():
    dirpath = os.path.join(settings.SITE_ROOT, 'db', 'init')
    for root, dirs, files in os.walk(dirpath):
        for file_name in files:
            if file_name.startswith('init_') and file_name.endswith('.py'):
                if file_name != 'init_all.py':
                    module = importlib.import_module(
                        'db.init.{}'.format(file_name.split('.')[0]))
                    module.init()

if __name__ == '__main__':
    _init()
