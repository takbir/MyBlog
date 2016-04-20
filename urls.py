# encoding=utf8

__all__ = ['url_mapping']

from common.importlib import import_module


url_mapping = []

_views = (
    'index.handlers',
)


def load_urls():
    url_list = []
    # 扫描所有views
    for _view in _views:
        module = import_module(_view)
        if hasattr(module, 'url_list'):
            urls = module.url_list
            url_list.extend(urls)
    return url_list

url_mapping.extend(load_urls())
