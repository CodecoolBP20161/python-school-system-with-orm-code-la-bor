from peewee import *
from example_data import *

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
# db = PostgresqlDatabase('dbname', user='dbuser')


class ConnectDatabase():

    def connect_database():
        with open('connect_str.txt', "r") as f:
            return f.readline()

    connect_str = connect_database()
    db = PostgresqlDatabase(connect_str)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = ConnectDatabase.db


class School(BaseModel, GenerateData):
    location = CharField()
    school_name = CharField()
    # mentors


class Applicant(BaseModel, GenerateData):
    app_code = CharField()
    first_name = CharField()
    last_name = CharField()
    city = CharField()
    school = ForeignKeyField(School)
    status = CharField()
    email = CharField()
    # interview = ForeignKeyField(Interview)

    def detect_new_applicants(self):
        return Applicant.select().where(Applicant.app_code == NULL).get()
        # return Applicant.get(Applicant.app_code == NULL)

    def generate_app_code():
        applicants = Applicant.select().where(Applicant.app_code != NULL).get()
        while True:
            app_code = random.randrange(10000, 100000)
            exists = False
            for code in applicants.app_code:
                if app_code == code:
                    exists = True
                    return
            if exists is False:
                return app_code

    def assign_app_code_to_new_applicants():
        new_applicants = detect_new_applicants()
        for applicant in new_applicants:
            applicant.app_code = generate_app_code()


class School(BaseModel, GenerateData):
    location = CharField()
    school_name = CharField()
    # mentors


class City(BaseModel, GenerateData):
    name = CharField()
    school_name = CharField()
