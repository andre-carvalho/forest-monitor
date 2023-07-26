from flask import Flask
from flask_bcrypt import Bcrypt
from forest_monitor.blueprint import blueprint

flask_bcrypt = Bcrypt()

def create_app(config):
    app = Flask(__name__)

    with app.app_context():
        app.config.from_object(config)
        app.register_blueprint(blueprint)
        flask_bcrypt.init_app(app)

    return app
