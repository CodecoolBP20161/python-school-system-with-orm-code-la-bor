from flask import *
from models import *


list_interviews = Blueprint('list', __name__)


@list.route('/list')
def list_inteviews():
    interviews = Interview.select()
    return render_template('list.html', interviews=interviews)


@list.route('/list/school')
def filter_interviews_by_school(school):
    query = Interview.select().where(school == school)
    return render_template('list.html', query=query)


@list.route('/list/app_code')
def filter_interviews_by_school(app_code):
    query = Interview.select().where(app_code == app_code)
    return render_template('list.html', query=query)


@list.route('/list/mentor')
def filter_interviews_by_school(mentor):
    query = Interview.select().where(mentor == mentor)
    return render_template('list.html', query=query)


@list.route('/list/reg_date')
def filter_interviews_by_school(reg_date):
    query = Interview.select().where(reg_date == reg_date)
    return render_template('list.html', query=query)
