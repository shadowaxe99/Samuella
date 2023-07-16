# Setup Instructions

This project is a Python application that interacts with the Google Calendar API. Here are the steps to set up the development environment:

1. **Install Python**: The application is written in Python. If you don't have Python installed, you can download it from [the official website](https://www.python.org/downloads/).

2. **Clone the repository**: You can clone the repository using the command `git clone <repository-url>`.

3. **Install dependencies**: The project dependencies are listed in the `requirements.txt` file. You can install these dependencies using pip, the Python package installer. Run the command `pip install -r requirements.txt` in the root directory of the project.

4. **Set up Google Calendar API**: The application interacts with the Google Calendar API. You'll need to set up a project in the [Google Cloud Console](https://console.cloud.google.com/), enable the Google Calendar API, and obtain credentials (a client ID and client secret) that the application can use. You can find more information on how to do this in the [Google Calendar API Python Quickstart guide](https://developers.google.com/calendar/quickstart/python).

   After obtaining the credentials, fill them in the `credentials.json` file in the following format:

   ```json
   {
     "web": {
       "client_id": "YOUR_CLIENT_ID",
       "project_id": "YOUR_PROJECT_ID",
       "auth_uri": "https://accounts.google.com/o/oauth2/auth",
       "token_uri": "https://oauth2.googleapis.com/token",
       "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
       "client_secret": "YOUR_CLIENT_SECRET",
       "redirect_uris": [
         "YOUR_REDIRECT_URI"
       ]
     }
   }
   ```

5. **Configure environment variables**: The application uses environment variables for configuration. You'll need to set these variables in your development environment. The required variables are:

    - `GOOGLE_CALENDAR_CLIENT_ID`: The client ID for the Google Calendar API.

    - `GOOGLE_CALENDAR_CLIENT_SECRET`: The client secret for the Google Calendar API.

Once you've completed these steps, you should be able to run the application in your development environment.

## Updates

### calendar_integration.py
- Commented out the line where 'create_credentials()' is called because the function is not defined.
- Added 'encoding="utf-8"' to the 'open' function call.
- Commented out the lines where 'events' member is used because it's not found in the 'Resource' instance.
- Replaced triple quotes with single quotes in the docstrings.