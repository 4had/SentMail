import smtplib
from smtplib import SMTPAuthenticationError, SMTPRecipientsRefused
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def try_again():
    question = input('Try again(y/n): ').lower()
    if question[0] == 'y':
        return True
    else:
        return False


def sent_mail():

    while True:

        """Questions for user"""

        email = input('Your Email: ')
        password = input('Password: ')

        """Questions for user"""

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        try:
            server.login(email, password)

            print('+' + '-' * 11 + '+')
            print('| logged in |')
            print('+' + '-' * 11 + '+')

            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = input("Recipient: ")
            if not SMTPRecipientsRefused:
                msg['Subject'] = input('Subject: ')
                text = input('Text: ')
                msg.attach(MIMEText(text, 'html'))

                server.sendmail(msg['From'], msg['To'], msg.as_string())

                print('+' + '-' * 21 + '+')
                print('| Email has been send |')
                print('+' + '-' * 21 + '+')
                server.quit()
                break
            else:
                print('+' + '-' * 19 + '+')
                print('| Invalid recipient |')
                print('+' + '-' * 19 + '+')
                if not try_again():
                    break

        except smtplib.SMTPAuthenticationError:
            print('+' + '-' * 27 + '+')
            print('| Invalid Email or Password |')
            print('+' + '-' * 27 + '+' + '\n')

            if not try_again():
                break


