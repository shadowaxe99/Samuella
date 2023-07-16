"""This is the main entry point for the application."""

from daily_inspiration import send_daily_inspiration
from sick_mode import start_sick_mode
from family_mode import handle_family_message
from leave_message import leave_message, get_message
from schedule_reminder import schedule_reminder
from workout_reminder import start_workout_mode
from calendar_integration import add_event, get_events
from ai_agent import AIAgent


def main():
    ai_agent = AIAgent()
    try:
        user_message = input('Enter a message for daily inspiration: ')
        ai_agent.add_user_message(user_message)
        print(ai_agent.get_bot_response())
    except Exception as e:
        print('Error in send_daily_inspiration. This function does not take any arguments.')
    try:
        user_message = input('Enter a message for sick mode: ')
        ai_agent.add_user_message(user_message)
        print(ai_agent.get_bot_response())
    except Exception as e:
        print('Error in start_sick_mode. This function does not take any arguments.')
    try:
        user_message = input('Enter a message for family mode: ')
        ai_agent.add_user_message(user_message)
        print(ai_agent.get_bot_response())
    except Exception as e:
        print('Error in handle_family_message. This function takes one argument: a string message.')
    try:
        user_message = input('Enter a message for leave message: ')
        ai_agent.add_user_message(user_message)
        print(ai_agent.get_bot_response())
    except Exception as e:
        print('Error in leave_message. This function does not take any arguments.')
    try:
        user_message = input('Enter a message for get message: ')
        ai_agent.add_user_message(user_message)
        print(ai_agent.get_bot_response())
    except Exception as e:
        print('Error in get_message. This function does not take any arguments.')
    try:
        user_message = input('Enter a message for schedule reminder: ')
        ai_agent.add_user_message(user_message)
        print(ai_agent.get_bot_response())
    except Exception as e:
        print('Error in schedule_reminder. This function does not take any arguments.')
    try:
        user_message = input('Enter a message for workout mode: ')
        ai_agent.add_user_message(user_message)
        print(ai_agent.get_bot_response())
    except Exception as e:
        print('Error in start_workout_mode. This function does not take any arguments.')

if __name__ == '__main__':
    main()