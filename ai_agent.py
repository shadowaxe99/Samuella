import openai
import json


class AIAgent:
    def __init__(self):
        self.messages = [{"role": "system",
                          "content": "You are a helpful assistant."}]

    def add_user_message(self, content):
        self.messages.append({"role": "user", "content": content})

    def get_bot_response(self):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            functions=[
                {
                    "name": "schedule_calendar_time",
                    "description": "Schedule a time on the calendar",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "time": {
                                "type": "string",
                                "description": "The time to schedule on the calendar"
                            }
                        },
                        "required": ["time"]
                    }
                },
                {
                    "name": "send_email",
                    "description": "Send an email",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "to": {
                                "type": "string",
                                "description": "The email address to send to"
                            },
                            "body": {
                                "type": "string",
                                "description": "The body of the email"
                            }
                        },
                        "required": ["to", "body"]
                    }
                }
            ]
        )
        response_message = response['choices'][0]['message']
        self.messages.append(response_message)

        # Check if the model called a function
        if 'function_call' in response_message:
            function_call = response_message['function_call']

            # Get the arguments for the function
            arguments = json.loads(function_call['arguments'])

            # Call the function with the arguments
            if function_call['name'] == 'schedule_calendar_time':
                self.schedule_calendar_time(arguments['time'])
            elif function_call['name'] == 'send_email':
                self.send_email(arguments['to'], arguments['body'])

        return response_message['content']

    def clear_messages(self):
        self.messages = [{"role": "system",
                          "content": "You are a helpful assistant."}]

    def schedule_calendar_time(self, time):
        # This is where you would add the code to schedule a time on the
        # calendar
        from calendar_integration import add_event
        add_event()

    def send_email(self, to, body):
        # This is where you would add the code to send an email
        from email_integration import main as send_email
        send_email()