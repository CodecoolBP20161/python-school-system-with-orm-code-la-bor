# This script can generate example data for "city" and "InterviewSlot" models.
from models import *


class GenerateData:

    @staticmethod
    def add_schools(schools):
        # from models import School
        for school in schools:
            School.create(name=school['name'], location=school['location'])

    @staticmethod
    def add_applicants(applicants):
        # from models import Applicant
        for applicant in applicants:
            Applicant.create(
                            app_code=applicant['app_code'],
                            first_name=applicant['first_name'],
                            last_name=applicant['last_name'],
                            hometown=applicant['hometown'],
                            school=applicant['school'],
                            status=applicant['status'],
                            email=applicant['email'],
                            interview=applicant['interview'],
                            reg_date=applicant['reg_date']
                            )

    @staticmethod
    def add_hometown_and_closest_school(cities):
        for city in cities:
            City.create(
                name=city['name'],
                school=city['school'])

    @staticmethod
    def add_mentors(mentors):
        # from models import Mentor
        for mentor in mentors:
            Mentor.create(
                first_name=mentor['first_name'],
                last_name=mentor['last_name'],
                school=mentor['school'],
                email=mentor['email']
            )

    @staticmethod
    def add_interview_slot(interviews):
        for interview in interviews:
            Interview.create(
                start_date=interview['start_date'],
                end_date=interview['end_date'],
                mentor=interview['mentor'],
                school=interview['school'],
                available=interview['available']
            )


