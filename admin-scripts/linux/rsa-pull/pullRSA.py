#!/usr/bin/env python2.7
import os, time
from httplib2 import Http
from apiclient.discovery import build
from oauth2client import client, tools
from oauth2client.file import Storage




def get_credentials():

    SCOPES = (
        'https://www.googleapis.com/auth/spreadsheets'
    )
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



def get_sheets(credz,sheetID):
    sheetz = build('sheets', 'v4', http=credz.authorize(Http()))
    getAllDemSheetz = sheetz.spreadsheets().get(spreadsheetId=sheetID, includeGridData=False, prettyPrint=True).execute()
    return getAllDemSheetz


def main():

    with open('/coding/mine/all.pass') as csvfile:
        readz = reader(csvfile,delimiter=':')
        for row in readz:
            if row[0] == 'rsa_pull':
                if row[1] == 'sheetid':
                    sheetID = row[2]
                else:
                    exit(2)

    # variables
    sheetId = sheetID


    # authorization
    credentials = get_credentials()

    # return keyz
    sheets = get_sheets(credentials, sheetId)

    #  print(sheets['spreadsheetId'])
    for i in sheets['sheets']['properties']:
        print(i)
        #  print(str(i) + ' + ' + str(type(i)))
    # getting specific keyz and users
    #  keys = get_keys()

main()
