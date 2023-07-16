# Troubleshooting Guide

Here are some common issues you might encounter when setting up the development environment or running the application, and how to resolve them:

1. **Python not installed**: The application is written in Python. If you don't have Python installed, you can download it from [the official website](https://www.python.org/downloads/).

2. **Dependencies not installed**: The project dependencies are listed in the `requirements.txt` file. If you encounter an error about a missing module, make sure you have installed the dependencies using pip, the Python package installer. Run the command `pip install -r requirements.txt` in the root directory of the project.

3. **Google Calendar API setup**: The application interacts with the Google Calendar API. If you encounter an error about missing credentials, make sure you have set up a project in the [Google Cloud Console](https://console.cloud.google.com/), enabled the Google Calendar API, and obtained credentials (a client ID and client secret) that the application can use. You can find more information on how to do this in the [Google Calendar API Python Quickstart guide](https://developers.google.com/calendar/quickstart/python).

4. **Environment variables not configured**: The application uses environment variables for configuration. If you encounter an error about missing environment variables, make sure you have set these variables in your development environment. The required variables are `GOOGLE_CALENDAR_CLIENT_ID` and `GOOGLE_CALENDAR_CLIENT_SECRET`.

If you encounter any other issues, feel free to ask for help!

## Updates

### data_storage.py
- No changes were made in this file.