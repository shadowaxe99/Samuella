import time
from flask import Flask, request
from twilio.rest import Client
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64
import datetime

# Your Gmail API credentials
GMAIL_API_CREDENTIALS = 'path_to_your_assistant_gmail_api_credentials.json'

# Your Twilio credentials
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'

# Create a Gmail API service
SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/calendar']
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(GMAIL_API_CREDENTIALS, SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
service = build('gmail', 'v1', credentials=creds)

# Create a Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    resp = MessagingResponse()

    # Extract the message body from the request
    incoming_msg = request.values.get('Body', '').lower()

    # If the incoming message is 'sick', cancel all events for the day and notify
    if 'sick' in incoming_msg:
        # Get today's date
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

        # Get the events for today
        events_result = service.events().list(calendarId='primary', timeMin=now, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])

        # Cancel all events for today
        for event in events:
            service.events().delete(calendarId='primary', eventId=event['id']).execute()

        # Send an email to notify about the cancellation
        message = MIMEText('I am not feeling well today and will not be able to attend the scheduled events. I will reschedule them as soon as possible.')
        message['to'] = 'recipient@example.com'
        message['from'] = 'your-assistant-email@example.com'
        message['subject'] = 'Cancellation of today's events'
        raw_message = base64.urlsafe_b64encode(message.as_bytes())
        raw_message = raw_message.decode()
        message = service.users().messages().send(userId='me', body={'raw': raw_message}).execute()

        resp.message("All events for today have been cancelled.")
    else:
        resp.message("I didn't understand your message.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)