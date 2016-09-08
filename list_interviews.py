from flask import *
from models import *


list_interviews = Blueprint('list_interviews', __name__)


@list_interviews.route('/list', methods=['GET', 'POST'])
def list_interview():
    rows = Applicant.select().join(Interview)
    return render_template('list.html', applicants=rows)


@list_interviews.route('/list/school', methods=['GET', 'POST'])
def list_interview_school():
    if request.method == 'POST':
        school_name = request.form['school_name']
        rows = get_rows_by_school_id(school_name)
    else:
        rows = get_rows_by_school_id(0)
    return render_template('list.html', applicants=rows)


def get_rows_by_school_id(query):
    if query == "0":
        return Applicant.select().join(Interview)
    else:
        return Applicant.select().join(Interview).where(Applicant.school == query)


@list_interviews.route('/list/app_code', methods=['GET', 'POST'])
def list_interview_app_code():
    if request.method == 'POST':
        app_code = request.form['app_code']
        rows = get_applicant_by_app_code(app_code)
    else:
        rows = get_applicant_by_app_code(0)
    return render_template('list.html', applicants=rows)


def get_applicant_by_app_code(query):
    if query == "":
        return Applicant.select().join(Interview)
    else:
        return Applicant.select().join(Interview).where(Applicant.app_code == query)


@list_interviews.route('/list/mentor', methods=['GET', 'POST'])
def list_interview_mentor():
    if request.method == 'POST':
        mentor = request.form['mentor']
        rows = get_applicant_by_mentor(mentor)
    else:
        rows = get_applicant_by_mentor(0)
    return render_template('list.html', applicants=rows)


def get_applicant_by_mentor(query):
    if query == "":
        return Applicant.select().join(Interview).join(Mentor)
    else:
        return Applicant.select().join(Interview).join(Mentor).where(Mentor.last_name == query)


@list_interviews.route('/filter')
def get_filter():
    return render_template('filter.html')
