"""This module is responsible for scheduling reminders."""

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime
import time
import threading

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

GMAIL_API_CREDENTIALS = 'credentials.json'

phone_number = '+12345678901'
reminder_interval = 60  # in seconds
message = 'This is your reminder.'
stop_reminders = False


def schedule_reminder():
    global stop_reminders
    stop_reminders = False
    while not stop_reminders:
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        events_result = service.events().list(
            calendarId='primary',
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
            if datetime.datetime.now().isoformat() >= start:
                send_sms(phone_number, message)
        time.sleep(reminder_interval)