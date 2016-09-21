from flask import *


about = Blueprint('about', __name__)

@about.route('/about')
def show_about_page():
    return render_template('about.html')
