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
                self.most,self.mode = self.has[x], x
    
    def mid(self):
        return self.mode
    
    def div(self):
        def fun(p):
            return p * math.log(p, 2)   
        e = 0
        for _, n in self.has.items():
            if n > 0:
                e = e+fun(n/self.n)
        return -e
