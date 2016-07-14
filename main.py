# encoding=utf8

import tornado.ioloop
import tornado.web
import tornado.escape
import settings
import sys
import os

packages_path = os.path.join(settings.SITE_ROOT, 'packages')
sys.path.insert(0, packages_path)

import urls
from tornado.httpserver import HTTPServer
from tornado.netutil import bind_sockets


from common.log_utils import getLogger
log = getLogger('main.py')


class PageNotFoundHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("error.html")

    def post(self):
        self.render("error.html")

    def initialize(self, status_code):
        self.set_status(status_code)

if len(sys.argv) > 1:
    MAIN_SITE_PORT = int(sys.argv[1])
else:
    MAIN_SITE_PORT = settings.SITE_PORT

tornado.web.ErrorHandler = PageNotFoundHandler

if __name__ == "__main__":

    tornado.locale.load_translations(settings.settings['translations'])
    application = tornado.web.Application(urls.url_mapping, **settings.settings)

    # bind signals
    sockets = bind_sockets(MAIN_SITE_PORT)

    if not settings.DEBUG and settings.OS == 'linux':
        import tornado.process
        tornado.process.fork_processes(0)  # 0 表示按 CPU 数目创建相应数目的子进程

    server = HTTPServer(application, xheaders=True)
    server.add_sockets(sockets)
    log.debug(settings.SITE_URL)
    tornado.ioloop.IOLoop.instance().start()
