from flask import *
from models import *


list_applicants = Blueprint('list_applicants', __name__)


@list_applicants.route('/list_applicants')
def list_interview():
    rows = Applicant.select().join(Interview)
    return render_template('list_applicant.html', applicants=rows)


@list_applicants.route('/list_applicants/status', methods=['GET', 'POST'])
def list_applicant_status():
    if request.method == 'POST':
        status = request.form['status']
        rows = get_rows_by_status(status)
    else:
        rows = get_rows_by_status(0)
    return render_template('list_applicant.html', applicants=rows)


def get_rows_by_status(query):
    if query == "0":
        return Applicant.select().join(Interview)
    else:
        return Applicant.select().join(Interview).where(Applicant.status == query)


@list_applicants.route('/list_applicants/reg_date', methods=['GET', 'POST'])
def list_applicant_reg_date():
    if request.method == 'POST':
        reg_date = request.form['reg_date']
        rows = get_rows_by_reg_date(reg_date)
    else:
        rows = get_rows_by_reg_date('2088-08-08')
    return render_template('list_applicant.html', applicants=rows)


def get_rows_by_reg_date(query):
    if query == "":
        return Applicant.select().join(Interview)
    else:
        return Applicant.select().join(Interview).where(Applicant.reg_date >= query)


@list_applicants.route('/list_applicants/hometown', methods=['GET', 'POST'])
def list_applicant_hometown():
    if request.method == 'POST':
        hometown = request.form['hometown']
        rows = get_rows_by_hometown(hometown)
    else:
        rows = get_rows_by_hometown(0)
    return render_template('list_applicant.html', applicants=rows)


def get_rows_by_hometown(query):
    if query == "":
        return Applicant.select().join(Interview)
    else:
        return Applicant.select().join(Interview).where(Applicant.hometown.contains(query))


@list_applicants.route('/list_applicants/name', methods=['GET', 'POST'])
def list_applicant_name():
    if request.method == 'POST':
        name = request.form['name']
        rows = get_rows_by_name(name)
    else:
        rows = get_rows_by_name(0)
    return render_template('list_applicant.html', applicants=rows)


def get_rows_by_name(query):
    if query == "":
        return Applicant.select().join(Interview)
    else:
        return Applicant.select().join(Interview).where(Applicant.last_name.contains(query))


@list_applicants.route('/list_applicants/email', methods=['GET', 'POST'])
def list_applicant_email():
    if request.method == 'POST':
        email = request.form['email']
        rows = get_rows_by_email(email)
    else:
        rows = get_rows_by_email(0)
    return render_template('list_applicant.html', applicants=rows)


def get_rows_by_email(query):
    if query == "":
        return Applicant.select().join(Interview)
    else:
        return Applicant.select().join(Interview).where(Applicant.email.contains(query))


@list_applicants.route('/list_applicants/school', methods=['GET', 'POST'])
def list_applicant_school():
    if request.method == 'POST':
        school = request.form['school_name']
        rows = get_rows_by_school(school)
    else:
        rows = get_rows_by_school(0)
    return render_template('list_applicant.html', applicants=rows)


def get_rows_by_school(query):
    if query == "0":
        return Applicant.select().join(Interview)
    else:
        return Applicant.select().join(Interview).join(School).where(School.name.contains(query))


@list_applicants.route('/list_applicants/mentor', methods=['GET', 'POST'])
def list_applicant_mentor():
    if request.method == 'POST':
        mentor = request.form['mentor']
        rows = get_rows_by_mentor(mentor)
    else:
        rows = get_rows_by_mentor(0)
    return render_template('list_applicant.html', applicants=rows)


def get_rows_by_mentor(query):
    if query == "":
        return Applicant.select().join(Interview).join(Mentor)
    else:
        return Applicant.select().join(Interview).join(Mentor).where(Mentor.last_name.contains(query))
