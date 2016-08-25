from models import *
from menu import *
from build import *
from example_data import *


input("Creating tables...  ")
create_table()
input("Database imaging is in progress... ⌛ ")
generate_data()
input("Hunting new applicants and generating application codes for them... ☢")
Applicant.assign_app_code_to_new_applicants()
input("Based on their hometown, applicants get assigned to the nearest Codecool school" + "\n")
Applicant.school_to_applicant()
input("Assign registration time to applicants"+"\n")
Applicant.assign_reg_date_to_new_applicants()
input("Assigning interviews to applicants")
Applicant.check_interview_date()

input("Press enter to the main menu")
Menu.main()
# Applicant.check_interview_date()
while True:
    answer = input("Do you want to create a new database? (yes or no): ").lower()
    if answer == "yes":
        input("Creating tables...  ")
        create_table()
        input("Database imaging is in progress... ⌛ ")
        generate_data()
        input("Hunting new applicants and generating application codes for them... ☢")
        Applicant.assign_app_code_to_new_applicants()
        input("Based on their hometown, applicants get assigned to the nearest Codecool school.")
        Applicant.school_to_applicant()
        input("Assigning interviews to applicants.")
        Applicant.check_interview_date()
        input("Press enter to the main menu.")
        print("\n")
        Menu.main()
    elif answer == "no":
        Menu.main()
    else:
        print("There is no such option, please choose yes or no.")
