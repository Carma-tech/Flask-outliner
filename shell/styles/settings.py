class Config(object):
    SECRET_KEY = 'secret key'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'

    CACHE_TYPE = 'simple'


class DevConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    SQLALCHEMY_ECHO = True

    CACHE_TYPE = 'null'

    # This allows us to test the forms from WTForm
    WTF_CSRF_ENABLED = False
    
    
    #SEND_EMAIL = False
    #SECURITY_LOGIN_USER_TEMPLATE = 'frontend/sign_in.html'
    #SECURITY_REGISTER_USER_TEMPLATE = 'frontend/create_account.html'
    # This needs to be set to implement verification code
    SECURITY_POST_REGISTER_VIEW = None
    SECURITY_USER_IDENTITY_ATTRIBUTES = ['email', 'username']
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT = '4f1WQbWEKMPv9S7p'
    SECURITY_RECOVERABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_CONFIRMABLE = False
    #SECURITY_CHANGE_URL = '/change_password'
    #SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False