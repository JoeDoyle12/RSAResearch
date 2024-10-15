class Public:
    def __init__(self, e, p, q):
        """
        Initialize object containing public data
        """
        self.n = p * q
        self.e = e
    
    def encrypt(self, num):
        return pow(num, self.e, self.n)