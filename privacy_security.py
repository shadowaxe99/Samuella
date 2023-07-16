"""This module is responsible for privacy and security related operations."""

import hashlib
import os


def hash_password(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + key


def verify_password(stored_password, provided_password):
    salt = stored_password[:32]
    stored_key = stored_password[32:]
    key = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return key == stored_key


from cryptography.fernet import Fernet

def encrypt_data(data):
    # Generate a key
    key = Fernet.generate_key()

    # Create a cipher object
    cipher_suite = Fernet(key)

    # Encrypt the data
    cipher_text = cipher_suite.encrypt(data.encode('utf-8'))

    return cipher_text


def decrypt_data(encrypted_data, key):
    # Create a cipher object
    cipher_suite = Fernet(key)

    # Decrypt the data
    plain_text = cipher_suite.decrypt(encrypted_data).decode('utf-8')

    return plain_text