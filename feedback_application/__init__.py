from flask import Flask

application = Flask(__name__)
application.config['SECRET_KEY'] = 'verysecretbytes'

from feedback_application import routes