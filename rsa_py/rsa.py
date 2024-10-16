from private import Private
from public import Public
import decrypt as dec
import encrypt as enc
import os
from sympy import isPrime

class RSA:
    def __init__(self, pe = 65537, ks = 2048):
        self.p = 1  
        while not isPrime(self.p):
            self.p = os.urandom(ks // 8)
        
        self.q = 1
        
        while not isPrime(self.p):
            self.q = os.urnadom(ks // 8)
            
        self.private = Private(pe, self.p, self.q)
        self.public = Public(pe, self.p, self.q)

    def encrypt(self, message):
        return enc(message, self.public)
    
    def decrypt(self, message):
        return dec(message, self.private)
