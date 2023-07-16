from sms_handler import app, handle_incoming_message
from twilio.twiml.messaging_response import MessagingResponse

def handle_incoming_message(incoming_msg, phone_number, resp):
    """Handle incoming messages for the twilio receive sms functionality."""
    # Basic logic to respond based on the incoming message
    if 'hello' in incoming_msg:
        resp.message("Hello, this is your Python app responding to your SMS")
    elif 'bye' in incoming_msg:
        resp.message("Goodbye!")
    elif 'how are you' in incoming_msg:
        resp.message("I'm an AI, I don't have feelings, but I'm functioning as expected.")
    elif 'what is your name' in incoming_msg:
        resp.message("I'm your friendly Python app.")
    elif 'tell me a joke' in incoming_msg:
        resp.message("Why don't scientists trust atoms? Because they make up everything!")
    else:
        resp.message("I didn't understand your message.")