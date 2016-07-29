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
                            email=applicant['email']
                            # interview=interviews['interview']
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
                        school_name=mentor['school']
                        )

    @staticmethod
    def get_interview():
        for interview in interviews:
            Interview.create(
                            start_date=interview['start'],
                            end_date=interview['end'],
                            mentor=interview['mentor'],
                            school_name=interview['school'],
                            available=interview['available']
                            )

schools = [
    {'name': 'CodecoolBudapest', 'location': 'Budapest'},
    {'name': 'CodecoolMiskolc', 'location': 'Miskolc'},
    {'name': 'CodecoolKrakow', 'location': 'Krakow'},
]

GenerateData.add_schools(schools)

# status: new/in progress/accepted/rejected
applicants = [
    {'app_code': None, 'first_name': 'Dominique', 'last_name': 'Williams', 'hometown': 'Budapest', 'school': None,
        'status': 'new', 'email': 'dolor@laoreet.co.uk'},
    {'app_code': None, 'first_name': 'Jemima', 'last_name': 'Foreman', 'hometown': 'Székesfehérvár', 'school': None,
        'status': 'new', 'email': 'magna@etultrices.net'},
    {'app_code': None, 'first_name': 'Zeph', 'last_name': 'Massey', 'hometown': 'Esztergom', 'school': None,
        'status': 'new', 'email': 'a.feiat.lus@monculus.co.uk'},
    {'app_code': None, 'first_name': 'Joseph', 'last_name': 'Crawford', 'hometown': 'Szentendre', 'school': None,
        'status': 'new', 'email': 'lacinia.mattis@arcu.com'},
    {'app_code': None, 'first_name': 'Ifeoma', 'last_name': 'Bird', 'hometown': 'Miskolc', 'school': None,
        'status': 'new', 'email': 'diam.duis.mi@orciti.com'},
    {'app_code': None, 'first_name': 'Arsenio', 'last_name': 'Matthews', 'hometown': 'Debrecen', 'school': None,
        'status': 'new', 'email': 'semper.pret@mauriseu.net'},
    {'app_code': None, 'first_name': 'Jemima', 'last_name': 'Cantu', 'hometown': 'Eger', 'school': None,
        'status': 'new', 'email': 'et.risus@mollis.com'},
    {'app_code': None, 'first_name': 'Carol', 'last_name': 'Arnold', 'hometown': 'Krakkó', 'school': None,
        'status': 'new', 'email': 'dapibus.rum@litor.com'},
    {'app_code': None, 'first_name': 'Jane', 'last_name': 'Forbes', 'hometown': 'Varsó', 'school': None,
        'status': 'new', 'email': 'janiebaby@nimmi.edu'},
]

GenerateData.add_applicants(applicants)

cities = [
    {'name': 'Budapest', 'school': School.get(School.name == 'CodecoolBudapest')},
    {'name': 'Székesfehérvár', 'school': School.get(School.name == 'CodecoolBudapest')},
    {'name': 'Esztergom', 'school': School.get(School.name == 'CodecoolBudapest')},
    {'name': 'Szentendre', 'school': School.get(School.name == 'CodecoolBudapest')},
    {'name': 'Miskolc', 'school': School.get(School.name =='CodecoolMiskolc')},
    {'name': 'Debrecen', 'school': School.get(School.name =='CodecoolMiskolc')},
    {'name': 'Eger', 'school': School.get(School.name =='CodecoolMiskolc')},
    {'name': 'Krakow', 'school': School.get(School.name =='CodecoolKrakow')},
    {'name': 'Warsaw', 'school': School.get(School.name == 'CodecoolKrakow')},
]

mentors = [
    {'first_name': 'Attila', 'last_name': 'Molnár', 'school': School.get(School.name == 'CodecoolMiskolc'),
        'email': 'attila.molnar@codecool.com'},
    {'first_name': 'Pál', 'last_name': 'Monoczki', 'school': School.get(School.name == 'CodecoolMiskolc'),
        'email': 'pal.monoczki@codecool.com'},
    {'first_name': 'Sándor', 'last_name': 'Szodoray', 'school': School.get(School.name == 'CodecoolMiskolc'),
        'email': 'sandor.szodoray@codecool.com'},
    {'first_name': 'Dániel', 'last_name': 'Salamon', 'school': School.get(School.name == 'CodecoolBudapest'),
        'email': 'daniel.salamon@codecool.com'},
    {'first_name': 'Miklós', 'last_name': 'Beöthy', 'school': School.get(School.name == 'CodecoolBudapest'),
        'email': 'miklos.beothy@codecool.com'},
    {'first_name': 'Tamás', 'last_name': 'Tompa', 'school': School.get(School.name == 'CodecoolBudapest'),
        'email': 'tamas.tompa@codecool.com'},
    {'first_name': 'Mateusz', 'last_name': 'Ostafil', 'school_name': School.get(School.name == 'CodecoolKrakow'),
        'email': 'mateusz.ostafil@codecool.com'},
]

interviews = [
    {'start_date': '2016-09-01 11:00:00', 'end_date': '2016-09-01 11:30:00',
        'mentor': Mentor.get(Mentor.id == 7), 'school': School.get(School.name == 'CodecoolKrakow'), 'available': True},
     {'start_date': '2016-09-01 11:30:00', 'end_date': '2016-09-01 12:00:00',
         'mentor': Mentor.get(Mentor.id == 1), 'school': School.get(School.name == 'CodecoolMiskolc'), 'available': True},
     {'start_date': '2016-09-01 12:30:00', 'end_date': '2016-09-01 13:00:00',
         'mentor': Mentor.get(Mentor.id == 2), 'school': School.get(School.name == 'CodecoolMiskolc'), 'available': True},
     {'start_date': '2016-09-01 13:00:00', 'end_date': '2016-09-01 13:30:00',
         'mentor': Mentor.get(Mentor.id == 3), 'school': School.get(School.name == 'CodecoolMiskolc'), 'available': True},
     {'start_date': '2016-09-02 11:00:00', 'end_date': '2016-09-02 11:30:00',
         'mentor': Mentor.get(Mentor.id == 7), 'school': School.get(School.name == 'CodecoolKrakow'), 'available': True},
     {'start_date': '2016-09-02 11:30:00', 'end_date': '2016-09-02 12:00:00',
         'mentor': Mentor.get(Mentor.id == 5), 'school': School.get(School.name == 'CodecoolBudapest'), 'available': True},
     {'start_date': '2016-09-02 12:00:00', 'end_date': '2016-09-02 12:30:00',
         'mentor': Mentor.get(Mentor.id == 6), 'school': School.get(School.name == 'CodecoolBudapest'), 'available': True},
     {'start_date': '2016-09-02 12:30:00', 'end_date': '2016-09-02 13:00:00',
         'mentor': Mentor.get(Mentor.id == 4), 'school': School.get(School.name == 'CodecoolBudapest'), 'available': True},
     {'start_date': '2016-09-02 13:00:00', 'end_date': '2016-09-02 13:30:00',
         'mentor': Mentor.get(Mentor.id == 6), 'school': School.get(School.name == 'CodecoolBudapest'), 'available': True},
    ]





# GenerateData.add_mentors(mentors)
GenerateData.add_hometown_and_closest_school(cities)
