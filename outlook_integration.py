"""This module is responsible for integrating with the Outlook API."""

import requests

# TODO: Replace these with your own values
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'your_redirect_uri'


class OutlookAPI:
    def __init__(self, token=None):
        self.token = token

    def get_token_from_code(self, auth_code):
        token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'

        token_data = {
            'grant_type': 'authorization_code',
            'code': auth_code,
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

        response = requests.post(token_url, data=token_data)
        response.raise_for_status()
        return response.json()

    def get_token_from_refresh_token(self, refresh_token):
        token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'

        token_data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

        response = requests.post(token_url, data=token_data)
        response.raise_for_status()
        return response.json()

    def get_events(self, start_datetime, end_datetime):
        events_url = 'https://graph.microsoft.com/v1.0/me/calendarview'

        query_parameters = {
            'startDateTime': start_datetime,
            'endDateTime': end_datetime
        }

        headers = {
            'Authorization': 'Bearer ' + self.token
        }

        response = requests.get(events_url, params=query_parameters, headers=headers)
        response.raise_for_status()
        return response.json()

    def create_event(self, start_datetime, end_datetime, subject, attendees=None):
        events_url = 'https://graph.microsoft.com/v1.0/me/events'

        event_data = {
            'subject': subject,
            'start': {
                'dateTime': start_datetime,
                'timeZone': 'UTC'
            },
            'end': {
                'dateTime': end_datetime,
                'timeZone': 'UTC'
            },
            'attendees': attendees or []
        }

        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json'
        }

        response = requests.post(events_url, json=event_data, headers=headers)
        response.raise_for_status()
        return response.json()