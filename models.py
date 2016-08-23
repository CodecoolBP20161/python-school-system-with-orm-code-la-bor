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

class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, null=True, default=None)
    email = CharField()


class Interview(BaseModel):
    start_date = DateTimeField()
    end_date = DateTimeField()
    mentor = ForeignKeyField(Mentor)
    school = ForeignKeyField(School, null=True, default=None)
    available = BooleanField(default=True)

    def get_applicant(self):
        return Applicant.get(Applicant.interview == self)


class Applicant(BaseModel):
    app_code = CharField(null=True, unique=True)
    first_name = CharField()
    last_name = CharField()
    hometown = CharField()
    school = ForeignKeyField(School, null=True, default=None)
    status = CharField()
    email = CharField()
    interview = ForeignKeyField(Interview, null=True, default=None, related_name='applicants')

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

    @classmethod
    def check_interview_date(cls):
        applicants = cls.select().where(cls.interview >> None)
        for applicant in applicants:
            applicant.interview_date_to_applicant()

    def interview_date_to_applicant(self):
        self.interview = Interview.select().where(Interview.available == True, Interview.school == self.school).get()
        self.interview.available = False
        self.interview.save()
        self.status = "waiting for interview"
        self.save()

    @staticmethod
    def get_status():
        application_code = input("Please enter your application code: ")
        try:
            applicant = Applicant.get(Applicant.app_code == application_code)
            print("\n Application Details \n",
                  "\n School: ", applicant.school.name,
                  "\n Status: ", applicant.status,
                  "\n")

        except Exception as inst:
            print("Invalid application code, please try again")
            print(inst)
            Applicant.get_status()

    @staticmethod
    def get_interview_details():
        application_code = input("Please enter your application code: ")
        try:
            applicant = Applicant.get(Applicant.app_code == application_code)
            print("\n Interview Details \n",
                  "\n Name: ", applicant.first_name, applicant.last_name,
                  "\n Start: ", applicant.interview.start_date,
                  "\n End: ", applicant.interview.end_date,
                  "\n Assigned mentor: ", applicant.interview.mentor.first_name, applicant.interview.mentor.last_name,
                  "\n Location: ", applicant.interview.school.name,
                  "\n")

        except Exception as err:
            print("Invalid application code, please try again")
            print(err)
            Applicant.get_interview_details()

    @staticmethod
<<<<<<< HEAD
    def get_filter_hometown():
        hometown = input("Please choose a city:")
        try:
            for applicant in Applicant.select().where(Applicant.hometown == hometown):
                print(applicant.first_name, applicant.last_name)
        except Exception as err:
            print("Not found city, please try again")
            print(err)
            Applicant.get_filter_hometown()
=======
    def get_filter_status():
        status = str(input("Choose a status (new, in-progress, waiting for interview): "))
        try:
            for applicant in Applicant.select().where(Applicant.status == status):
                print(applicant.first_name, applicant.last_name, applicant.status)
        except Exception as err:
            print("Invalid status, please try again")
            print(err)
            Applicant.get_filter_status()
>>>>>>> 012738de85a9fce4b5cd9dff20ddf1aa03c485a7

    @staticmethod
    def get_filter_school():
        school = input("Please choose a school: 1. Budapest, 2. Miskolc, 3.Krakow: ")
        try:
            for applicant in Applicant.select().where(Applicant.school == school):
                print(applicant.first_name, applicant.last_name, applicant.school.name)
        except Exception as err:
            print("Invalid School, please try again")
            print(err)
            Applicant.get_filter_school()


class City(BaseModel):
    name = CharField()
    school = ForeignKeyField(School, null=True, default=None)
