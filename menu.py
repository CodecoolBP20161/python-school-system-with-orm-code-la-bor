from models import *
from print_table import *


class Menu:

    @classmethod
    def choose_main_menu(cls):
        while True:
            print("\tMain menu:\n", "\t\t1: Admin\n", "\t\t2: Applicant\n", "\t\t3: Mentor\n", "\t\tPress Q to EXIT", "\n")

            option = input("Choose an option: ").upper()
            if option == "1":
                cls.choose_admin_menu()
            elif option == "2":
                cls.choose_applicant_menu()
            elif option == "3":
                cls.choose_mentor_menu()
            elif option == "Q":
                exit()
            else:
                print("There is no such option.")

    @staticmethod
    def choose_applicant_menu():
        while True:
            print("\tApplicant menu:\n", "\t\t1: Application details\n", "\t\t2: Interview details\n",
                  "\t\t3: Questions\n", "\t\tPress Q to main menu:\n")

            option = input("Choose an option: ").upper()
            if option == "1":
                Applicant.get_status()
            elif option == "2":
                Applicant.get_interview_details()
            elif option == "3":
                print("question?")
                print('\n')
            elif option == "Q":
                break
            else:
                print("There is no such option.")

    @classmethod
    def choose_admin_menu(cls):

        while True:
            print("\tAdmin menu:\n", "\t\t1: Applicants\n", "\t\t2: Interviews \n", "\t\t3: Questions \n",
                  "\t\tPress Q to main menu:\n")

            option = input("Choose an option: ").upper()
            if option == "1":
                cls.choose_applicants_admin_menu()
            elif option == "2":
                print("Interview details")
                print('\n')
            elif option == "3":
                print("question?")
                print('\n')
            elif option == "Q":
                break
            else:
                print("There is no such option.")

    @staticmethod
    def choose_applicants_admin_menu():

        while True:
            print("\tApplicants (Admin menu):\n", "\t\t1: status\n", "\t\t2: time \n", "\t\t3: hometown \n",
                  "\t\t4: personal data \n", "\t\t5: school \n", "\t\t6: mentor name \n", "\t\tPress Q to admin menu:\n")

            option = input("Choose a filter: ")
            if option == "1":
                PrintTable.print_all(Applicant.get_filter_status())
            elif option == "2":
                # function for peewee query
                print("function for peewee query")
            elif option == "3":
                PrintTable.print_all(Applicant.get_filter_hometown())
            elif option == "4":
                PrintTable.print_all(Applicant.get_filter_email())
            elif option == "5":
                PrintTable.print_all(Applicant.get_filter_school())
            elif option == "6":
                # function for peewee query
                print("function for peewee query")
            elif option == "q":
                break
            else:
                print("There is no such option.")

    @staticmethod
    def choose_mentor_menu():
        while True:
            print("\tMentor menu:\n", "\t\t1: Interview\n", "\t\t2: Questions \n", "\t\tQ: Back to main menu:\n")

            option = input("Choose an option: ").upper()
            if option == "1":
                print("interview")
                print('\n')
            elif option == "2":
                print("question?")
                print('\n')
            elif option == "Q":
                break
            else:
                print("There is no such option.")


    @classmethod
    def main(cls):
        cls.choose_main_menu()

if __name__ == '__main__':
    Menu.main()
