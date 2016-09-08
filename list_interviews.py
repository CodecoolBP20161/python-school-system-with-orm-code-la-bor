from flask import *
from models import *


list_interviews = Blueprint('list_interviews', __name__)


@list_interviews.route('/list', methods=['GET', 'POST'])
def list_interview():
    if request.method == 'POST':
        school_name = request.form['School_name']
        rows = get_rows_by_school_id(school_name)
    else:
        rows = get_rows_by_school_id(0)
    return render_template('list.html', applicants=rows)


def get_rows_by_school_id(school_id):
    if school_id == "0":
        return Applicant.select().join(Interview)
    else:
        return Applicant.select().join(Interview).where(Applicant.school == school_id)


# @list_interviews.route('/list')
# def filter_interviews_by_school():
#     print(school_name)
#     applicants = Applicant.select().join(Interview).where(Applicant.school == 1)
#     return render_template('list.html', applicants=applicants)

#
# @list_interviews.route('/list/app_code')
# def filter_interviews_by_school(app_code):
#     query = Interview.select().where(Applicant.app_code == app_code)
#     return render_template('list.html', query=query)
#
#
# @list_interviews.route('/list/mentor')
# def filter_interviews_by_school(mentor):
#     query = Interview.select().where(mentor == mentor)
#     return render_template('list.html', query=query)
#
#
# @list_interviews.route('/list/reg_date')
# def filter_interviews_by_school(reg_date):
#     query = Interview.select().where(reg_date == reg_date)
#     return render_template('list.html', query=query)
