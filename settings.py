# encoding=utf8

import os
SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_PORT = 80
SITE_DOMAIN = '127.0.0.1'

OS = 'windows'

DEBUG = True

SECRET_KEY = '1f906fb1638ebdb01ade5f1cb55e928f8fe09fcc'

# db config
try:
    import sae.const
    MYSQL_DBNAME = sae.const.MYSQL_DB      # 数据库名
    MYSQL_USER = sae.const.MYSQL_USER    # 用户名
    MYSQL_PASSWD = sae.const.MYSQL_PASS    # 密码
    MYSQL_HOST = sae.const.MYSQL_HOST    # 主库域名（可读写）
    MYSQL_PORT = int(sae.const.MYSQL_PORT)    # 端口，类型为<type 'str'>，请根据框架要求自行转换为int
except ImportError:
    MYSQL_DBNAME = ''
    MYSQL_USER = ''
    MYSQL_PASSWD = ''
    MYSQL_HOST = ''
    MYSQL_PORT = 3306

try:
    from local_settings import *
except:
    print 'load local settings faild.'

if SITE_PORT == 80:
    SITE_URL = 'http://%s' % SITE_DOMAIN
else:
    SITE_URL = 'http://%s:%s' % (SITE_DOMAIN, SITE_PORT)

settings = dict(
    cookie_secret=SECRET_KEY,
    # login_url="/login/",
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    root_path=os.path.join(os.path.dirname(__file__)),
    xsrf_cookies=False,
    autoescape="xhtml_escape",
    debug=DEBUG,
    xheaders=True,
    translations=os.path.join(os.path.dirname(__file__), "translations"),
    # static_url_prefix='', #启用CDN后可修改此定义, 例如: "http://cdn.abc.com/static/"
)
