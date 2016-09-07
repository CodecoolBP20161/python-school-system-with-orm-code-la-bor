from flask import *
from models import *


list_interviews = Blueprint('list_interviews', __name__)


@list_interviews.route('/list')
def list_interview():
    applicants = Applicant.select().join(Interview)
    return render_template('list.html', applicants=applicants)


# @list_interviews.route('/list/school')
# def filter_interviews_by_school(school):
#     query = Interview.select().where(school == school)
#     return render_template('list.html', query=query)
#
#
# @list_interviews.route('/list/app_code')
# def filter_interviews_by_school(app_code):
#     query = Interview.select().where(app_code == app_code)
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
