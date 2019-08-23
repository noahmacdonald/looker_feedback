from flask import Flask
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)
application = Flask(__name__)
application.config['SECRET_KEY'] = 'verysecretbytes'
csrf.init_app(application)

from feedback_application import routes