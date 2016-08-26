from email_model import EmailSender


class ProjectEmail:

    @staticmethod
    def send_applicant_info(applicant):
        body = "Dear {0}, \n Your application code: {1} \n The location of the school you've been assigned to: {2}".format(applicant.first_name + ' ' + applicant.last_name, applicant.app_code, applicant.school.location)
        subject = "Your application details"
        to_address = applicant.email
        EmailSender.email_send(to_address, body, subject)

    @staticmethod
    def send_interview_details(applicant):
        body = "Dear {0}, \n Your interview details: \n Your interview will start: {1} \n Your interview will end: {2} \n Your mentor will be: {3} \n The location of the school: {4}".format(
            applicant.first_name + ' ' + applicant.last_name,
            applicant.interview.start_date,
            applicant.interview.end_date,
            applicant.interview.mentor.first_name + ' ' + applicant.interview.mentor.last_name,
            applicant.school.location
            )
        subject = "Your interview details"
        to_address = applicant.email
        EmailSender.email_send(to_address, body, subject)

    @staticmethod
    def send_details_to_mentor(applicant):
        body = "Dear {0}, \n Your screening details: \n Applicant name: {1} \n Start date: {2} \n End date: {3} \n".format(
            applicant.interview.mentor.first_name + ' ' + applicant.interview.mentor.last_name,
            applicant.first_name + ' ' + applicant.last_name,
            applicant.interview.start_date,
            applicant.interview.end_date,
        )
        subject = "Your screening details"
        to_address = applicant.interview.mentor.email
        EmailSender.email_send(to_address, body, subject)