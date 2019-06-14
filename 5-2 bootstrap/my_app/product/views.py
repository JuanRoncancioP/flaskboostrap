import ccy
from flask import request
from werkzeug import abort
from flask import render_template
from flask import Blueprint
from my_app.product.models import PRODUCTS





product_blueprint = Blueprint('product', __name__,
        template_folder="templates",
        static_folder="static",
        static_url_path="/static"
)

#print(dir(product_blueprint));

@product_blueprint.route('/')
@product_blueprint.route('/home')
def home():
    #print(response)
    return render_template('home.html', products = PRODUCTS)

@product_blueprint.route('/product/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product = product)    

@product_blueprint.context_processor
def some_processor():
        def full_name(product):
                return '{0} / {1}'.format( product['category'], 
                product['name'])
        return {'full_name': full_name}

@product_blueprint.context_processor
def some_processor2():
        def half_name(product):
                return '{0} - {1} - context prossesor'.format( product['category'], 
                product['name'])
        return {'half_name': half_name}

@product_blueprint.context_processor
def some_processor3():
        def momentjs(timestamp):
                return momentjs
        return {'momentjs':  momentjs}



@product_blueprint.app_template_filter('full_name')
def full_name_filter(product):
        return '{0} ** {1}'.format(product['category'],
        product['name']) 

@product_blueprint.app_template_filter('format_currency')
def format_currecy_filter(amount):
        currency_code = ccy.countryccy(request.accept_languages.best [-2:])
        return '{0} {1}'.format(currency_code, amount)