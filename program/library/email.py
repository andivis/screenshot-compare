import sys
import os
import logging
import smtplib

from email.mime.text import MIMEText

from . import helpers

from .helpers import get

class Email:
    def sendEmail(self, emailAddress, subject, message):
        result = False

        logging.info(f'Sending email to {emailAddress}. Subject: {subject}. Message: {message}.')

        if not emailAddress or not message:
            logging.info(f'Not sending email. Email address or message is blank.')
            return

        gmail_user = self.options['smtpUsername']
        gmail_password = self.options['smtpPassword']

        try:
            smtpserver = smtplib.SMTP(self.options['smtpHost'], self.options['smtpPort'])
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()

            # some servers may not require authentication
            if gmail_user and gmail_password:
                smtpserver.login(gmail_user, gmail_password)

            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = gmail_user
            msg['To'] = emailAddress

            if ',' in emailAddress:
                emailAddress = emailAddress.split(',')
                msg['To'] = ", ".join(emailAddress)

            smtpserver.sendmail(gmail_user, emailAddress, msg.as_string())
            smtpserver.quit()

            result = True

            logging.info('Sent email successfully')
        except Exception as e:
            helpers.handleException(e, 'Something went wrong while sending the email')

        return result

    def __init__(self, options):
        self.options = options