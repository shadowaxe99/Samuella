"""This module is responsible for integrating with external services."""

import requests


def send_request(url, headers, data):
    try:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Failed to send request: {response.text}')
    except Exception:
        print('An error occurred while sending the request.')