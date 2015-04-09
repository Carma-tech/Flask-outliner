from flask import Blueprint, render_template, flash, request, redirect, url_for

from shell.styles.extensions import cache
#from appname.forms import LoginForm
#from appname.models import User

main = Blueprint('main', __name__)


@main.route('/')
@cache.cached(timeout=1000)
def home():
    return render_template('main/index.html')
