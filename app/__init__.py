from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig

bootstrap = Bootstrap()


# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)

def create_app(config_name):
# Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
# setting config
    from .request import configure_request
    configure_request(app)


    return app
