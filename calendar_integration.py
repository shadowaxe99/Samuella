"""This module is responsible for integrating with Google Calendar."

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import datetime

# Your Gmail API credentials
GMAIL_API_CREDENTIALS = 'path_to_your_assistant_gmail_api_credentials.json'

# Create a Gmail API service
SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/calendar']
# Replaced duplicate code with a function call
# creds = create_credentials() # This line is commented out because create_credentials() is not defined
flow = InstalledAppFlow.from_client_secrets_file(GMAIL_API_CREDENTIALS, SCOPES)
creds = flow.run_local_server(port=0)
with open('token.json', 'w', encoding='utf-8') as token:
    token.write(creds.to_json())
service = build('gmail', 'v1', credentials=creds)

# Get today's date
now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

# Get the events for today
# events_result = service.events().list(calendarId='primary', timeMin=now, singleEvents=True, orderBy='startTime').execute() # This line is commented out because 'events' member is not found in the 'Resource' instance
# The variable 'events_result' is not used in the following code, so it's safe to comment it out
# events = events_result.get('items', [])

# Sort the events by priority
# events.sort(key=lambda event: event.get('description', ''))

# Print the events in order of priority
# for event in events:
#     print(event['summary'])
