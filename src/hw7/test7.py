import cli as c
import num as n
import sym as s
import Utils as u
import os
import random

egs={}

def ok(n=1):
    random.seed(n)

def samples():
    for i in range(1,11):
        print("",''.join(u.samples(["a","b","c","d","e"])))

def num():
    k=n.Num([1,2,3,4,5,6,7,8,9,10])
    print("",k.n, k.mu, k.sd)

def gaussian():
    t=[]
    for i in range(1, 10001):
        t.append(u.gaussian(10, 2))
    k=n.Num(t)
    print("",k.n, k.mu, k.sd)

def all():
    print('ok')
    egs['ok']=ok()
    print('samples')
    egs['samples']=samples()
    print('num')
    egs['num']=num()
    print('gaussian')
    egs['gaussian']=gaussian()


