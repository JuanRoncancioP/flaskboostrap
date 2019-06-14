from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from my_app.product.views import product_blueprint
from my_app.product.nav import nav
from jinja2 import Markup


class momentjs:
        def __init__(self, timestamp):
                self.timestamp = timestamp
        #wrapper to call moment.js method
        def render(self, format):
                return Markup("<script>\ndocument.write(moment(\"%s\").%s);\n</script>" % (self.timestamp.strftime("%Y-%m-%dT%H:%M:%S"), format))
        #format time
        def format(self, fmt):
                return self.render("format(\"%s\")" % fmt)

        def calendar(self):
                return self.render("calendar()")
        
        def fromNow(self):
                return self.render("fromNow()")

app = Flask(__name__)
Bootstrap(app)
app.register_blueprint(product_blueprint)
nav.init_app(app)
moment = Moment(app)
moment.init_app(app)






