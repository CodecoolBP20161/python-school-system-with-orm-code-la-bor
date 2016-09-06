from flask import *
from peewee import *
from build import *
from registration import *


app = Flask('School system')

app.register_blueprint(registration)


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
