import binascii
import os


def generate_key():
    """Generate a completely random string"""
    return binascii.hexlify(os.urandom(20)).decode()
