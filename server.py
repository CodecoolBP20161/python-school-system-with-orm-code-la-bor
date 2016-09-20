from build import *
from index import *
from registration import *
from example_data import *
from list_interviews import *
from list_applicants import *
from about import *


app = Flask('School system')

app.register_blueprint(registration)
app.register_blueprint(index)
app.register_blueprint(list_interviews)
app.register_blueprint(list_applicants)
app.register_blueprint(about)


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
    generate_data()
    app.run(debug=True)
