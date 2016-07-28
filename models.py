from peewee import *

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
    location = CharField()
    school_name = CharField()
    # mentors


class Applicant(BaseModel):
    app_code = CharField(null=True, unique=True)
    first_name = CharField()
    last_name = CharField()
    city = CharField()
    school = ForeignKeyField(School, default=None)
    status = CharField()
    email = CharField()
    # interview = ForeignKeyField(Interview)

    @staticmethod
    def detect_new_applicants():
        return Applicant.select().where(Applicant.app_code >> None)
        # return Applicant.get(Applicant.app_code == NULL)

    def generate_app_code(self):
        self.applicants = Applicant.select().where(Applicant.app_code != NULL).get()
        exists = True
        while exists is True:
            app_code = random.randrange(10000, 100000)
            exists = False
            for code in self.applicants.app_code:
                if app_code == code:
                    exists = True
            if exists is False:
                Applicant.update(Applicant.app_code == app_code).where(Applicant.id == self.id)

    @staticmethod
    def assign_app_code_to_new_applicants():
        new_applicants = Applicant.detect_new_applicants()
        for applicant in new_applicants:
            applicant.app_code = Applicant.generate_app_code()

    def get_closest_school(self):
        return City.select(City.school_name).where(City.name == self.hometown)

    @classmethod
    def school_to_applicant(cls):
        for element in cls.select().where(cls.closest_school >> None):
            element.closest_school = element.get_closest_school_name()
            element.save()


class School(BaseModel):
    location = CharField()
    school_name = CharField()
    # mentors


class City(BaseModel):
    name = CharField()
    school_name = CharField()

print(Applicant.detect_new_applicants())
print(Applicant.assign_app_code_to_new_applicants())
