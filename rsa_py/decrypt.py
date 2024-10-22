"""
decrypt.py: Decrypt entire messages
Author: Joe Doyle
"""

def decrypt(message, priv):
    decrypted = []
    
    for m in message:
        decrypted.append(priv.decrypt(m))
    
    return decrypted