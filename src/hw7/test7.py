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

def all():
    print('ok')
    egs['ok']=ok()
    print('samples')
    egs['samples']=samples()


