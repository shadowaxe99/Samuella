"""This is the main entry point for the application."""

from daily_inspiration import send_daily_inspiration
from sick_mode import start_sick_mode
from family_mode import handle_family_message
from leave_message import leave_message, get_message
from schedule_reminder import schedule_reminder
from workout_reminder import start_workout_mode
from calendar_integration import add_event, get_events
from ai_agent import start_ai_agent


def main():
    send_daily_inspiration()
    start_sick_mode()
    handle_family_message('Hello')
    leave_message()
    get_message()
    schedule_reminder()
    start_workout_mode()
    add_event()
    get_events()
    start_ai_agent()

if __name__ == '__main__':
    main()