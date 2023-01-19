import math
Seed = 937162211

#Numerics
def rint(lo, hi):
    return math.floor(0.5 + rand(lo, hi))

def rand(lo, hi):
    lo, hi = (lo or 0), (hi or 1)
    global Seed
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi-lo) * Seed / 2147483647

def rnd(n, nPlaces):
    mult = 10**nPlaces 
    return math.floor(n * mult + 0.5) / mult