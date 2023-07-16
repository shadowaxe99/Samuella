"""This module is responsible for integrating with the Twilio API."""

from twilio.rest import Client

ACCOUNT_SID = 'your_account_sid'
AUTH_TOKEN = 'your_auth_token'


def send_sms(to, body):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=body,
        from_='+12345678901',
        to=to
    )
    print(message.sid)