from email_model import EmailSender


class ProjectEmail:

    @staticmethod
    def send_applicant_info(applicant):
        body = "Dear {0}, \n Your application code: {1} \n The location of the school you've been assigned to: {2}".format(applicant.first_name + ' ' + applicant.last_name, applicant.app_code, applicant.school.location)
        subject = "Your application details"
        to_address = applicant.email
        EmailSender.email_send(to_address, body, subject)
