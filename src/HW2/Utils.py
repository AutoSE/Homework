import math
import sys
import re
import math
from pathlib import Path
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
    if s=='true' or s=='True':
        return True
    elif s=='false' or s=='False':
        return False
    elif s.isdigit():
        return int(s)
    elif '.' in s:
        if s.replace('.','').isdigit():
            return float(s)
        else:
            return s
    else:
        return s

def csv(sFilename, fun):
    sFilename=Path(sFilename)
    t=[]
    f=open(sFilename.absolute(),'r')
    lines=f.readlines()
    for line in lines:
        t=[]
        for s in re.findall("([^,]+)", line):
            t.append(coerce(s))
        fun(t)



#Lists
def map(t, fun):
    u={}
    for k,v in enumerate(t):
        v,k=fun(v)
        if k:
            u[k]=v
        else:
            u[1+len(u)]=v
    return u

def kap(t, fun):
    u={}
    for k,v in enumerate(t):
        v,k=fun(k,v)
        if k:
            u[k]=v
        else:
            u[len(u)+1]=v
    return u
