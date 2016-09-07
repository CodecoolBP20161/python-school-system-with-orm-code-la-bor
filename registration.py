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
    # Applicant.handle_new_applicants()
    new_applicant.app_code = Applicant.generate_app_code()
    new_applicant.status = 'in progress'
    if new_applicant.hometown in ['Budapest', 'Székesfehérvár', 'Esztergom', 'Komárom']:
        new_applicant.school = 1
    elif new_applicant.hometown in ['Miskolc', 'Eger', 'Aggtelek']:
        new_applicant.school = 2
    elif new_applicant.hometown in ['Krakow', 'Warsaw']:
        new_applicant.school = 3
    else:
        new_applicant.school = 1
    new_applicant.save()
    Applicant.interview_date_to_applicant(new_applicant)
    # ProjectEmail.send_applicant_info(new_applicant)
    return redirect('/')

