from peewee import *
import random

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
# db = PostgresqlDatabase('dbname', user='dbuser')


class ConnectDatabase():

    def connect_database():
        with open('connect_str.txt', "r") as f:
            return f.readline().strip()

    connect_str = connect_database()
    db = PostgresqlDatabase(connect_str)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = ConnectDatabase.db


class School(BaseModel):
    # id = PrimaryKeyField(default=None)
    location = CharField()
    name = CharField()
    # mentors

class Interview(BaseModel):
    start_date = DateTimeField()
    end_date = DateTimeField()
    mentor = CharField()
    school = ForeignKeyField(School, null=True, default=None)
    available = BooleanField(default=True)

class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, null=True, default=None)
    email = CharField()

class Applicant(BaseModel):
    app_code = CharField(null=True, unique=True)
    first_name = CharField()
    last_name = CharField()
    hometown = CharField()
    school = ForeignKeyField(School, null=True, default=None)
    status = CharField()
    email = CharField()
    interview = ForeignKeyField(Interview, null=True)

    @staticmethod
    def detect_new_applicants():
        return Applicant.select().where(Applicant.app_code >> None)
        # return Applicant.get(Applicant.app_code == NULL)

    def generate_app_code():
        applicants = Applicant.select().where(Applicant.app_code != None)
        exists = True
        while exists is True:
            new_app_code = random.randrange(10000, 100000)
            exists = False
            for applicant in applicants:
                if applicant.app_code == new_app_code:
                    exists = True
            if exists is False:
                return new_app_code

    @staticmethod
    def assign_app_code_to_new_applicants():
        new_applicants = Applicant.detect_new_applicants()
        for applicant in new_applicants:
            # new_app_code = Applicant.generate_app_code()
            applicant.app_code = Applicant.generate_app_code()
            applicant.status = 'in progress'
            applicant.save()
            # Applicant.update(Applicant.app_code == new_app_code).where(Applicant.id == applicant.id).execute()

        # return City.select(City.school_name).where(City.name == Applicant.hometown)

    @staticmethod
    def school_to_applicant():
        applicants = Applicant.select().where(Applicant.school >> None)
        for applicant in applicants:
            applicant.school = City.select().where(City.name == applicant.hometown).get().school

            # element.closest_school = element.get_closest_school_name()
            applicant.save()

    def interview_date_to_applicant():
        available = Interview.available
        if available is True:
            applicants = Applicant.select().where(Applicant.interview >> None)
            for applicant in applicants:
                applicant.interview = Interview.select().where(Interview.school == applicant.school).get()
                Interview.available = False
                applicant.save()

    @staticmethod
    def get_status():
        application_code = input("Please enter your application code: " + "\n")
        try:
            applicant = Applicant.get(Applicant.app_code == application_code)
            print("\n", applicant.status)
        except:
            print("Invalid application code, please try again")
            Applicant.get_status()

class City(BaseModel):
    name = CharField()
    school = ForeignKeyField(School, null=True, default=None)
