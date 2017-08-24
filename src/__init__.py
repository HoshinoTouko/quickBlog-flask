''' src/__init__.py '''
from flask import Flask
from .views.index import INDEX
from .views.posts import POSTS
from .views.auth import AUTH
from .views.archives import ARCHIVES

# Instance relative config
APP = Flask(__name__, instance_relative_config=True)
APP.config.from_object('config')
APP.config.from_pyfile('config.py')

# Regist blueprint
APP.register_blueprint(INDEX, url_prefix='/')
APP.register_blueprint(POSTS, url_prefix='/posts')
APP.register_blueprint(AUTH, url_prefix='')
APP.register_blueprint(ARCHIVES, url_prefix='')
