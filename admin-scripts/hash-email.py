#!/usr/bin/env python2

from sys import argv
import smtplib as mail
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

'''
I try to never put in my passwords/other osint stuff in my code
so you will have to replace the account info with your personal account
so where it is labeled
# account username
and/or
# account password
replace either all of the information with your personal file and/or
replace it with your actual credentials where appropriate
'''

# used to grab account information
from os.path import join, expanduser
from csv import reader
from argparse import ArgumentParser

# account username
parser = ArgumentParser(description='$(description)')
parser.add_argument("-u", "--username",help="$(help-text)", action="store_true")
if args.token:
    apiKey = args.token
else:
    with open(join(expanduser('~'), 'src/49th/all.pass')) as csvfile:
        readz = reader(csvfile, delimiter=':')
        for row in readz:
            if row[0] == '$(account)':
                emailAddr = row[2]


# account password
parser = ArgumentParser(description='$(description)')
parser.add_argument("-p", "--password",help="$(help-text)",action="store_true")
if args.token:
    apiKey = args.token
else:
    with open(join(expanduser('~'), 'src/49th/all.pass')) as csvfile:
        readz = reader(csvfile, delimiter=':')
        for row in readz:
            if row[0] == '$(account)':
                emailPass = row[2]


# all the metadata for sending message such as the following:
# who from (myaddr), password (app_pass), and subject of email (sub)
myaddr = emailAddr
app_pass = emailPass
sub = '49th Security Divsion Password Hash'


# format in csv is [email-addr,password-hash]
# for loop for sending messages and obtaining hash with email addr of who to send to from csv
# how to send out a mass email to all members of clubs with password hashes
with open(argv[1], 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # logging into gmail account or whatever your email uses
        server = mail.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(myaddr, app_pass)


        # defining things needed for message to send properly
        msg = MIMEMultipart()
        msg['From'] = myaddr
        msg['Subject'] = sub
        body = "super nice message saying hello to everyone!!!"
        toaddr = row[0]
        hashes = row[1]
        msg['To'] = toaddr


        # adding hashes to the body of the message
        # body += hashes


        # converting to needed text type
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()


        # sending the actual message
        server.sendmail(msg.get('From'), msg['To'], text)


        # properly closing the channel between google
        server.quit()
