# This script can generate example data for "City" and "InterviewSlot" models.
from models import *

schools = [
    {'name': 'CodecoolBudapest', 'location': 'Budapest'},
    {'name': 'CodecoolMiskolc', 'location': 'Miskolc'},
    {'name': 'CodecoolKrakkó', 'location': 'Krakkó'},
]

# status: new/in progress/accepted/rejected
applicants = [
    {'app_code': None, 'first_name': 'Dominique', 'last_name': 'Williams', 'city': 'Budapest', 'school': None,
        'status': 'new', 'email': 'dolor@laoreet.co.uk'},
    {'app_code': None, 'first_name': 'Jemima', 'last_name': 'Foreman', 'city': 'Székesfehérvár', 'school': None,
        'status': 'new', 'email': 'magna@etultrices.net'},
    {'app_code': None, 'first_name': 'Zeph', 'last_name': 'Massey', 'city': 'Esztergom', 'school': None,
        'status': 'new', 'email': 'a.feiat.lus@monculus.co.uk'},
    {'app_code': None, 'first_name': 'Joseph', 'last_name': 'Crawford', 'city': 'Szentendre', 'school': None,
        'status': 'new', 'email': 'lacinia.mattis@arcu.com'},
    {'app_code': None, 'first_name': 'Ifeoma', 'last_name': 'Bird', 'city': 'Miskolc', 'school': None,
        'status': 'new', 'email': 'diam.duis.mi@orciti.com'},
    {'app_code': None, 'first_name': 'Arsenio', 'last_name': 'Matthews', 'city': 'Debrecen', 'school': None,
        'status': 'new', 'email': 'semper.pret@mauriseu.net'},
    {'app_code': None, 'first_name': 'Jemima', 'last_name': 'Cantu', 'city': 'Eger', 'school': None,
        'status': 'new', 'email': 'et.risus@mollis.com'},
    {'app_code': None, 'first_name': 'Carol', 'last_name': 'Arnold', 'city': 'Krakkó', 'school': None,
        'status': 'new', 'email': 'dapibus.rum@litor.com'},
    {'app_code': None, 'first_name': 'Jane', 'last_name': 'Forbes', 'city': 'Varsó', 'school': None,
        'status': 'new', 'email': 'janiebaby@nimmi.edu'},

]

cities = [
    {'name': 'Budapest', 'school_city': 'Budapest'},
    {'name': 'Székesfehérvár', 'school_city': 'Budapest'},
    {'name': 'Esztergom', 'school_city': 'Budapest'},
    {'name': 'Szentendre', 'school_city': 'Budapest'},
    {'name': 'Miskolc', 'school_city': 'Miskolc'},
    {'name': 'Debrecen', 'school_city': 'Miskolc'},
    {'name': 'Eger', 'school_city': 'Miskolc'},
    {'name': 'Krakkó', 'school_city': 'Krakkó'},
    {'name': 'Varsó', 'school_city': 'Krakkó'},
]


mentors = [
    {'first_name': 'Attila', 'last_name': 'Molnár', 'school_name': 'CodecoolMiskolc',
        'email': 'attila.molnar@codecool.com'},
    {'first_name': 'Pál', 'last_name': 'Monoczki', 'school_name': 'CodecoolMiskolc',
        'email': 'pal.monoczki@codecool.com'},
    {'first_name': 'Sándor', 'last_name': 'Szodoray', 'school_name': 'CodecoolMiskolc',
        'email': 'sandor.szodoray@codecool.com'},
    {'first_name': 'Dániel', 'last_name': 'Salamon', 'school_name': 'CodecoolBudapest',
        'email': 'daniel.salamon@codecool.com'},
    {'first_name': 'Miklós', 'last_name': 'Beöthy', 'school_name': 'CodecoolBudapest',
        'email': 'miklos.beothy@codecool.com'},
    {'first_name': 'Tamás', 'last_name': 'Tompa', 'school_name': 'CodecoolBudapest',
        'email': 'tamas.tompa@codecool.com'},
    {'first_name': 'Mateusz', 'last_name': 'Ostafil', 'school_name': 'CodecoolKrakkó',
        'email': 'mateusz.ostafil@codecool.com'},
]

interviews = [
    {'start_date': '2016-09-01 11:00:00', 'end_date': '2016-09-01 11:30:00',
        'mentor': 'Mateusz Ostafil', 'school_name': 'CodecoolKrakkó', 'available': 'True'},
    {'start_date': '2016-09-01 11:30:00', 'end_date': '2016-09-01 12:00:00',
        'mentor': 'Attila Molnár', 'school_name': 'CodecoolMiskolc', 'available': 'True'},
    {'start_date': '2016-09-01 12:30:00', 'end_date': '2016-09-01 13:00:00',
        'mentor': 'Pál Monoczki', 'school_name': 'CodecoolMiskolc', 'available': 'True'},
    {'start_date': '2016-09-01 13:00:00', 'end_date': '2016-09-01 13:30:00',
        'mentor': 'Sándor Szodoray', 'school_name': 'CodecoolMiskolc', 'available': 'True'},
    {'start_date': '2016-09-02 11:00:00', 'end_date': '2016-09-02 11:30:00',
        'mentor': 'Mateusz Ostafil', 'school_name': 'CodecoolKrakkó', 'available': 'True'},
    {'start_date': '2016-09-02 11:30:00', 'end_date': '2016-09-02 12:00:00',
        'mentor': 'Miklós Beöthy', 'school_name': 'CodecoolBudapest', 'available': 'True'},
    {'start_date': '2016-09-02 12:00:00', 'end_date': '2016-09-02 12:30:00',
        'mentor': 'Tamás Tompa', 'school_name': 'CodecoolBudapest', 'available': 'True'},
    {'start_date': '2016-09-02 12:30:00', 'end_date': '2016-09-02 13:00:00',
        'mentor': 'Dániel Salamon', 'school_name': 'CodecoolBudapest', 'available': 'True'},
    {'start_date': '2016-09-02 13:00:00', 'end_date': '2016-09-02 13:30:00',
        'mentor': 'Tamás Tompa', 'school_name': 'CodecoolBudapest', 'available': 'True'},
]


class GenerateData:

    @staticmethod
    def add_schools(schools):
        # from models import School
        for school in schools:
            School.create(school_name=school['name'], location=school['location'])

    @staticmethod
    def add_applicants(applicants):
        # from models import Applicant
        for applicant in applicants:
            Applicant.create(
                            app_code=applicant['app_code'],
                            first_name=applicant['first_name'],
                            last_name=applicant['last_name'],
                            city=applicant['city'],
                            school=applicant['school'],
                            status=applicant['status'],
                            email=applicant['email']
                            #interview=interviews['interview']
                            )

    @staticmethod
    def get_closest_school():
        for city in cities:
            City.create(
                        name=city['name'],
                        school_city=School.select().where(School.location == city['school_city'])
                        )

    @staticmethod
    def add_mentors(mentors):
        # from models import Mentor
        for mentor in mentors:
            Mentor.create(
                        first_name=mentor['first_name'],
                        last_name=mentor['last_name'],
                        school_name=mentor['school_name']
                        )

    @staticmethod
    def get_interview():
        for interview in interviews:
            Interview.create(
                            start_date=interview['start'],
                            end_date=interview['end'],
                            mentor=interview['mentor'],
                            school_name=interview['school_name'],
                            available=interview['available']
                            )


Applicant.delete().execute()
School.delete().execute()
GenerateData.add_schools(schools)
# GenerateData.add_mentors(mentors)
GenerateData.add_applicants(applicants)


