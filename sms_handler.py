"""This module is responsible for handling incoming SMS messages."""

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def handle_incoming_message():
    number = request.form['From']
    message_body = request.form['Body']

    resp = MessagingResponse()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(resp)