#! ../env/bin/python
import os

from flask import Flask, render_template
from flask.ext.security import SQLAlchemyUserDatastore
from webassets.loaders import PythonLoader as PythonAssetsLoader

from shell.webinterface import assets
from shell.webinterface.controllers.user.models import User, Role, Connection
from shell.webinterface.extensions import (
    db,
    cache,
    assets_env,
    bootstrap,
    debug_toolbar,
    security,
    social
)
from shell.webinterface.controllers.user import forms
from shell.webinterface.plugin.social import SQLAlchemyConnectionDatastore


def create_app(object_name, env="prod"):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/
    Arguments:
        object_name: the python path of the config object,
                     e.g. appname.settings.ProdConfig
        env: The name of the current environment, e.g. prod or dev
    """

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    app = Flask(__name__, 
        static_folder=os.path.join(BASE_DIR, 'webinterface', 'static'),
        template_folder=os.path.join(BASE_DIR, 'webinterface', 'templates')
    )

    app.config.from_object(object_name)
    app.config['ENV'] = env
    app.jinja_env.globals['project_name'] = 'Styles' 

    # register flask extensions
    register_extensions(app)

    # register our blueprints
    register_blueprints(app)
    
    register_errorhandlers(app)
    return app

def register_extensions(app):
    # initialize SQLAlchemy
    db.init_app(app)    
    # initialize the cache
    cache.init_app(app)
    
    # initialize security
    ds = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, datastore=ds,
                      register_form=forms.ExtendedRegisterForm)   
    # initialize bootstrap resource
    bootstrap.init_app(app)
    # initialize the debug tool bar
    #debug_toolbar.init_app(app)
    
    # Initialize social
    social_ds = SQLAlchemyConnectionDatastore(db, Connection)
    social.init_app(app, social_ds)
    
    #Import and register the different asset bundles
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().iteritems():
        assets_env.register(name, bundle)
    return None
    

def register_blueprints(app):
    from shell.webinterface.controllers.main import main
    app.register_blueprint(main)
    from shell.webinterface.controllers.user import user
    app.register_blueprint(user)
    return None

def register_errorhandlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template("{0}.html".format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
