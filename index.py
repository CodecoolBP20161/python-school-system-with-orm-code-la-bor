from flask import *
from models import *


index = Blueprint('index', __name__)


@index.route('/')
def welcome():
    return render_template('navbar.html')
