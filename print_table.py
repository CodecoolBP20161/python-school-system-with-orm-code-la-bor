from models import *
from tabulate import tabulate


class PrintTable:

    @staticmethod
    def print_all():
        all_applicants = [applicant for applicant in Applicant.select()]
        table = []
        for applicant in all_applicants:
           table.extend([[applicant.app_code, applicant.first_name, applicant.last_name, applicant.hometown,
           applicant.school.name, applicant.status, applicant.email]])
        headers = ["1", "2", "energy", "2", "3", "4", "6", "4"]
        print(tabulate(table, headers, tablefmt="fancy_grid"))


# PrintTable.print_all()

