# encoding=utf8

try:
    from functools import wraps
except ImportError:
    raise "No wrapper"

import tornado


def render_json(method):
    '''
    Annotation is for the handler which not implements the BaseHandler
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        output = method(self, *args, **kwargs)
        if not isinstance(output, dict):
            return output
        output.pop('self', '')
        success_json = {'status': '200'}
        success_json.update(output)
        self.write(tornado.escape.json_encode(success_json))
    return wrapper


def render_to(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        tmpl_file, params = method(self, *args, **kwargs)
        if 'self' in params:
            params.pop('self')
        self.render(tmpl_file, **params)
    return wrapper
