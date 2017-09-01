#!/usr/bin/env python2

from sys import argv
import smtplib as mail
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
# used to grab account information
from os.path import join, expanduser
from csv import reader
from argparse import ArgumentParser

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

# account username
parser = ArgumentParser(description='This script is used to send out password hashes, with a gmail account, for people that have been added to ad')
parser.add_argument("-u", "--username", help="your email you want to send it with", action="store_true")
parser.add_argument("-p", "--password", help="your password for you email", action="store_true")
parser.add_argument('filez', help='argument for the file you need to provide in the following format: emailAddress,passwordHash')
args = parser.parse_args()
if args.username:
    apiKey = args.username
else:
    with open(join(expanduser('~'), 'src/49th/all.pass')) as csvfile:
        readz = reader(csvfile, delimiter=':')
        for row in readz:
            if row[0] == 'gmail-email':
                emailAddr = row[2]


# account password
if args.password:
    apiKey = args.password
else:
    with open(join(expanduser('~'), 'src/49th/all.pass')) as csvfile:
        readz = reader(csvfile, delimiter=':')
        for row in readz:
            if row[0] == 'gmail-pass':
                emailPass = row[2]


# all the metadata for sending message such as the following:
# who from (myaddr), password (app_pass), and subject of email (sub)
myaddr = emailAddr
app_pass = emailPass
sub = '49th Security Divsion Password Hash'


# format in csv is [email-addr,password-hash]
# for loop for sending messages and obtaining hash with email addr of who to send to from csv
# how to send out a mass email to all members of clubs with password hashes
with open(args.filez, 'rb') as csvfile:
    reader = reader(csvfile)
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
