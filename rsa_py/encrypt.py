def encrypt(message, pub):
    """
    Takes a message and uses the Public class to encrypt the message character by character.
    Returns a list of the encrypted characters.
    """
    encrypted = []
    
    for m in message:
        encrypted.append(pub.encrypt(m))
    
    return encrypted
