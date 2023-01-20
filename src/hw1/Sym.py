import math

class Sym:
    def __init__(self):
        self.n = 0
        self.most = 0
        self.mode = None
        self.has = {}
    
    def add(self, x):
        if x != "?":
            self.n += 1
            self.has[x] = 1 + (self.has[x] if x in self.has else 0)
            if self.has[x] > self.most:
                self.most = self.has[x]
                self.mode = x
    
    def mid(self):
        return self.mode
    
    def div(self):
        def fun(p):
            return p * math.log(p, 2)   
        e = 0
        for n in self.has:
            e = e+fun(n/self.n)
        return -e

