"""
rsa_py/encrypt.py: Encrypt entire messages
Author: Joe Doyle
"""

def encrypt(message, pub):
    encrypted = []
    
    for m in message:
        encrypted.append(pub.encrypt(m))
    
    return encrypted