"""
des_instance.py: Define DES class
Author: Jack Doyle
"""

import des_py.des_boxes as F
import secrets

class DES: 
    def __init__(self):
        secure_rng = secrets.SystemRandom()
        self.key = secure_rng.getrandbits(64)
        
    def message_to_int(self, mess):
        message = mess
        
        while len(message) % 8 != 0:
            message += b"\x00"
        
        submessages = []
        
        for i in range(0, len(message), 8):
            submessages.append(message[i:i+8])
        
        message_nums = []
        
        for m in submessages:
            message_nums.append(int.from_bytes(m, "big"))
        
        return message_nums
    
    def int_to_message(self, message):
        decrypted_bytes = b""
        for n in message:
            decrypted_bytes += n.to_bytes(8, "big")
        
        return decrypted_bytes
        
    
    def encrypt(self, mess):
        message_nums = self.message_to_int(mess)
    
        encrypted = []
        
        for m in message_nums:
            encrypted.append(F.des_encrypt(m, self.key))
        
        encrypted_bytes = self.int_to_message(encrypted)
        
        return encrypted_bytes
        
    
    def decrypt(self, mess):
        message_nums = self.message_to_int(mess)
        
        decrypted = []
        
        for m in message_nums:
            decrypted.append(F.des_decrypt(m, self.key))
        
        decrypted_bytes = self.int_to_message(decrypted)
        
        return decrypted_bytes
    