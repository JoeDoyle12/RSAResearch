"""
rsa_py/rsa.py: Define a hommade implementation of RSA
Authors: Joe Doyle, Jack Doyle
"""

from rsa_py.private import Private
from rsa_py.public import Public
from  rsa_py.decrypt import decrypt as dec
from rsa_py.encrypt import encrypt as enc
from sympy import isprime
import secrets

class RSA:
    def __init__(self, pe = 65537, ks = 2**256):
        secure_rng = secrets.SystemRandom()

        self.p = 1  
        while not isprime(self.p):
            self.p = secure_rng.randrange(ks // 8, ks)
        
        self.q = 1
        
        while not isprime(self.q):
            self.q = secure_rng.randrange(ks // 8, ks)
            
        self.private = Private(pe, self.p, self.q)
        self.public = Public(pe, self.p, self.q)

    def encrypt(self, message):
        return enc(message, self.public)
    
    def decrypt(self, message):
        return dec(message, self.private)
