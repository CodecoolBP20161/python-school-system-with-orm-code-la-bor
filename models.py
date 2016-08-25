from peewee import *
import random
import time


class ConnectDatabase:

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
    location = CharField()
    name = CharField()


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

    @classmethod
    def get_school_filter(cls):
        school = input("Please choose a school: 1. Budapest, 2. Miskolc, 3. Krakow: ")
        return [interview for interview in cls.select().where(cls.school == school)]

    @classmethod
    def get_filter_mentor(cls):
        mentor = input(
            "Select a Mentor for sorting users by: 1. Attila Molnár 2. Pál Monoczki 3. Sándor Szodoray " +
            "4. Dániel Salamon 5. Miklós Beöthy 6. Tamás Tompa 7. Mateusz Ostafil: ")
        return [interview for interview in cls.select().where(cls.mentor == mentor)]


class Applicant(BaseModel):
    app_code = CharField(null=True, unique=True)
    first_name = CharField()
    last_name = CharField()
    hometown = CharField()
    school = ForeignKeyField(School, null=True, default=None)
    status = CharField()
    email = CharField()
    interview = ForeignKeyField(
        Interview,
        null=True,
        default=None,
        related_name='applicants')
    reg_date = DateTimeField(null=True)

    @staticmethod
    def detect_new_applicants():
        return Applicant.select().where(Applicant.app_code >> None)

    @staticmethod
    def generate_app_code():
        applicants = Applicant.select().where(Applicant.app_code is not None)
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
    def str_time_prop(start, end, format, prop):
        start_time = time.mktime(time.strptime(start, format))
        end_time = time.mktime(time.strptime(end, format))
        prop_time = start_time + prop * (end_time - start_time)
        return time.strftime(format, time.localtime(prop_time))

    @staticmethod
    def random_date(start, end, prop):
        return Applicant.str_time_prop(start, end, '%Y-%m-%d %H:%M:%S', prop)

    @staticmethod
    def assign_reg_date_to_new_applicants():
        new_applicants = Applicant.select().where(Applicant.reg_date >> None)
        for applicant in new_applicants:
            applicant.reg_date = Applicant.random_date("2016-04-01 12:01:00", "2016-08-22 11:59:59", random.random())
            applicant.save()

    @staticmethod
    def assign_app_code_to_new_applicants():
        new_applicants = Applicant.detect_new_applicants()
        for applicant in new_applicants:
            applicant.app_code = Applicant.generate_app_code()
            applicant.status = 'in progress'
            applicant.save()

    @staticmethod
    def school_to_applicant():
        applicants = Applicant.select().where(Applicant.school >> None)
        for applicant in applicants:
            applicant.school = City.select().where(City.name == applicant.hometown).get().school
            applicant.school = City.select().where(
                City.name == applicant.hometown).get().school
            applicant.save()

    @classmethod
    def check_interview_date(cls):
        applicants = cls.select().where(cls.interview >> None)
        for applicant in applicants:
            applicant.interview_date_to_applicant()

    def interview_date_to_applicant(self):
        self.interview = Interview.select().where(
            Interview.available, Interview.school == self.school).get()
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

    @classmethod
    def get_filter_hometown(cls):
        hometown = str(input("Please choose a city: "))
        return [applicant for applicant in cls.select().where(cls.hometown.contains(hometown))]

    @classmethod
    def get_filter_email(cls):
        email = str(input("Please write an e-mail address: "))
        return [applicant for applicant in cls.select().where(cls.email.contains(email))]

    @classmethod
    def get_filter_status(cls):
        status = str(
            input("Choose a status (new, in-progress, waiting for interview): "))
        return [applicant for applicant in cls.select().where(cls.status.contains(status))]

    @classmethod
    def get_filter_school(cls):
        school = input(
            "Please choose a school: 1. Budapest, 2. Miskolc, 3.Krakow: ")
        return [applicant for applicant in cls.select().where(cls.school == school)]

    @classmethod
    def get_filter_status(cls):
        status = str(input("Choose a status (new, in-progress, waiting for interview): "))
        return [applicant for applicant in cls.select().where(cls.status.contains(status))]

    @classmethod
    def get_filter_school(cls):
        school = input("Please choose a school: 1. Budapest, 2. Miskolc, 3. Krakow: ")
        return [applicant for applicant in cls.select().where(cls.school == school)]

    @classmethod
    def get_filter_time(cls):
        reg_date = input("Enter a date in the following format - 2016-04-01 12:01:00: ")
        return [applicant for applicant in cls.select().where(cls.reg_date >= reg_date)]

    @classmethod
    def get_filter_mentor(cls):
        mentor = input(
            "Select a Mentor for sorting users by: 1. Attila Molnár 2. Pál Monoczki 3. Sándor Szodoray " +
            "4. Dániel Salamon 5. Miklós Beöthy 6. Tamás Tompa 7. Mateusz Ostafil: ")
        return [applicant for applicant in cls.select()
                .join(Interview, on=(cls.interview == Interview.id))
                .join(Mentor, on=(Interview.mentor == Mentor.id)).where(Mentor.id == mentor)]

    @classmethod
    def get_applicant_filter(cls):
        app_code = input("Please enter an application code: ")
        return cls.select().where(cls.app_code == app_code)


class City(BaseModel):
    name = CharField()
    school = ForeignKeyField(School, null=True, default=None)
