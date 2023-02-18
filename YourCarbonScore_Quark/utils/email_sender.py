import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

def send_mail(receiver_email, subject, content):
    load_dotenv()
    admin_mail = os.getenv('ADMIN_EMAIL')

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = admin_mail
    msg['To'] = receiver_email


    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(content, 'plain')
    part2 = MIMEText(content, 'html')
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()
    
    # Authentication
    s.login(admin_mail, os.getenv('PASSWORD'))

    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(admin_mail, receiver_email, msg.as_string())
    s.quit()