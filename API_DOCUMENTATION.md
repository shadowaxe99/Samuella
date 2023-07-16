# API Documentation

This application interacts with both the Google Calendar API and Twilio API. Here are the main API calls that the application makes:

1. **Authenticate**: The application authenticates with the Google Calendar API and Twilio API. For Google Calendar API, it uses OAuth 2.0. This involves redirecting the user to a Google sign-in page, where the user can grant the application access to their Google Calendar data. For Twilio API, it uses the account SID and auth token.

2. **Fetch upcoming events**: The application fetches the upcoming events on the user's calendar using the `events().list` method of the Google Calendar API.

3. **Delete event**: The application deletes an event from the user's calendar using the `events().delete` method of the Google Calendar API.

4. **Send SMS**: The application sends an SMS using the Twilio API. It responds to incoming messages with a simple text message. If the incoming message is 'sick', it cancels all events for the day and notifies the user.

5. **Send Email**: The application sends an email using the Gmail API. If the user is sick, it sends an email to notify about the cancellation of today's events.

For more detailed information on the Google Calendar API, refer to the [official documentation](https://developers.google.com/calendar). For more information on the Twilio API, refer to the [official documentation](https://www.twilio.com/docs/quickstart).