from tabulate import tabulate


class PrintTable:

    @staticmethod
    def print_applicant(query):
        if query:
            table = []
            for applicant in query:
                table.extend([[applicant.app_code, applicant.first_name, applicant.last_name, applicant.hometown,
                               applicant.school.name, applicant.status, applicant.email, applicant.reg_date]])
            headers = ["App_code", "First name", "Last name", "Hometown", "School", "Status", "E-mail",
                       "Registration time"]
            print(tabulate(table, headers, tablefmt="fancy_grid"))
        else:
            print("This filter option does not exist!")

    @staticmethod
    def print_interview(query):
        if query:
            table = []
            for interview in query:
                table.extend([[interview.school.name, interview.get_applicant().app_code,
                               interview.mentor.first_name + ' ' + interview.mentor.last_name, interview.start_date,
                               interview.end_date]])
            headers = ["School", "App_code", "Mentor name", "Start date", "End date"]
            print(tabulate(table, headers, tablefmt="fancy_grid"))
        else:
            print("This filter option does not exist!")

    @staticmethod
    def print_interview_app_code(query):
        if query:
            table = []
            for i in query:
                table.extend([[i.school.name, i.app_code,
                               i.interview.mentor.first_name + ' ' + i.interview.mentor.last_name, i.interview.start_date,
                               i.interview.end_date]])
            headers = ["School", "App_code", "Mentor name", "Start date", "End date"]
            print(tabulate(table, headers, tablefmt="fancy_grid"))
        else:
            print("This filter option does not exist!")

    @staticmethod
    def print_interview_date(query):
        if query:
            table = []
            for i in query:
                table.extend([[i.applicant.school.name, i.appplicant.app_code,
                               i.mentor.first_name + ' ' + i.mentor.last_name,
                               i.start_date,
                               i.end_date]])
            headers = ["School", "App_code", "Mentor name", "Start date", "End date"]
            print(tabulate(table, headers, tablefmt="fancy_grid"))
        else:
            print("This filter option does not exist!")