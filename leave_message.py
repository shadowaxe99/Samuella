"""This module is responsible for handling incoming messages."

from twilio.twiml.messaging_response import MessagingResponse
from sms_handler import app

@app.route('/sms', methods=['POST'])
def sms_reply():
    '''Responds to incoming messages with a thank you message.'''
    resp = MessagingResponse()
    resp.message('Thank you for your message. We will get back to you soon.')
    return str(resp)
