"""This module is responsible for scheduling workout reminders."""

from twilio.rest import Client
import time
import threading

ACCOUNT_SID = 'your_account_sid'
AUTH_TOKEN = 'your_auth_token'

phone_number = '+12345678901'
reminder_interval = 60  # in seconds
message = 'This is your workout reminder.'
stop_reminders = False


def start_workout_mode():
    global stop_reminders
    stop_reminders = False
    while not stop_reminders:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_='+12345678901',
            to=phone_number
        )
        print(message.sid)
        time.sleep(reminder_interval)