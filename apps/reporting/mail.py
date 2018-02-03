import sendgrid
import os
from sendgrid.helpers.mail import *

USER_SIDE_ERROR_REPORT_MAIL_LIST = os.environ.get('USER_SIDE_ERROR_REPORT_MAIL_LIST')
PROGRAM_SIDE_ERROR_REPORT_MAIL_LIST = os.environ.get('PROGRAM_SIDE_ERROR_REPORT_MAIL_LIST')


def report(subj, cont, report_code):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("info@miye.com")
    to_email = Email("mevlanaayas@gmail.com")
    subject = subj
    content = cont
    sg_mail = Mail(from_email, subject, to_email, content)
    sg.client.mail.send.post(request_body=sg_mail.get())
