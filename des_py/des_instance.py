import des_boxes as F
import secrets

class DES: 
    def __init__(self):
        secure_rng = secrets.SystemRandom()
        self.key = secure_rng.getrandbits(64)
        
    def encrypt(self, message):
        decrypted = []
        
        for m in message:
            decrypted.append(F.encrypt(m, self.key))
    
    def decrypt(self, message):
        decrypted = []
        
        for m in message:
            decrypted.append(F.decrypt(m, self.key))
        
        return decrypted
    