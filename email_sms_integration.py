"""This module is responsible for sending emails and SMS messages."

import base64
import os
import pickle
from email.mime.text import MIMEText
from twilio.rest import Client
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

GMAIL_API_CREDENTIALS = 'credentials.json'


def send_email(receiver, subject, body):
    """Send an email using the Gmail API."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                GMAIL_API_CREDENTIALS, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    message = MIMEText(body)
    message['to'] = receiver
    message['from'] = 'me'
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_string().encode('utf-8'))
    raw_message = raw_message.decode('utf-8')
    body = {'raw': raw_message}
    message = (service.users().messages().send(userId='me', body=body).execute())
    print(f"Message Id: {message.get('id')}")
    return message

def send_sms(receiver, body):
    """Send an SMS using the Twilio API."""
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_='+12345678901',
        to=receiver
    )

    print(message.sid)
