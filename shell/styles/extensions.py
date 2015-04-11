from flask.ext.cache import Cache
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.security import Security
from flask_assets import Environment

#from styles.models import User

# Setup flask cache
cache = Cache()

# init flask assets
assets_env = Environment()

# flask security
security = Security()

# flask sqlalchemy
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

debug_toolbar = DebugToolbarExtension()

#login_manager = LoginManager()
#login_manager.login_view = "main.login"
#login_manager.login_message_category = "warning"


#@login_manager.user_loader
#def load_user(userid):
#    return User.query.get(userid)