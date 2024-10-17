def decrypt(message, priv):
    decrypted = []
    
    for m in message:
        decrypted.append(priv.decrypt(m))
    
    return decrypted