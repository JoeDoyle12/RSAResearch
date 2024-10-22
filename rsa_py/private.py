"""
private.py: Helper class for privately kept variables in RSA implementation
Author: Joe Doyle
"""
class Private:
    def __init__(self, e, p, q):
        self.phi = (p - 1) * (q - 1)
        self.d = pow(e, -1, self.phi)
        self.n = p * q
    
    def decrypt(self, message):
        return pow(message, self.d, self.n)
    