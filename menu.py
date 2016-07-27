class Menu:

    @staticmethod
    def choose_main_menu():
        option = input("Please enter the key of the option, that you want to choose: ")
        if option == "1":
            print("Admin")
            Menu.admin_menu()
            Menu.choose_admin_menu()
        elif option == "2":
            print("Applicant")
            Menu.applicant_menu()
            Menu.choose_applicant_menu()
        elif option == "3":
            print("Mentor")
            Menu.mentor_menu()
            Menu.choose_mentor_menu()
        elif option == "q":
            exit()
        else:
            raise KeyError("There is no such option.")

    @staticmethod
    def main_menu():
        print("\tMain menu:\n", "\t\t1: Admin\n", "\t\t2: Applicant\n", "\t\t3: Mentor\n", "\t\tPress Q to EXIT")

    @staticmethod
    def main():
        while True:
            Menu.main_menu()
            try:
                Menu.choose_main_menu()
            except KeyError as err:
                print("Please choose from these options:")

    @staticmethod
    def applicant_menu():
        print("\tApplicant menu:\n", "\t\t1: Application details\n", "\t\t2: Interview details\n", "\t\t3: Questions\n"
              "\t\tq: Back to main menu:\n")


    @staticmethod
    def choose_applicant_menu():
        option = input("Please enter the key of the option, that you want to choose: ")
        if option == "1":
            print("application details")
            print('\n')
        elif option == "2":
            print("interview details")
            print('\n')
        elif option == "3":
            print("question?")
            print('\n')
        elif option == "q":
            exit()
        else:
            raise KeyError("There is no such option.")

    @staticmethod
    def admin_menu():
        print("\tAdmin menu:\n", "\t\t1: Applicants\n", "\t\t2: Interviews \n", "\t\t3: Questions \n",
              "\t\tq: Back to main menu:\n")

    @staticmethod
    def choose_admin_menu():
        option = input("Please enter the key of the option, that you want to choose: ")
        if option == "1":
            print("application details")
            print('\n')
        elif option == "2":
            print("interview details")
            print('\n')
        elif option == "3":
            print("question?")
            print('\n')
        elif option == "q":
            exit()
        else:
            raise KeyError("There is no such option.")

    @staticmethod
    def mentor_menu():
        print("\tMentor menu:\n", "\t\t1: Interview\n", "\t\t2: Questions \n", "\t\tq: Back to main menu:\n")

    @staticmethod
    def choose_mentor_menu():
        option = input("Please enter the key of the option, that you want to choose: ")
        if option == "1":
            print("interview")
        elif option == "2":
            print("question?")
        elif option == "q":
            exit()
        else:
            raise KeyError("There is no such option.")


if __name__ == '__main__':
    Menu.main()