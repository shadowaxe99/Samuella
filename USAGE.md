# Usage Instructions

This Python application is designed to be run from the command line. Here's how to use it:

1. **Navigate to the project directory**: Use the command `cd <path-to-project-directory>` to navigate to the root directory of the project.

2. **Run the application**: Use the command `python main.py` to run the application. The application will prompt you to enter details for a recurring event, which will then be created on your Google Calendar.

3. **Enter event details**: When prompted, enter the details for the event. You'll need to provide the following details:

    - Start time of the event in RFC3339 timestamp format

    - End time of the event in RFC3339 timestamp format

    - Summary or title of the event

    - Description of the event

    - Location of the event

    - Recurrence rule in RFC2445 iCalendar format

After you've entered the event details, the application will create the event on your Google Calendar and provide a link to the event.

## Updates

### ai_agent.py
- No changes were made in this file.