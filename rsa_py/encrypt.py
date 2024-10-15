def encrypt(message, pub):
    encrypted = []
    
    for m in message:
        encrypted.append(pub.encrypt(m))
    
    return encrypted