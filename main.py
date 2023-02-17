import os
import smtplib
import time
from email.mime.text import MIMEText


#pinging function
def ping_ips():
    with open('ip.txt') as file:
        dump = file.read()
        dump = dump.splitlines()

    os.system('cls')

    for ip in dump:
        print('Ping Sending', ip)
        print('-' * 60)
        result = os.system('ping -n 2 {}'.format(ip))
        print(result)
        print('-' * 60)
        if result != 0:
            send_email(ip)
#mail sending function
def send_email(ip):
    sender_email = 'sender_mail'
    sender_password = 'sender_password'
    recipient_email = 'recipient_email'
    smtp_server = 'smtp_server'

    message = MIMEText(f'Ping Error: {ip}')
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'Ping Error'

    with smtplib.SMTP(smtp_server, 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

while True:
    ping_ips()
    print("Will try again in 5 minutes...")
    time.sleep(10)  # 5 minut = 5 x 60 second
