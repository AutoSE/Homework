import cli as c
import num as n
import sym as s
import Utils as u
import os

egs={}
global line

def the():
    print(c.the)
    egs['the'] = c.the
    return True

def sym():
    sym = s.Sym()
    for k,x in enumerate(["a","a","a","a","b","b","c"]):
        sym.add(x)
    egs['sym'] = "a" == sym.mid() and 1.379 == u.rnd(sym.div())
    return "a" == sym.mid() and 1.379 == u.rnd(sym.div())

def num():
    num = n.Num()
    for k,x in enumerate([1,1,1,1,2,2,3]):
        num.add(x)
    egs['num'] = 11/7 == num.mid() and 0.787 == u.rnd(num.div())
    return 11/7 == num.mid() and 0.787 == u.rnd(num.div())

def csv_help(t):
    line += len(t)
def csv():
    n=0
    
    u.csv(c.the["file"],csv_help)
    egs['csv'] = n == 8*399
    return n == 8*399

def data():
    pass

def stats():
    pass



print(the())
print(sym())
print(num())
print(csv())
print(egs)





