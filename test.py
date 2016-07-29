from models import *

print(Applicant.detect_new_applicants())
print(Applicant.assign_app_code_to_new_applicants())
Applicant.school_to_applicant()
Applicant.interview_date_to_applicant()
