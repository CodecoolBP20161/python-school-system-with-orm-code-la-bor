from flask import Flask, request, current_app
from peewee import *
from build import *


app = Flask('School system')


@app.before_request
def before_request():
    ConnectDatabase.db.connect()


@app.after_request
def after_request(response):
    ConnectDatabase.db.close()
    return response


with app.app_context():
    print(current_app.name + ' started')

if __name__ == "__main__":
    create_table()
    app.run(debug=True)
