from flask import Flask

application = Flask(__name__)
application.config['SECRET_KEY'] = 'fe6365a91ea361b04a497b5ee1d8faa0'

from feedback_application import routes