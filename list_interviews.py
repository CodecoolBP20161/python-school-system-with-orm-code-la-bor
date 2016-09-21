from flask import *
from models import *


list_interviews = Blueprint('list_interviews', __name__)


@list_interviews.route('/list_interviews')
def list_interview():
    rows = Applicant.select().join(Interview)
    return render_template('list_interview.html', applicants=rows)


@list_interviews.route('/list_interviews/school', methods=['GET', 'POST'])
def list_interview_school():
    if request.method == 'POST':
        school_name = request.form['filter']
        rows = get_rows_by_school_id(school_name)
    else:
        rows = get_rows_by_school_id(0)
    return render_template('list_interview.html', applicants=rows)


def get_rows_by_school_id(query):
    if query == "0":
        return Applicant.select().join(Interview)
    else:
        return Applicant.select().join(Interview).where(Applicant.school == query)


@list_interviews.route('/list_interviews/app_code', methods=['GET', 'POST'])
def list_interview_app_code():
    if request.method == 'POST':
        app_code = request.form['filter']
        rows = get_applicant_by_app_code(app_code)
    else:
        rows = get_applicant_by_app_code(0)
    return render_template('list_interview.html', applicants=rows)


def get_applicant_by_app_code(query):
    if query == "0":
        return Applicant.select().join(Interview)
    else:
        return Applicant.select().join(Interview).where(Applicant.app_code.contains(query))


@list_interviews.route('/list_interviews/mentor', methods=['GET', 'POST'])
def list_interview_mentor():
    if request.method == 'POST':
        mentor = request.form['filter']
        rows = get_applicant_by_mentor(mentor)
    else:
        rows = get_applicant_by_mentor(0)
    return render_template('list_interview.html', applicants=rows)


def get_applicant_by_mentor(query):
    if query == "":
        return Applicant.select().join(Interview).join(Mentor)
    else:
        return Applicant.select().join(Interview).join(Mentor).where(Mentor.last_name.contains(query))


@list_interviews.route('/list_interviews/start_date', methods=['GET', 'POST'])
def list_interview_start_date():
    if request.method == 'POST':
        start_date = request.form['filter']
        rows = get_applicant_by_start_date(start_date)
    else:
        rows = get_applicant_by_start_date('2017-08-15')
    return render_template('list_interview.html', applicants=rows)


def get_applicant_by_start_date(query):
    if query == "":
        return Applicant.select().join(Interview)
    else:
        return Applicant.select().join(Interview).where(Interview.start_date >= query)