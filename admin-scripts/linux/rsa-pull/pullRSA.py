#!/usr/bin/env python2.7
import os, time, argparse, yaml, codecs
from csv import reader
from datetime import date,timedelta
from httplib2 import Http
from apiclient.discovery import build
from oauth2client import client, tools
from oauth2client.file import Storage



def get_credentials():
    SCOPES = ( 'https://www.googleapis.com/auth/spreadsheets')
    pathToSecret = '/coding/49th/creds/rsa-pull'
    clientSecretFile = 'client_secret.json'
    clientSecret = os.path.join(pathToSecret, clientSecretFile)
    accessFile = 'access.json'
    clientAccess = os.path.join(pathToSecret, accessFile)
    store = Storage(clientAccess)
    credz = store.get()

    if not credz or credz.invalid:
        flow = client.flow_from_clientsecrets(clientSecret, SCOPES)
        credz = tools.run_flow(flow, store)

    return credz



def get_sheets(credz,sheetID,sheetName):
    sheetz = build('sheets', 'v4', http=credz.authorize(Http()))
    #  getAllDemSheetz = sheetz.spreadsheets().get(spreadsheetId=sheetID, includeGridData=True, prettyPrint=True).execute()
    getAllDemSheetz = sheetz.spreadsheets().values().get(spreadsheetId=sheetID, range=sheetName).execute()
    return getAllDemSheetz


def get_keys(sheetz):

    # accessing values from the dictionary that sheetz is in
    valuesFromSheet = sheetz['values']

    # doing a for loop and skipping the first row (headers) with the [1:]
    keyz = valuesFromSheet[1:]

    # returning the key values in list form
    return keyz


def get_users(rsaKeyzFormData, sheetNamez):

    usersz = []

    for user in rsaKeyzFormData:

        # accessing the email for a key value
        email = user[1].split('@')[0].encode('ascii','replace')

        # accessing the username that the user submitted
        username = user[2].encode('ascii','replace')

        # accessing the rsa key that the user submitted
        rsaKey = user[4].encode('ascii','replace')

        if email and username and rsaKey:
            newData = { 'key': email, 'name':username, 'rsaKey': rsaKey }
            newUsersz = set_keys(usersz,newData)
        else:
            print('not working properly')
            exit(2)
    return newUsersz

def set_keys(usersz,newData):
    if any(d['key'] == newData['key'] for d in usersz):
        for user in usersz:
            if user['key'] == newData['key']:
                if isinstance(user['rsaKey'], str):
                    if newData['rsaKey'] != user['rsaKey']:
                        user['rsaKey'] = [user['rsaKey'],newData['rsaKey']]
                else:
                    if newData['rsaKey'] not in user['rsaKey']:
                        user['rsaKey'].append(newData['rsaKey'])
        return usersz
    elif not any(d['key'] == newData['key'] for d in usersz):
        usersz.append(newData)
        return usersz
    else:
        print('Something weird')

def set_users(usersz, sheetNamez):
    # dictionary to yaml
    yamlOut = {'users':usersz}
    with open('users.yml', 'w') as outfile:
        yaml.dump(yamlOut,outfile,default_flow_style=False)
    # accessing the email for a key value
    # accessing the username that the user submitted
    # accessing the rsa key that the user submitted


def errorz(info):
    # send email to 49thSD-Lab_Manager-Group@uncc.edu with info
    print('halo')

def main():

    parser = argparse.ArgumentParser(description='Used to pull down rsa keys')

    parser.add_argument('users', choices=['Lab_Trolls', 'Lab_Minions', 'General_Members', 'Web_Dev'], help='the users you are trying to pull down rsa keys for.(This is relient on the names of the sheets in the Google Sheet "RSA Keys (Responses)")')

    args = parser.parse_args()
    #  print(args.users)

    with open('/coding/49th/creds/all.pass') as csvfile:
        readz = reader(csvfile,delimiter=':')
        for row in readz:
            if row[0] == 'rsa_pull':
                if row[1] == 'sheetid':
                    sheetID = row[2]
                else:
                    exit(2)

    # variables
    sheetId = sheetID
    userSheetName = args.users
    # authorization
    credentials = get_credentials()
    # return keyz
    sheets = get_sheets(credentials, sheetId, userSheetName)
    # getting keys
    rsaKeys = get_keys(sheets)
    if rsaKeys:
        users = get_users(rsaKeys, userSheetName)
        set_users(users, userSheetName)
    else:
        print('Nothing else to do...')
        exit()

main()
