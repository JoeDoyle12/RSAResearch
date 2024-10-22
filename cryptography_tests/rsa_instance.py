"""
rsa_instance.py: Defines RSA wrapper class
Authors: Joe Doyle, Jack Doyle
"""

from cryptography.hazmat.primitives.asymmetric import (rsa, padding)
from cryptography.hazmat.primitives import hashes

class RSA:
    def __init__(self, pe = 65537, ks = 2048):
        self.private_key = rsa.generate_private_key(
            public_exponent=pe,
            key_size=ks,
        )
        self.public_key = (self.private_key).public_key()
        

    def encrypt(self, message):
        ciphertext = self.public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext
    
    def decrypt(self, ciphertext):
        plaintext = (self.private_key).decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext
