import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# Test File for G-CalendarAPI

# This function authenticates a user with the Google Calendar API and returns a service object.
# The service object serves as a connection to the Google Calendar API and is necessary for any
# interactions with the API. Once the service object is obtained, it can be passed to other functions
# to perform tasks such as creating, updating, fetching events etc.
# Therefore, successful creation of the service object confirms successful authentication and
# a valid connection to the Google Calendar API.


def authenticate():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # Replaced duplicate code with a function call
creds = create_credentials()
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    return service


# Call the Calendar API
def get_upcoming_events(service: object, num_events: int = 10):
    """
    Fetches the upcoming events on the user's calendar.
    :param service: The authenticated Google Calendar service object
    :param num_events: The number of upcoming events to fetch. If not provided, defaults to 10.
    :return: None

    For example, get_upcoming_events(service, 5) would fetch the next 5 upcoming events.
    If no number is provided, the function defaults to fetching the next 10 upcoming events.
    """

    # Call the Calendar API
    import datetime
    service = authenticate()
    try:
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print(f'Getting the upcoming {num_events} events')
        events_result = service.events().list(
            calendarId='primary',
            timeMin=now,
            maxResults=num_events,
            singleEvents=True,
            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        else:
            # Prints the start and name of the upcoming events
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)


def add_event(
        service: object,
        start: str,
        end: str,
        summary: str,
        description: str,
        location: str) -> str:
    """
    Creates an event.
    :param service: The authenticated Google Calendar service object
    :param start: The start time of the event in RFC3339 timestamp format
    :param end: The end time of the event in RFC3339 timestamp format
    :param summary: The summary or title of the event
    :param description: The description of the event
    :param location: The location of the event
    :return: The event's html link if the event is created successfully
    """
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end,
            'timeZone': 'America/Los_Angeles',
        },
    }
    try:
        created_event = service.events().insert(
            calendarId='primary', body=event).execute()
        print(f"Event created: {created_event['htmlLink']}")
        return created_event['htmlLink']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def delete_event(service: object, event_id: str) -> bool:
    """
    Deletes an event.
    :param service: The authenticated Google Calendar service object
    :param event_id: The ID of the event to delete
    :return: True if the event is deleted successfully, False otherwise
    """
    try:
        service.events().delete(calendarId='primary', eventId=event_id).execute()
        print(f"Event {event_id} deleted.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def update_event(service: object, event_id: str, updated_event: dict) -> str:
    """
    Updates an event.
    :param service: The authenticated Google Calendar service object
    :param event_id: The ID of the event to update
    :param updated_event: A dictionary containing the updated event details
    :return: The event's html link if the event is updated successfully
    """
    try:
        updated_event = service.events().update(
            calendarId='primary',
            eventId=event_id,
            body=updated_event).execute()
        print(f"Event updated: {updated_event['htmlLink']}")
        return updated_event['htmlLink']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def check_availability(service: object, start: str, end: str) -> list:
    """
    Checks the availability of the calendar.
    :param service: The authenticated Google Calendar service object
    :param start: The start time of the period to check in RFC3339 timestamp format
    :param end: The end time of the period to check in RFC3339 timestamp format
    :return: A list of busy periods within the specified time period
    """
    body = {
        "timeMin": start,
        "timeMax": end,
        "items": [{"id": 'primary'}]
    }
    try:
        events_result = service.freebusy().query(body=body).execute()
        busy_periods = events_result[u'calendars'][u'primary'][u'busy']
        return busy_periods
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_event(service: object, event_id: str) -> dict:
    """
    Retrieves an event.
    :param service: The authenticated Google Calendar service object
    :param event_id: The ID of the event to retrieve
    :return: A dictionary containing the event details if the event is retrieved successfully
    """
    try:
        event = service.events().get(calendarId='primary', eventId=event_id).execute()
        return event
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_settings(service: object) -> dict:
    """
    Retrieves the user's calendar settings.
    :param service: The authenticated Google Calendar service object
    :return: A dictionary containing the user's calendar settings if the settings are retrieved successfully
    """
    try:
        settings = service.settings().list().execute()
        return settings
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    """Show basic usage of the Google Calendar API
    main() really for testing, but can show how these functions would
    be called / what data is expected to be passed to them
    """
    service = authenticate()

    # Get upcoming events
    get_upcoming_events(service, 5)

    # Create an event
    start_time = "2023-08-10T09:00:00-07:00"  # replace with real date and time
    end_time = "2023-08-10T10:00:00-07:00"  # replace with real date and time
    add_event(
        service,
        start_time,
        end_time,
        'Test Event',
        'Test Description',
        'Test Location')

    # Delete an event
    event_id = "abcdefgh"  # replace with real event ID
    delete_event(service, event_id)

    # Update an event
    event_id = "abcdefgh"  # replace with real event +ID
    updated_event_data = {}  # replace with real data
    update_event(service, event_id, updated_event_data)

    # Check availability
    start_time = "2023-08-10T09:00:00-07:00"  # replace with real date and time
    end_time = "2023-08-10T10:00:00-07:00"  # replace with real date and time
    check_availability(service, start_time, end_time)

    # Get an event
    event_id = "abcdefgh"  # replace with real event ID
    get_event(service, event_id)

    # Get settings
    get_settings(service)


if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()