"""This module is responsible for sending daily inspirational quotes via SMS."""

import time
from twilio.rest import Client
import openai

# Your Twilio account SID and auth token
ACCOUNT_SID = 'Your Twilio account SID'
AUTH_TOKEN = 'Your Twilio auth token'

# Your OpenAI API key
OPENAI_API_KEY = 'Your OpenAI API key'

# Create a Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Create an OpenAI client
openai.api_key = OPENAI_API_KEY

completion = openai.Completion.create(engine="text-davinci-002")

# The phone numbers to send the quote to
phone_numbers = ['+1234567890', '+0987654321']  # Add more numbers as needed

# The interval between quotes (in seconds)
QUOTE_INTERVAL = 60 * 60 * 24  # 24 hours

while True:
    # Use GPT-3 to generate an inspirational quote
    PROMPT = "Create an inspirational quote"
    response = completion.create(prompt=PROMPT, max_tokens=60)
    quote = response['choices'][0]['text']['content'].strip()

    # Send the quote to each phone number
    for phone_number in phone_numbers:
        client.messages.create(
            body=quote,
            from_='Your Twilio phone number',
            to=phone_number
        )

    # Wait for the next quote
    time.sleep(QUOTE_INTERVAL)
