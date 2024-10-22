"""
cryptography_tests/fernet_instance.py: Defines a Fernet wrapper class
Authors: Joe Doyle, Jack Doyle
"""

from cryptography.fernet import Fernet as F

class Fernet:
    def __init__(self):
        self.key = F.generate_key()
        self.f = F(self.key)
    
    def encrypt(self, message):
        return (self.f).encrypt(message)
    
    def decrypt(self, token):
        return (self.f).decrypt(token)
