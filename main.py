from models import *
from menu import *
from build import *
from example_data import *




input("Create database: ")
create_table()
input("Database imaging is in progress ⌛ ")
generate_data()

input("Hunting new applicants ☢ ")
Applicant.detect_new_applicants()
input("Applicant.assign_app_code_to_new_applicants")
Applicant.assign_app_code_to_new_applicants()
input("Applicant.school_to_applicant" + "\n")
Applicant.school_to_applicant()

input("Press enter to the main menu")
Menu.main()
# Applicant.check_interview_date()


