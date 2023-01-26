import cli as c
import num as n
import sym as s
import Utils as u
import os

egs={}


def the():
    print(c.the)
    egs['the'] = c.the
    return True

def sym():
    sym_obj = s.Sym()
    for k,x in enumerate(["a","a","a","a","b","b","c"]):
        sym_obj.add(x)
    egs['sym'] = "a" == sym_obj.mid() and 1.379 == u.rnd(sym_obj.div())
    return "a" == sym_obj.mid() and 1.379 == u.rnd(sym_obj.div())

def num():
    num_obj = n.Num()
    for k,x in enumerate([1,1,1,1,2,2,3]):
        num_obj.add(x)
    egs['num'] = 11/7 == num_obj.mid() and 0.787 == u.rnd(num_obj.div())
    return 11/7 == num_obj.mid() and 0.787 == u.rnd(num_obj.div())

def csv_help(t):
    global line
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





