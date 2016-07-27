from peewee import *

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
# db = PostgresqlDatabase('dbname', user='dbuser')

class ConnectDatabase():

    @staticmethod
    def connect_database():
        with open('connect_str.txt', "r") as f:
            return f.readline()

    connect_str = connect_database()
    db = PostgresqlDatabase(connect_str)

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = ConnectDatabase.db


class Applicant(BaseModel, GenerateData):
    app_code = CharField()
    first_name = CharField()
    last_name = CharField()
    city = CharField()
    school = ForeignKeyField(School)
    status = CharField()
    email = CharField()
    interview = ForeignKeyField(Interview)

    def detect_new_applicants(self):
        return Applicant.select().where(Applicant.app_code == NULL).get()
        # return Applicant.get(Applicant.app_code == NULL)

class School(BaseModel, GenerateData):
    location = CharField()
    school_name = CharField()
    # mentors


class City(BaseModel, GenerateData):
    name = CharField()
    school_name = CharField()
