class Private:
    def __init__(self, e, p, q):
        self.phi = (p - 1) * (q - 1)
        self.d = pow(e, -1, self.phi)
        self.n = p * q
    
    def decrypt():
        pass
