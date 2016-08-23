from tabulate import tabulate


class PrintTable:

    @staticmethod
    def print_all(query):
        if query:
            all_applicants = [applicant for applicant in query]
            table = []
            for applicant in all_applicants:
                table.extend([[applicant.app_code, applicant.first_name, applicant.last_name, applicant.hometown,
                applicant.school.name, applicant.status, applicant.email]])
            headers = ["App_code", "First name", "Last name", "Hometown", "School", "Status", "E-mail"]
            print(tabulate(table, headers, tablefmt="fancy_grid"))
        else:
            print("This filter option does not exist!")

# PrintTable.print_all()
