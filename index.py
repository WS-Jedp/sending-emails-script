import pandas as pd
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

ENDPOINT = os.getenv('ENPOINT_URL')
CSV_FILE_PATH = os.getenv('CSV_FILE')
CSV_EMAIL_FIELD = os.getenv('CSV_EMAIL_FIELD')
AVOID_EMAILS = os.getenv('AVOID_EMAILS')
PAYLOAD_EMAILS_FIELD = os.getenv('PAYLOAD_EMAILS_FIELD')
PAYLOAD_OPTIONAL_FIELDS = os.getenv('PAYLOAD_OPTIONAL_FIELDS')
RESPONSE_FILE = os.getenv('RESPONSE_FILE')

def getEmailsFromCSV():
    emailsReader = pd.read_csv(CSV_FILE_PATH)
    emails = emailsReader[CSV_EMAIL_FIELD]
    uniqueEmails = []

    for email in emails:

        if(AVOID_EMAILS):
            ignore_emails = json.loads(AVOID_EMAILS)
            if(email in ignore_emails):
                continue

        if(email not in emails):
            uniqueEmails.append(email)

    
    return uniqueEmails

def sendEmails():
    emails = getEmailsFromCSV()
    headers = {'content-type': 'application/json', 'Accept': 'application/json'}

    payload = {}
    payload[PAYLOAD_EMAILS_FIELD] = emails


    if(PAYLOAD_OPTIONAL_FIELDS):
        optional_fields = json.loads(PAYLOAD_OPTIONAL_FIELDS)
        for field in optional_fields:
            payload[field] = optional_fields[field]


    response = requests.post(ENDPOINT, data=json.dumps(payload), headers=headers)

    return response.json()


if __name__ == "__main__":

    json_response = sendEmails()
    with open(RESPONSE_FILE, 'w+') as response_file:
        json.dump(json_response, response_file)
