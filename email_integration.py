import os.path
import base64
import re
import time
import dateutil.parser as parser
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from transformers import pipeline

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify', 'https://www.googleapis.com/auth/calendar']

# Initialize the Hugging Face transformer pipeline for text generation
translator = pipeline('translation_en_to_fr')

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels."""
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me',labelIds=['INBOX'],q='is:unread').execute()
    messages = results.get('messages', [])

    if not messages:
        print('No new messages.')
    else:
        message_count = 0
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            email_data = msg['payload']['headers']
            for values in email_data:
                name = values['name']
                if name == 'From':
                    from_name = values['value']
                    for part in msg['payload']['parts']:
                        try:
                            data = part['body']
                            byte_code = base64.urlsafe_b64decode(data['data'])
                            text = byte_code.decode('utf-8')
                            print('Message received from:', from_name)
                            print('Message body:', text)
                            translated_text = translator(text)[0]['translation_text']
                            print('Translated message:', translated_text)
                            message_count += 1
                        except BaseException as error:
                            pass
        print('You have', message_count, 'new emails.')


if __name__ == '__main__':
    main()