"""This module is responsible for handling family mode operations."""

import openai
from openai import OpenAI, GPT3Encoder, GPT3Completion

OPENAI_API_KEY = 'your_openai_api_key'

client = OpenAI()


def handle_family_message(message):
    prompt = f'You are an AI assistant for a family. A family member sends you the following message: "{message}"'
    completion = GPT3Completion.create(model='text-davinci-002', prompt=prompt, max_tokens=100)
    response = completion.choices[0].text.strip()
    return response