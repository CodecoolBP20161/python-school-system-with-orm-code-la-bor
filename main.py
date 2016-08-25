from models import *
from menu import *
from build import *
from example_data import *


while True:
    answer = input("Do you want to create a new database? (yes or no): ").lower()
    if answer == "yes":
        input("Creating tables...  ")
        create_table()
        input("Database imaging is in progress... ⌛ ")
        generate_data()
        input("Hunting new applicants and generating application codes for them... ☢.\
              Based on their hometown, applicants get assigned to the nearest Codecool school.")
        Applicant.handle_new_applicants()
        input("Assigning interviews to applicants.")
        Applicant.check_interview_date()
        Interview.send_email()
        Applicant.assign_reg_date_to_new_applicants()
        input("Press enter to the main menu.")
        print("\n")
        Menu.main()
    elif answer == "no":
        Menu.main()
    else:
        print("There is no such option, please choose yes or no.")
