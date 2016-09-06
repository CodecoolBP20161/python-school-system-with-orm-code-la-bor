from flask import *
from models import *
import datetime


registration = Blueprint('registration', __name__)


@registration.route('/registration', methods=['GET'])
def get_applicant_reg():
    return render_template('registration_form.html')


@registration.route('/registration', methods=['POST'])
def add_applicant():
    reg_date = datetime.datetime.now()
    columns = ['first_name', 'last_name', 'hometown', 'email']
    data = [request.form[element] for element in columns]
    new_applicant = Applicant(first_name=data[0], last_name=data[1], hometown=data[2], email=data[3], reg_date=reg_date)
    new_applicant.save()
    return render_template('welcome.html')
