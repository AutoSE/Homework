import cli as c
import num as n
import sym as s
import Utils as u
import os
import Data as d

egs={}
line=0

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
    egs['csv'] = line == 8*399
    return line == 8*399

def data():
    data = d.Data(c.the["file"])
    return len(data.rows) == 398 and data.cols.y[0].w == -1 and data.cols.x[1].at == 1 and len(data.cols.x) == 4

def stats():
    data = d.Data(c.the['file'])
    for k, cols in {'y' : data.cols.y, 'x' : data.cols.x }.items():
        print(k, 'mid', data.stats('mid', cols, 2))
        print(' ', 'div', data.stats('div', cols, 2))
    return True



def all():
  egs['the']=the()
  egs['csv']=csv()
  egs['data']=data()
  egs['stats']=stats()
  egs['sym']=sym()
  egs['num']=num()





