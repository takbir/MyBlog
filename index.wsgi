import tornado.wsgi
import sae
import urls
import settings

app = tornado.wsgi.WSGIApplication(urls.url_mapping, **settings.settings)

application = sae.create_wsgi_app(app)
