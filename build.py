# This script can create the database tables based on your models

from models import *

ConnectDatabase.db.connect()
# List the tables here what you want to create...
ConnectDatabase.db.create_tables([Applicant, School, City], safe=True)
