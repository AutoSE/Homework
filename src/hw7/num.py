import re
import Utils as u
import cli as g

class Num:
    def __init__(self, t=None):
        self.n, self.mu, self.m2 = 0,0,0
        self.sd=0
        for w in t or []:
            self.add(w)

    def add(self,n):
        self.n+= 1
        d=n -self.mu
        self.mu=self.mu+(d/self.n)
        self.m2=self.m2+(d*(n-self.mu))
        self.sd= 0 if self.n<2 else (self.m2/(self.n-1))**0.5

    def mid(self):
        return self.mu

    def div(self):
        return 0 if self.m2<0 or self.n<2 else (self.m2/(self.n-1))**0.5

    def rnd(self,x,n):
        return x if x=='?' else u.rnd(x,n)

    def norm(self, n):
        return n if n == "?" else (n-self.lo)/(self.hi - self.lo + 10**-32)

    def dist(self, n1, n2):
        if n1 == "?" and n2 == "?":
            return 1
        n1, n2 = self.norm(n1), self.norm(n2)
        if n1 == "?":
            n1 = 1 if n2 < 0.5 else 0
        if n2 == "?":
            n2 = 1 if n1 < 0.5 else 0
        return abs(n1 - n2)
