import math,re
Seed = 937162211

def settings(s):
    return dict(re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)",s))

#Numerics
def rint(lo, hi):
    return math.floor(0.5 + rand(lo, hi))

def rand(lo, hi):
    lo= lo or 0
    hi= hi or 1
    global Seed
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi-lo) * Seed / 2147483647

def rnd(n, nPlaces=3    ):
    mult = 10**nPlaces 
    return math.floor(n * mult + 0.5) / mult

#Strings
def fmt(sControl):
    return str(sControl)

def oo(t):
    print(t)
    return t

def coerce(s):
    return int(s) if s.isdigit() else s


