import sendgrid
import os
from sendgrid.helpers.mail import *


def report(subj, cont):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("info@miye.com")
    to_email = Email("mevlanaayas@gmail.com")
    subject = subj
    content = cont
    sg_mail = Mail(from_email, subject, to_email, content)
    sg.client.mail.send.post(request_body=sg_mail.get())


