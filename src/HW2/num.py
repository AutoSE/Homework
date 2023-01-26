import math
import re

class Num:
    def __init__(self, at=None, txt=None):
        self.at, self.txt = at if at else 0, txt if txt else ""
        self.n, self.mu, self.m2 = 0,0,0
        self.mu=0
        self.n=0
        self.lo, self.hi = float("inf"), float("-inf")
        self.w = -1 if "-" in self.txt else 1 

    def add(self,n):
        if n != '?':
            n=int(n)
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + d/self.n
            self.m2 = self.m2 + d*(n-self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)

    def mid(self,x):
        return self.mu

    def div(self,x):
        return 0 if self.m2<0 or self.n<2 else (self.m2/(self.n-1))**0.5

    def rnd(self,x,n):
        return x if x=='?' else self.rnd(x,n)