from models import *
from print_table import *


class Menu:

    @staticmethod
    def main_menu():
        print("\tMain menu:\n", "\t\t1: Admin\n", "\t\t2: Applicant\n", "\t\t3: Mentor\n", "\t\tPress Q to EXIT", "\n")

    @staticmethod
    def choose_main_menu():
        option = input("Choose an option: ")
        if option == "1":
            Menu.admin_menu()
            Menu.choose_admin_menu()
        elif option == "2":
            Menu.applicant_menu()
            Menu.choose_applicant_menu()
        elif option == "3":
            Menu.mentor_menu()
            Menu.choose_mentor_menu()
        elif option == "q":
            exit()
        else:
            raise KeyError("There is no such option.")

    @staticmethod
    def applicant_menu():
        print("\tApplicant menu:\n", "\t\t1: Application details\n", "\t\t2: Interview details\n", "\t\t3: Questions\n"
              "\t\tPress Q to main menu:\n")

    @staticmethod
    def choose_applicant_menu():
        while True:
            option = input("Choose an option: ")
            if option == "1":
                Applicant.get_status()
            elif option == "2":
                Applicant.get_interview_details()
            elif option == "3":
                print("question?")
                print('\n')
            elif option == "q":
                break
            else:
                raise KeyError("There is no such option.")
            Menu.applicant_menu()

    @staticmethod
    def admin_menu():
        print("\tAdmin menu:\n", "\t\t1: Applicants\n", "\t\t2: Interviews \n", "\t\t3: Questions \n",
              "\t\tPress Q to main menu:\n")

    @staticmethod
    def choose_admin_menu():
        while True:
            option = input("Choose an option: ")
            if option == "1":
                Menu.applicants_admin_menu()
                Menu.choose_applicants_admin_menu()
            elif option == "2":
                print("Interview details")
                print('\n')
            elif option == "3":
                print("question?")
                print('\n')
            elif option == "q":
                break
            else:
                raise KeyError("There is no such option.")
            Menu.admin_menu()

    @staticmethod
    def choose_applicants_admin_menu():
        while True:
            option = input("Choose a filter: ")
            if option == "1":
                Applicant.get_filter_status()
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
                raise KeyError("There is no such option.")
            Menu.choose_applicants_admin_menu()

    @staticmethod
    def applicants_admin_menu():
        print("\tApplicants (Admin menu):\n", "\t\t1: status\n", "\t\t2: time \n", "\t\t3: hometown \n",
              "\t\t4: personal data \n", "\t\t5: school \n", "\t\t6: mentor name \n"  "\t\tPress Q to admin menu:\n")

    @staticmethod
    def mentor_menu():
        print("\tMentor menu:\n", "\t\t1: Interview\n", "\t\t2: Questions \n", "\t\tq: Back to main menu:\n")

    @staticmethod
    def choose_mentor_menu():
        while True:
            option = input("Choose an option: ")
            if option == "1":
                print("interview")
                print('\n')
            elif option == "2":
                print("question?")
                print('\n')
            elif option == "q":
                break
            else:
                raise KeyError("There is no such option.")
            Menu.mentor_menu()

    @staticmethod
    def main():
        while True:
            Menu.main_menu()
            try:
                Menu.choose_main_menu()
            except KeyError as err:
                print("Please choose from these options:")

if __name__ == '__main__':
    Menu.main()
