#! ../env/bin/python

from flask import Flask
from flask.ext.security import SQLAlchemyUserDatastore
from webassets.loaders import PythonLoader as PythonAssetsLoader

from shell.styles import assets
from shell.styles.controllers.user.models import User, Role
from shell.styles.extensions import (
    db,
    cache,
    assets_env,
    bootstrap,
    debug_toolbar,
    security
)


def create_app(object_name, env="prod"):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/
    Arguments:
        object_name: the python path of the config object,
                     e.g. appname.settings.ProdConfig
        env: The name of the current environment, e.g. prod or dev
    """

    app = Flask(__name__)

    app.config.from_object(object_name)
    app.config['ENV'] = env
    app.jinja_env.globals['project_name'] = 'Styles' 

    # initialize SQLAlchemy
    db.init_app(app)
    
    # initialize the cache
    cache.init_app(app)

    # initialize security
    ds = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, datastore=ds)
    
    # initialize bootstrap resource
    bootstrap.init_app(app)
    
    # initialize the debug tool bar
    debug_toolbar.init_app(app)

    #Import and register the different asset bundles
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().iteritems():
        assets_env.register(name, bundle)

    # register our blueprints
    from shell.styles.controllers.main import main
    app.register_blueprint(main)

    return app