def generate_data():

    schools = [
        {'name': 'CodecoolBudapest', 'location': 'Budapest'},
        {'name': 'CodecoolMiskolc', 'location': 'Miskolc'},
        {'name': 'CodecoolKrakow', 'location': 'Krakow'},
    ]

    GenerateData.add_schools(schools)

    # status: new/in progress/accepted/rejected
    applicants = [
        {'app_code': None, 'first_name': 'Dominique', 'last_name': 'Williams', 'hometown': 'Budapest', 'school': None,
            'status': 'new', 'email': 'codelabor1@gmail.com', 'interview': None, 'reg_date': None},
        {'app_code': None, 'first_name': 'Jemima', 'last_name': 'Foreman', 'hometown': 'Székesfehérvár', 'school': None,
            'status': 'new', 'email': 'codelabor1@gmail.com', 'interview': None, 'reg_date': None},
        {'app_code': None, 'first_name': 'Zeph', 'last_name': 'Massey', 'hometown': 'Esztergom', 'school': None,
            'status': 'new', 'email': 'codelabor1@gmail.com', 'interview': None, 'reg_date': None},
        {'app_code': None, 'first_name': 'Joseph', 'last_name': 'Crawford', 'hometown': 'Szentendre', 'school': None,
            'status': 'new', 'email': 'codelabor1@gmail.com', 'interview': None, 'reg_date': None},
        {'app_code': None, 'first_name': 'Ifeoma', 'last_name': 'Bird', 'hometown': 'Miskolc', 'school': None,
            'status': 'new', 'email': 'codelabor1@gmail.com', 'interview': None, 'reg_date': None},
        {'app_code': None, 'first_name': 'Arsenio', 'last_name': 'Matthews', 'hometown': 'Debrecen', 'school': None,
            'status': 'new', 'email': 'codelabor1@gmail.com', 'interview': None, 'reg_date': None},
        {'app_code': None, 'first_name': 'Jemima', 'last_name': 'Cantu', 'hometown': 'Eger', 'school': None,
            'status': 'new', 'email': 'codelabor1@gmail.com', 'interview': None, 'reg_date': None},
        {'app_code': None, 'first_name': 'Carol', 'last_name': 'Arnold', 'hometown': 'Krakow', 'school': None,
            'status': 'new', 'email': 'codelabor1@gmail.com', 'interview': None, 'reg_date': None},
        {'app_code': None, 'first_name': 'Jane', 'last_name': 'Forbes', 'hometown': 'Warsaw', 'school': None,
            'status': 'new', 'email': 'codelabor1@gmail.com', 'interview': None, 'reg_date': None},
    ]

    GenerateData.add_applicants(applicants)

    cities = [
        {'name': 'Budapest', 'school': School.get(School.name == 'CodecoolBudapest')},
        {'name': 'Székesfehérvár', 'school': School.get(School.name == 'CodecoolBudapest')},
        {'name': 'Esztergom', 'school': School.get(School.name == 'CodecoolBudapest')},
        {'name': 'Szentendre', 'school': School.get(School.name == 'CodecoolBudapest')},
        {'name': 'Miskolc', 'school': School.get(School.name == 'CodecoolMiskolc')},
        {'name': 'Debrecen', 'school': School.get(School.name == 'CodecoolMiskolc')},
        {'name': 'Eger', 'school': School.get(School.name == 'CodecoolMiskolc')},
        {'name': 'Krakow', 'school': School.get(School.name == 'CodecoolKrakow')},
        {'name': 'Warsaw', 'school': School.get(School.name == 'CodecoolKrakow')},
    ]

    mentors = [
        {'first_name': 'Attila', 'last_name': 'Molnár', 'school': School.get(School.name == 'CodecoolMiskolc'),
            'email': 'codelabor1@gmail.com'},
        {'first_name': 'Pál', 'last_name': 'Monoczki', 'school': School.get(School.name == 'CodecoolMiskolc'),
            'email': 'codelabor1@gmail.com'},
        {'first_name': 'Sándor', 'last_name': 'Szodoray', 'school': School.get(School.name == 'CodecoolMiskolc'),
            'email': 'codelabor1@gmail.com'},
        {'first_name': 'Dániel', 'last_name': 'Salamon', 'school': School.get(School.name == 'CodecoolBudapest'),
            'email': 'codelabor1@gmail.com'},
        {'first_name': 'Miklós', 'last_name': 'Beöthy', 'school': School.get(School.name == 'CodecoolBudapest'),
            'email': 'codelabor1@gmail.com'},
        {'first_name': 'Tamás', 'last_name': 'Tompa', 'school': School.get(School.name == 'CodecoolBudapest'),
            'email': 'codelabor1@gmail.com'},
        {'first_name': 'Mateusz', 'last_name': 'Ostafil', 'school': School.get(School.name == 'CodecoolKrakow'),
            'email': 'codelabor1@gmail.com'},
    ]

    GenerateData.add_mentors(mentors)

    interviews = [
        {'start_date': '2016-09-01 11:00:00', 'end_date': '2016-09-01 11:30:00',
         'mentor': Mentor.get(Mentor.id == 7), 'school': School.get(School.name == 'CodecoolKrakow'),
         'available': True},
        {'start_date': '2016-09-01 11:30:00', 'end_date': '2016-09-01 12:00:00',
         'mentor': Mentor.get(Mentor.id == 1), 'school': School.get(School.name == 'CodecoolMiskolc'),
         'available': True},
        {'start_date': '2016-09-01 12:30:00', 'end_date': '2016-09-01 13:00:00',
         'mentor': Mentor.get(Mentor.id == 2), 'school': School.get(School.name == 'CodecoolMiskolc'),
         'available': True},
        {'start_date': '2016-09-01 13:00:00', 'end_date': '2016-09-01 13:30:00',
         'mentor': Mentor.get(Mentor.id == 3), 'school': School.get(School.name == 'CodecoolMiskolc'),
         'available': True},
        {'start_date': '2016-09-02 11:00:00', 'end_date': '2016-09-02 11:30:00',
         'mentor': Mentor.get(Mentor.id == 7), 'school': School.get(School.name == 'CodecoolKrakow'),
         'available': True},
        {'start_date': '2016-09-02 11:30:00', 'end_date': '2016-09-02 12:00:00',
         'mentor': Mentor.get(Mentor.id == 5), 'school': School.get(School.name == 'CodecoolBudapest'),
         'available': True},
        {'start_date': '2016-09-02 12:00:00', 'end_date': '2016-09-02 12:30:00',
         'mentor': Mentor.get(Mentor.id == 6), 'school': School.get(School.name == 'CodecoolBudapest'),
         'available': True},
        {'start_date': '2016-09-02 12:30:00', 'end_date': '2016-09-02 13:00:00',
         'mentor': Mentor.get(Mentor.id == 4), 'school': School.get(School.name == 'CodecoolBudapest'),
         'available': True},
        {'start_date': '2016-09-02 13:00:00', 'end_date': '2016-09-02 13:30:00',
         'mentor': Mentor.get(Mentor.id == 6), 'school': School.get(School.name == 'CodecoolBudapest'),
         'available': True},
        {'start_date': '2016-09-03 13:00:00', 'end_date': '2016-09-03 13:30:00',
         'mentor': Mentor.get(Mentor.id == 6), 'school': School.get(School.name == 'CodecoolBudapest'),
         'available': True},
        {'start_date': '2016-09-03 13:00:00', 'end_date': '2016-09-03 13:30:00',
         'mentor': Mentor.get(Mentor.id == 5), 'school': School.get(School.name == 'CodecoolBudapest'),
         'available': True},
        {'start_date': '2016-09-03 13:00:00', 'end_date': '2016-09-03 13:30:00',
         'mentor': Mentor.get(Mentor.id == 4), 'school': School.get(School.name == 'CodecoolBudapest'),
         'available': True},
    ]

    GenerateData.add_interview_slot(interviews)
    # GenerateData.add_hometown_and_closest_school(cities)


